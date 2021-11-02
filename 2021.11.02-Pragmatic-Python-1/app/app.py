import argparse
import os
import re
import shutil
from typing import Union
import unicodedata

import bs4
from bs4.element import ResultSet, Tag
import requests

from .items import Item


DEFAULT_OUTPUT_PATH = os.path.abspath("out")


def get(url: str, **kwargs) -> requests.Response:
    response = requests.get(url, **kwargs)
    response.raise_for_status()
    return response


def find_element(soup: Union[bs4.BeautifulSoup, Tag], selector: str, **kwargs):
    element = soup.select_one(selector, **kwargs)
    if element is None:
        raise ValueError(f"No element with selector={selector} found.")
    return element


def parse_price(text: str) -> int:
    price_match = re.match(r"\$(\d+)", text)
    if price_match is None:
        raise ValueError(f"Could not parse result_price from text={text}")
    price = int(price_match.groups()[0])
    return price


def parse_image_urls(tag: Tag) -> list[str]:
    image_ids = tag["data-ids"]
    if isinstance(image_ids, str):
        image_ids = image_ids.split(",")
    image_ids = [
        re.sub(r"\d:","", image_id)
        for image_id
        in image_ids
    ]
    image_urls = [
        f"https://images.craigslist.org/{data_id}_300x300.jpg"
        for data_id
        in image_ids
    ]
    return image_urls


# See: https://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename
def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def download_item_images(item: Item, output: str):
    filename_prefix = f"{slugify(item.title)}_"
    for index, url in enumerate(item.image_urls):
        response = get(url, stream=True)
        filename = f"{filename_prefix}{index}.jpg"
        filepath = os.path.join(output, filename)
        # See: https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
        with open(filepath, "wb") as outfile:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, outfile)


def parse_items(soup: bs4.BeautifulSoup) -> list[Item]:
    items: list[Item] = []
    results: ResultSet[Tag] = soup.find_all("li", class_="result-row") 
    for result in results:
        title_element = find_element(result, ".result-title")
        price_element = find_element(result, ".result-price")
        image_container_element = find_element(result, ".result-image")
        title = title_element.text
        price = parse_price(price_element.text)
        image_urls = parse_image_urls(image_container_element)
        item = Item(title, price, image_urls=image_urls)
        items.append(item)
    return items


def find_lowest_priced_item(items: list[Item]) -> Item:
    item_prices = [item.price for item in items]
    lowest_price = min(item_prices)
    lowest_price_index = item_prices.index(lowest_price)
    lowest_price_item = items[lowest_price_index]
    return lowest_price_item


def parse_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--lowest", action="store_true")
    parser.add_argument("--images", action="store_true")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT_PATH)
    cli_args = parser.parse_args()
    return cli_args


def main():
    cli_args = parse_cli_args()
    response = get(cli_args.url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    items = parse_items(soup)

    if cli_args.lowest:
        lowest_priced_item = find_lowest_priced_item(items)
        print(f"{lowest_priced_item.title} is the lowest priced vehicle at ${lowest_priced_item.price}")
    elif cli_args.images:
        output = cli_args.output
        for item in items:
            download_item_images(item, output=output)
    else:
        for item in items:
            print(item.title)


if __name__ == "__main__":
    main()

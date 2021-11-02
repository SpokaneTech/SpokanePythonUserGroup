import argparse
import re

import bs4
from bs4.element import ResultSet, Tag
import requests

from .items import Item


items: list[Item] = []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()

    url: str = args.url
    response = requests.get(url)
    if not response.ok:
        raise ValueError(f"url={url} returned status_code={response.status_code}")
    
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results: ResultSet[Tag] = soup.find_all("li", class_="result-row") 
    for result in results:
        title_element = result.select_one(".result-title")
        if title_element is None:
            raise ValueError("No element with .result-title found.")

        price_element = result.select_one(".result-price")
        if price_element is None:
            raise ValueError("No element with .result-price found.")

        title = title_element.text

        price_match = re.match(r"\$(\d+)", price_element.text)
        if price_match is None:
            raise ValueError(f"Could not parse result_price={price_element}")
        price = int(price_match.groups()[0])

        item = Item(title, price)
        items.append(item)

    item_prices = [item.price for item in items]
    lowest_price = min(item_prices)
    lowest_price_index = item_prices.index(lowest_price)
    lowest_price_item = items[lowest_price_index]
    print(f"{lowest_price_item.title} is the lowest priced vehicle at ${lowest_price}")


if __name__ == "__main__":
    main()

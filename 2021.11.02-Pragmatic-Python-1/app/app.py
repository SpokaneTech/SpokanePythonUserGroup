import argparse

import bs4
from bs4.element import ResultSet, Tag
import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", "-U", required=True)
    args = parser.parse_args()

    url: str = args.url
    response = requests.get(url)
    if not response.ok:
        raise ValueError(f"url={url} returned status_code={response.status_code}")
    
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results: ResultSet[Tag] = soup.find_all("li", class_="result-row") 
    for result in results:
        print(result["data-pid"])
        result_title = result.select_one(".result-title")
        if result_title is None:
            raise ValueError("No element with .result-title found.")
        print(result_title.text)


if __name__ == "__main__":
    main()

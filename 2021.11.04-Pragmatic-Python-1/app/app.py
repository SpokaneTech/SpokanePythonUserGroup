import argparse

import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", "-U", required=True)
    args = parser.parse_args()

    url: str = args.url
    response = requests.get(url)
    if not response.ok:
        raise ValueError(f"url={url} returned status_code={response.status_code}")


if __name__ == "__main__":
    main()

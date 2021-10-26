import argparse

import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", "-U", required=True)
    args = parser.parse_args()

    response = requests.get(args.url)
    print(response.status_code)
    


if __name__ == "__main__":
    main()

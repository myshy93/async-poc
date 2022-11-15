import asyncio
from pathlib import Path
from time import perf_counter
import requests

ROOT_DIR = Path(__file__).parent
DOWNLOAD_DIR = ROOT_DIR / "downloads"
IMG_URL_TEMPLATE = "https://httpcats.com/{}.jpg"

DOWNLOAD_DIR.mkdir(exist_ok=True)


def download_content(url, file_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, "wb") as fout:
        fout.write(response.content)


def main():
    codes = list(range(400, 460))
    print("STARTING TO DOWNLOAD")
    print(f"{len(codes)} codes in queue.")
    print("-" * 30)

    start = perf_counter()

    for i in codes:
        url = IMG_URL_TEMPLATE.format(i)
        file_path = DOWNLOAD_DIR / f"{i}.jpg"

        try:
            print(f"HTTP Request to {url}.")
            download_content(url, file_path)
        except requests.HTTPError as err:
            print(err)
        else:
            print(f"Response saved to {file_path}")

    print(f"FINISH in {perf_counter() - start}")


if __name__ == "__main__":
    main()

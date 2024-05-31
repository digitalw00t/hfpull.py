#!/usr/bin/env python3

import os
import subprocess
import argparse

def download_and_rename(url):
    # Use wget to download the file
    subprocess.run(["wget", url])

    # Extract the filename from the URL
    filename = url.split("/")[-1].split("?")[0]

    # Rename the downloaded file
    os.rename(filename + "?download=true", filename)

    print(f"Downloaded and renamed the file to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Download a file and rename it to remove the query string.")
    parser.add_argument('url', type=str, help='The URL of the file to download')

    args = parser.parse_args()
    download_and_rename(args.url)

if __name__ == "__main__":
    main()


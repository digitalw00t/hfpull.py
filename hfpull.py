#!/usr/bin/env python3

import os
import subprocess
import argparse
import requests
from bs4 import BeautifulSoup

def download_and_rename(url):
    # Use wget to download the file
    subprocess.run(["wget", url])

    # Extract the filename from the URL
    filename = url.split("/")[-1].split("?")[0]

    # Rename the downloaded file
    os.rename(filename + "?download=true", filename)

    return filename

def fetch_model_card(url):
    # Fetch the HTML content of the model card page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the text from the HTML content
    model_card_text = soup.get_text()

    return model_card_text

def create_markdown_file(filename, url, model_card_text):
    # Create a markdown file with the model card text and download URL
    markdown_filename = filename.replace(".gguf", ".md")
    with open(markdown_filename, 'w') as md_file:
        md_file.write(f"# Model Card for {filename}\n\n")
        md_file.write(f"## Download URL\n{url}\n\n")
        md_file.write("## Model Card\n")
        md_file.write(model_card_text)
    print(f"Created markdown file: {markdown_filename}")

def main():
    parser = argparse.ArgumentParser(description="Download a file and create a markdown file with the model card.")
    parser.add_argument('url', type=str, help='The URL of the file to download')

    args = parser.parse_args()
    
    # Download and rename the file
    filename = download_and_rename(args.url)
    
    # Construct the model card URL
    base_url = args.url.split('/resolve/')[0]
    model_card_url = base_url

    # Fetch the model card text
    model_card_text = fetch_model_card(model_card_url)
    
    # Create the markdown file
    create_markdown_file(filename, args.url, model_card_text)

if __name__ == "__main__":
    main()


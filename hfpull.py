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
    markdown_filename = filename.replace(".gguf", ".card")
    with open(markdown_filename, 'w') as md_file:
        md_file.write(f"# Model Card for {filename}\n\n")
        md_file.write(f"## Download URL\n{url}\n\n")
        md_file.write("## Model Card\n")
        md_file.write(model_card_text)
    print(f"Created markdown file: {markdown_filename}")

def derive_model_name_and_card_filename(url):
    # Normalize URL to ensure it has a consistent format
    if not url.startswith("https://"):
        url = "https://huggingface.co/" + url

    # Extract model name from the URL
    parts = url.split('/')
    model_name = ""
    card_filename = ""
    
    for part in parts:
        if 'GGUF' in part:
            model_name = '-'.join(part.split('-')[:-1])
            card_filename = part + ".card"
            break

    if not model_name:
        # Handle case when 'GGUF' is not directly in the URL part
        model_name = parts[-1]
        card_filename = model_name + ".card"
    
    return model_name, card_filename

def main():
    parser = argparse.ArgumentParser(description="Download a file and create a markdown file with the model card.")
    parser.add_argument('url', type=str, help='The URL of the file to download or the model card to fetch')
    parser.add_argument('--card', action='store_true', help='Fetch only the model card')

    args = parser.parse_args()

    # Derive model name and card filename from URL
    model_name, card_filename = derive_model_name_and_card_filename(args.url)
    if not model_name or not card_filename:
        print("Unable to derive model name and card filename from the URL")
        return

    # Determine whether to download the model file or only fetch the card
    if '/resolve/' in args.url:
        # Download and rename the file
        filename = download_and_rename(args.url)
        
        # Construct the model card URL
        model_card_url = '/'.join(args.url.split('/')[:5])
        if not model_card_url.startswith("https://"):
            model_card_url = "https://huggingface.co/" + model_card_url

        # Fetch the model card text
        model_card_text = fetch_model_card(model_card_url)
        
        # Create the markdown file
        create_markdown_file(filename, args.url, model_card_text)
    else:
        # Construct the model card URL
        model_card_url = '/'.join(args.url.split('/')[:5])
        if not model_card_url.startswith("https://"):
            model_card_url = "https://huggingface.co/" + model_card_url

        # Fetch the model card text
        model_card_text = fetch_model_card(model_card_url)

        # Create the markdown file
        create_markdown_file(card_filename, model_card_url, model_card_text)

if __name__ == "__main__":
    main()


# hfpull.py

`hfpull.py` is a Python script designed to download files from URLs and create corresponding model card markdown files. The script can fetch and process URLs from Hugging Face, deriving model names and generating markdown files containing model cards.

## Features

- Download files from specified URLs.
- Generate markdown files with model card information.
- Handle different URL formats to extract model names and card filenames.
- Support a `--card` option to fetch only the model card.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using:

```sh
pip install requests beautifulsoup4
Usage
Download a file and create a model card
To download a file from a URL and create a corresponding model card markdown file, use:

python3 hfpull.py <url>
Fetch only the model card
To fetch only the model card without downloading the file, use the --card option:

python3 hfpull.py <url> --card
Examples
Download a file and create a model card
python3 hfpull.py https://huggingface.co/xxx777xxxASD/PrimaMonarch-EroSumika-2x10.7B-128k-GGUF/resolve/main/PrimaMonarch-EroSumika-2x10.7B-128k-Q5_K_S.gguf?download=true
Fetch only the model card
python3 hfpull.py xxx777xxxASD/PrimaMonarch-EroSumika-2x10.7B-128k-GGUF --card
How It Works
The script accepts a URL as an argument.
It determines whether the URL points to a downloadable file or a model card page.
If the URL points to a file (/resolve/ in the URL), it downloads the file and creates a markdown file with the model card.
If the URL does not point to a file, it fetches the model card and creates a markdown file.
The model name and card filename are derived from the URL.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add new feature').
Push the branch to GitHub (git push origin feature-branch).
Create a pull request.
License
This project is licensed under the MIT License.

Acknowledgements
Hugging Face for their model hosting platform.
Contributors to the requests and beautifulsoup4 libraries.

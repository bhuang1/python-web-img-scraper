# Python Web Image Scraper

This project is a Python script to scrape and download images from a given URL. It uses `selenium` to handle dynamic web pages and `BeautifulSoup` for parsing HTML.

## Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager
- Mozilla Firefox

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/python-web-img-scraper.git
    cd python-web-img-scraper
    ```

2.  Create the virtual environment using `uv`:
    ```bash
    uv venv
    ```

## Usage

To run the script, use the following command:

```bash
uv run python scraper.py <URL>
```

Replace `<URL>` with the full URL of the web page you want to scrape.

**Example:**

```bash
uv run python scraper.py https://www.example.com
```

The script will create an `img` directory in the project root and save the downloaded images there.

## How It Works

1.  **Fetches Page with Selenium:** The script uses `selenium` with the Firefox WebDriver to load the target URL. This is crucial for websites that load content dynamically with JavaScript.
2.  **Parses HTML:** Once the page is loaded, `BeautifulSoup` parses the final HTML source code.
3.  **Finds Image Tags:** It searches for all `<img>` tags in the HTML.
4.  **Downloads Images:** For each image found, it constructs the absolute URL and downloads the image file (`.png` or `.jpg`) into the local `img/` directory.

## Dependencies

- `beautifulsoup4>=4.13.4`
- `requests>=2.32.4`
- `selenium>=4.34.2`
- `webdriver-manager>=4.0.2`

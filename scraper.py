
import os
import sys
import time
from urllib.parse import urljoin
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

def scrape_images(url):
    try:
        # Use webdriver-manager to automatically handle the GeckoDriver
        service = Service(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')  # Run in headless mode (no GUI)
        driver = webdriver.Firefox(service=service, options=options)
    except Exception as e:
        print(f"Error setting up Selenium for Firefox: {e}")
        print("Please ensure you have Mozilla Firefox installed.")
        return

    print("Fetching page with Selenium (Firefox)...")
    driver.get(url)

    # Wait for the page and any JavaScript (like Cloudflare's check) to load
    time.sleep(5)

    # Get the final page source after JavaScript execution
    html = driver.page_source
    driver.quit()

    # --- Parse HTML and Download Images ---
    soup = BeautifulSoup(html, 'html.parser')
    img_tags = soup.find_all('img')

    if not img_tags:
        print("No image tags found. The page might not have loaded correctly.")
        return

    if not os.path.exists('img'):
        os.makedirs('img')

    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    }
    session.headers.update(headers)

    for img in img_tags:
        img_url = img.get('src')
        if img_url:
            img_url = urljoin(url, img_url)
            if img_url.lower().endswith(('.png', '.jpg')):
                try:
                    print(f"Downloading {img_url}...")
                    img_data = session.get(img_url).content
                    filename = os.path.join('img', os.path.basename(img_url))
                    with open(filename, 'wb') as f:
                        f.write(img_data)
                    print(f"Saved to {filename}")
                    time.sleep(1)
                except requests.exceptions.RequestException as e:
                    print(f"Error downloading {img_url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: uv run python scraper.py <URL>")
    else:
        try:
            from webdriver_manager.firefox import GeckoDriverManager
        except ImportError:
            print("webdriver-manager is not installed. Please run:")
            print("uv pip install webdriver-manager")
            sys.exit(1)

        scrape_images(sys.argv[1])

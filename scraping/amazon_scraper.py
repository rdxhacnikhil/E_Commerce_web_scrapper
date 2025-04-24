from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from datetime import datetime
# import pandas as pd
# import time
# import random

# def setup_driver():
#     # Same setup logic as Flipkart scraper
#     ...

# def scrape_amazon_mobiles(driver, pages=1):
#     all_products = []
#     for page in range(1, pages + 1):
#         print(f"\nScraping Amazon - Page {page}")
#         url = f"https://www.amazon.com/s?k=mobiles&page={page}"
#         driver.get(url)
#         time.sleep(random.uniform(2, 4))

#         try:
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
#             )
#         except:
#             print(f"Timeout on page {page}")
#             continue

#         soup = BeautifulSoup(driver.page_source, 'html.parser')
#         containers = soup.select("div.s-main-slot div[data-asin]:not([data-asin=''])")

#         for item in containers:
#             title_tag = item.select_one("h2 a span")
#             price_whole = item.select_one("span.a-price-whole")
#             price_fraction = item.select_one("span.a-price-fraction")
#             rating_tag = item.select_one("span.a-icon-alt")

#             if not title_tag or not price_whole:
#                 continue

#             price = f"{price_whole.text.strip()}.{price_fraction.text.strip()}" if price_fraction else price_whole.text.strip()
#             product = {
#                 'timestamp': datetime.now().isoformat(),
#                 'title': title_tag.text.strip(),
#                 'price': float(price.replace(",", "")),
#                 'rating': rating_tag.text.strip() if rating_tag else None,
#                 'page_number': page
#             }
#             print(f"✔ {product['title'][:40]}... (${product['price']})")
#             all_products.append(product)

#     return all_products

# def save_data(data, filename='data/amazon_mobiles.csv'):
#     df = pd.DataFrame(data)
#     df.to_csv(filename, index=False)
#     print(f"\nSaved {len(data)} products to {filename}")
# scraping/amazon_scraper.py
import time
import json
import os
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException

# def get_amazon_mobile_data(pages=40):
#     # Setup WebDriver
#     driver = webdriver.Chrome()  # Adjust based on your browser setup
    
#     products = []
#     base_url = "https://www.amazon.in/s?i=electronics&rh=n%3A1389432031&s=popularity-rank&fs=true&ref=lp_1389432031_sar"

#     for page in range(1, pages + 1):
#         url = f"{base_url}&page={page}"
#         driver.get(url)
        
#         # Wait for products to load
#         try:
#             WebDriverWait(driver, 15).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "div.puis-card-container"))
#             )
#         except TimeoutException:
#             print(f"Timeout on page {page}. Moving to next page.")
#             continue
        
#         # Extract all product cards
#         product_cards = driver.find_elements(By.CSS_SELECTOR, "div.puis-card-container")
        
#         for card in product_cards:
#             product = {}
            
#             # Product Name
#             try:
#                 name = card.find_element(By.CSS_SELECTOR, "h2.a-size-base-plus span").text
#                 product['name'] = name
#             except NoSuchElementException:
#                 product['name'] = 'N/A'
            
#             # Price
#             try:
#                 price = card.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
#                 product['price'] = price.replace(',', '')
#             except NoSuchElementException:
#                 product['price'] = 'N/A'
            
#             # Rating
#             try:
#                 rating_element = card.find_element(By.CSS_SELECTOR, "i.a-icon-star-small")
#                 rating_text = rating_element.get_attribute('aria-label')
#                 product['rating'] = rating_text.split(' ')[0]
#             except (NoSuchElementException, AttributeError):
#                 product['rating'] = 'N/A'
            
#             # Number of Reviews
#             try:
#                 reviews = card.find_element(By.CSS_SELECTOR, "span.a-size-base.s-underline-text").text
#                 product['reviews'] = reviews.replace(',', '')
#             except NoSuchElementException:
#                 product['reviews'] = 'N/A'
            
#             # Product URL
#             try:
#                 url = card.find_element(By.CSS_SELECTOR, "a.a-link-normal.s-no-outline").get_attribute('href')
#                 product['url'] = url
#             except NoSuchElementException:
#                 product['url'] = 'N/A'
            
#             products.append(product)
        
#         time.sleep(2)  # Delay to prevent blocking
    
#     driver.quit()
#     return products
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# import random

# def get_amazon_mobile_data(pages=40):
#     # Setup headless driver with user-agent
#     options = Options()
#     options.add_argument("--headless=new")
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

#     driver = webdriver.Chrome(options=options)

#     products = []
#     base_url = "https://www.amazon.in/s?i=electronics&rh=n%3A1389432031&s=popularity-rank&fs=true&ref=lp_1389432031_sar"

#     for page in range(1, pages + 1):
#         print(f"\nScraping page {page}...")
#         url = f"{base_url}&page={page}"
#         driver.get(url)

#         try:
#             # CAPTCHA check
#             if "captcha" in driver.current_url:
#                 print("⚠️ CAPTCHA detected. Skipping this page.")
#                 time.sleep(5)
#                 continue

#             # Wait for product cards
#             WebDriverWait(driver, 25).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "div.puis-card-container"))
#             )

#             product_cards = driver.find_elements(By.CSS_SELECTOR, "div.puis-card-container")

#             if not product_cards:
#                 print(f"⚠️ No products found on page {page}.")
#                 continue

#             for card in product_cards:
#                 product = {}
#                 try:
#                     product['name'] = card.find_element(By.CSS_SELECTOR, "h2 span").text
#                 except NoSuchElementException:
#                     product['name'] = 'N/A'

#                 try:
#                     product['price'] = card.find_element(By.CSS_SELECTOR, "span.a-price-whole").text.replace(',', '')
#                 except NoSuchElementException:
#                     product['price'] = 'N/A'

#                 try:
#                     rating = card.find_element(By.CSS_SELECTOR, "i.a-icon-star-small").get_attribute('aria-label')
#                     product['rating'] = rating.split(' ')[0]
#                 except (NoSuchElementException, AttributeError):
#                     product['rating'] = 'N/A'

#                 try:
#                     product['reviews'] = card.find_element(By.CSS_SELECTOR, "span.a-size-base.s-underline-text").text.replace(',', '')
#                 except NoSuchElementException:
#                     product['reviews'] = 'N/A'

#                 try:
#                     product['url'] = card.find_element(By.CSS_SELECTOR, "a.a-link-normal.s-no-outline").get_attribute('href')
#                 except NoSuchElementException:
#                     product['url'] = 'N/A'

#                 products.append(product)

#         except TimeoutException:
#             print(f"⏱️ Timeout on page {page}. Skipping...")

#         # Add random sleep to simulate real browsing and avoid blocking
#         time.sleep(random.uniform(3, 6))

#     driver.quit()
#     return products
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Sample list of user agents (you can expand this list)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
]

def create_driver():
    """Create a new Chrome driver instance with a random user agent"""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    user_agent = random.choice(USER_AGENTS)
    options.add_argument(f"user-agent={user_agent}")
    return webdriver.Chrome(options=options)

def get_amazon_mobile_data(pages=40):
    products = []
    base_url = "https://www.amazon.in/s?i=electronics&rh=n%3A1389432031&s=popularity-rank&fs=true&ref=lp_1389432031_sar"

    for page in range(1, pages + 1):
        print(f"\n🔄 Scraping page {page} with rotated User-Agent...")
        driver = create_driver()
        url = f"{base_url}&page={page}"
        driver.get(url)

        try:
            if "captcha" in driver.current_url:
                print("⚠️ CAPTCHA detected. Skipping this page.")
                driver.quit()
                continue

            WebDriverWait(driver, 25).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.puis-card-container"))
            )

            product_cards = driver.find_elements(By.CSS_SELECTOR, "div.puis-card-container")

            if not product_cards:
                print(f"⚠️ No products found on page {page}.")
                driver.quit()
                continue

            for card in product_cards:
                product = {}

                try:
                    product['name'] = card.find_element(By.CSS_SELECTOR, "h2 span").text
                except NoSuchElementException:
                    product['name'] = 'N/A'

                try:
                    product['price'] = card.find_element(By.CSS_SELECTOR, "span.a-price-whole").text.replace(',', '')
                except NoSuchElementException:
                    product['price'] = 'N/A'

                try:
                    rating = card.find_element(By.CSS_SELECTOR, "i.a-icon-star-small").get_attribute('aria-label')
                    product['rating'] = rating.split(' ')[0]
                except (NoSuchElementException, AttributeError):
                    product['rating'] = 'N/A'

                try:
                    product['reviews'] = card.find_element(By.CSS_SELECTOR, "span.a-size-base.s-underline-text").text.replace(',', '')
                except NoSuchElementException:
                    product['reviews'] = 'N/A'

                try:
                    product['url'] = card.find_element(By.CSS_SELECTOR, "a.a-link-normal.s-no-outline").get_attribute('href')
                except NoSuchElementException:
                    product['url'] = 'N/A'

                products.append(product)

        except TimeoutException:
            print(f"⏱️ Timeout on page {page}. Skipping...")

        driver.quit()
        time.sleep(random.uniform(3, 7))  # Add human-like delay

    return products





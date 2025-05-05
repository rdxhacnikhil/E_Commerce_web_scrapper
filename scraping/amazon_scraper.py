# # from bs4 import BeautifulSoup
# # import json
# # import os
# # import csv
# # from selenium import webdriver
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.common.by import By
# # from bs4 import BeautifulSoup
# # import time
# # import random
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.common.exceptions import TimeoutException, NoSuchElementException
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# import time
# import random

# USER_AGENTS = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
# ]

# def create_driver():
#     options = Options()
#     options.add_argument("--headless=new")
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     user_agent = random.choice(USER_AGENTS)
#     options.add_argument(f"user-agent={user_agent}")
#     return webdriver.Chrome(options=options)

# def get_amazon_mobile_data(pages=1):
#     products = []
#     base_url = "https://www.amazon.in/s?i=electronics&rh=n%3A1389432031&s=popularity-rank&fs=true&ref=lp_1389432031_sar"

#     for page in range(1, pages + 1):
#         print(f"\n🔄 Scraping page {page} with rotated User-Agent...")
#         driver = create_driver()
#         url = f"{base_url}&page={page}"
#         driver.get(url)

#         try:
#             if "captcha" in driver.current_url:
#                 print("⚠️ CAPTCHA detected. Skipping this page.")
#                 driver.quit()
#                 continue

#             WebDriverWait(driver, 25).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "div.puis-card-container"))
#             )

#             product_cards = driver.find_elements(By.CSS_SELECTOR, "div.puis-card-container")

#             if not product_cards:
#                 print(f"⚠️ No products found on page {page}.")
#                 driver.quit()
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

#                 try:
#                     product['image_url'] = card.find_element(By.CSS_SELECTOR, 'img.s-image').get_attribute('src')
#                 except NoSuchElementException:
#                     product['image_url'] = 'N/A'

#                 products.append(product)

#         except TimeoutException:
#             print(f"⏱️ Timeout on page {page}. Skipping...")

#         driver.quit()
#         time.sleep(random.uniform(3, 7))  # Human-like delay

#     return products

# # Sample list of user agents (you can expand this list)
# USER_AGENTS = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
# ]

# def create_driver():
#     """Create a new Chrome driver instance with a random user agent"""
#     options = Options()
#     options.add_argument("--headless=new")
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     user_agent = random.choice(USER_AGENTS)
#     options.add_argument(f"user-agent={user_agent}")
#     return webdriver.Chrome(options=options)

# def get_amazon_mobile_data(pages=1):
#     products = []
#     base_url = "https://www.amazon.in/s?i=electronics&rh=n%3A1389432031&s=popularity-rank&fs=true&ref=lp_1389432031_sar"

#     for page in range(1, pages + 1):
#         print(f"\n🔄 Scraping page {page} with rotated User-Agent...")
#         driver = create_driver()
#         url = f"{base_url}&page={page}"
#         driver.get(url)

#         try:
#             if "captcha" in driver.current_url:
#                 print("⚠️ CAPTCHA detected. Skipping this page.")
#                 driver.quit()
#                 continue

#             WebDriverWait(driver, 25).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "div.puis-card-container"))
#             )

#             # product_cards = driver.find_elements(By.CSS_SELECTOR, "div.puis-card-container")
#             product_cards = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot > div[data-asin]")

#             if not product_cards:
#                 print(f"⚠️ No products found on page {page}.")
#                 driver.quit()
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
#                 try:
#                     product['image_url'] = card.find_element(By.CSS_SELECTOR, 'img.s-image').get_attribute('src')
#                 except NoSuchElementException:
#                     product['image_url'] = 'N/A'

#         except TimeoutException:
#             print(f"⏱️ Timeout on page {page}. Skipping...")

#         driver.quit()
#         time.sleep(random.uniform(3, 7))  # Add human-like delay

#     return products
import time
import random
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
]

def create_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    user_agent = random.choice(USER_AGENTS)
    options.add_argument(f"user-agent={user_agent}")
    return webdriver.Chrome(options=options)

def get_amazon_mobile_data(pages=1):
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
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot > div[data-asin]"))
            )

            product_cards = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot > div[data-asin]")

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

                try:
                    product['image_url'] = card.find_element(By.CSS_SELECTOR, 'img.s-image').get_attribute('src')
                except NoSuchElementException:
                    product['image_url'] = 'N/A'

                products.append(product)

        except TimeoutException:
            print(f"⏱️ Timeout on page {page}. Skipping...")

        driver.quit()
        time.sleep(random.uniform(3, 7))  # Human-like delay

    return products

def save_to_csv(data, filename="data/amazon_mobiles.csv"):
    if not data:
        print("⚠️ No data to save.")
        return

    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ Saved {len(data)} records to {filename}")

if __name__ == "__main__":
    scraped_data = get_amazon_mobile_data(pages=1)
    save_to_csv(scraped_data)







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
#     options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
#     return webdriver.Chrome(options=options)

# def get_amazon_laptop_data(pages=1):
#     base_url = "https://www.amazon.in/s?i=computers&rh=n%3A1375424031&s=popularity-rank&fs=true&ref=lp_1375424031_sar"
#     products = []

#     for page in range(1, pages + 1):
#         print(f"\n🔄 Scraping Amazon Laptops Page {page}...")
#         driver = create_driver()
#         url = f"{base_url}&page={page}"
#         driver.get(url)

#         try:
#             if "captcha" in driver.current_url:
#                 print("⚠️ CAPTCHA detected. Skipping page.")
#                 driver.quit()
#                 continue

#             WebDriverWait(driver, 25).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "div.puis-card-container"))
#             )

#             product_cards = driver.find_elements(By.CSS_SELECTOR, "div.puis-card-container")

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
#             print("⏱️ Timeout. Skipping page.")

#         driver.quit()
#         time.sleep(random.uniform(3, 6))

#     return products
# # 
import time
import random
import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# User-Agent List for Randomization
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
    options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def setup_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def get_amazon_laptop_data(pages=1):
    base_url = "https://www.amazon.in/s?i=computers&rh=n%3A1375424031&s=popularity-rank&fs=true&ref=lp_1375424031_sar"
    all_data = []

    for page in range(1, pages + 1):
        print(f"\n🔄 Scraping Amazon Laptops Page {page}...")
        driver = create_driver()
        url = f"{base_url}&page={page}"
        driver.get(url)

        try:
            if "captcha" in driver.current_url:
                print("⚠️ CAPTCHA detected. Skipping page.")
                driver.quit()
                continue

            WebDriverWait(driver, 25).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.puis-card-container"))
            )

            product_cards = driver.find_elements(By.CSS_SELECTOR, "div.puis-card-container")

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
                    product['image_url'] = card.find_element(By.CSS_SELECTOR, "img.s-image").get_attribute("src")
                except NoSuchElementException:
                    product['image_url'] = 'N/A'

                all_data.append(product)

        except TimeoutException:
            print("⏱️ Timeout. Skipping page.")

        driver.quit()
        time.sleep(random.uniform(3, 6))

    return all_data

# def save_data(data, filename="amazon_laptops.csv"):
#     if not data:
#         print("⚠️ No data to save.")
#         return

#     os.makedirs("data", exist_ok=True)
#     filepath = os.path.join("data", filename)

#     with open(filepath, "w", newline="", encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=data[0].keys())
#         writer.writeheader()
#         writer.writerows(data)

#     print(f"✅ Data saved to {filepath}")
def save_data(data, filename="amazon_laptops.csv"):
    if not data:
        print("⚠️ No data to save.")
        return

    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ Data saved to {filename}")



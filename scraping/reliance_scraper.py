# # reliance_scraper.py

# import time
# import csv
# import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def setup_driver():
#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--window-size=1920,1080")
#     driver = webdriver.Chrome(options=options)
#     return driver

# def scrape_reliance_best_selling(driver, pages=12):
#     base_url = "https://www.reliancedigital.in/collection/best-selling-phones-250422?page_no={}&page_size=12&page_type=number"
#     all_products = []

#     for page in range(1, pages + 1):
#         print(f"[Reliance] Scraping Page {page}...")
#         driver.get(base_url.format(page))
#         time.sleep(4)

#         product_cards = driver.find_elements(By.CSS_SELECTOR, "div.card-info-container")

#         for card in product_cards:
#             try:
#                 title = card.find_element(By.CSS_SELECTOR, ".product-card-title").text.strip()
#                 price = card.find_element(By.CSS_SELECTOR, ".price-container .price").text.strip()
#                 mrp = card.find_element(By.CSS_SELECTOR, ".mrp-amount").text.strip()
#                 discount = card.find_element(By.CSS_SELECTOR, ".discount").text.strip()

#                 all_products.append({
#                     "title": title,
#                     "price": price,
#                     "mrp": mrp,
#                     "discount": discount
#                 })
#             except Exception as e:
#                 print(f"Error scraping a product: {e}")

#     return all_products

# def save_data(data, csv_filename, json_filename):
#     # Save to CSV
#     with open(csv_filename, "w", newline='', encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=["title", "price", "mrp", "discount"])
#         writer.writeheader()
#         writer.writerows(data)

#     # Save to JSON
#     with open(json_filename, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)

# if __name__ == "__main__":
#     driver = setup_driver()
#     try:
#         products = scrape_reliance_best_selling(driver, pages=12)
#         save_data(products, "data/reliance_mobiles.csv", "data/reliance_mobiles.json")
#         print(f"\n✅ Scraped and saved {len(products)} products from Reliance Digital.")
#     finally:
#         driver.quit()


import time
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    return driver
def scrape_reliance_5g_smartphones(driver, pages=30):
    base_url = "https://www.reliancedigital.in/collection/5g-smartphones-250422?page_no={}&page_size=12&page_type=number"
    all_products = []

    for page in range(1, pages + 1):
        print(f"[Reliance 5G] Scraping page {page}...")
        driver.get(base_url.format(page))
        time.sleep(3)  # Let the page load fully

        product_cards = driver.find_elements(By.CSS_SELECTOR, "div.card-info-container")

        for card in product_cards:
            try:
                title = card.find_element(By.CSS_SELECTOR, ".product-card-title").text.strip()
                price = card.find_element(By.CSS_SELECTOR, ".price").text.strip()

                try:
                    mrp = card.find_element(By.CSS_SELECTOR, ".mrp-amount").text.strip()
                except:
                    mrp = None

                try:
                    availability = card.find_element(By.CSS_SELECTOR, ".out-of-stock").text.strip()
                except:
                    availability = "In Stock"

                all_products.append({
                    "title": title,
                    "price": price,
                    "mrp": mrp,
                    "availability": availability
                })
            except Exception as e:
                print(f"Error scraping product: {e}")

    return all_products

# def scrape_reliance_best_selling(driver, pages=12):
#     base_url = "https://www.reliancedigital.in/collection/best-selling-phones-250422?page_no={}&page_size=12&page_type=number"
#     all_products = []

#     for page in range(1, pages + 1):
#         print(f"[Reliance] Scraping Page {page}...")
#         driver.get(base_url.format(page))
#         time.sleep(4)

#         product_cards = driver.find_elements(By.CSS_SELECTOR, "div.card-info-container")

#         for card in product_cards:
#             try:
#                 title = card.find_element(By.CSS_SELECTOR, ".product-card-title").text.strip()
#                 price = card.find_element(By.CSS_SELECTOR, ".price-container .price").text.strip()
#                 mrp = card.find_element(By.CSS_SELECTOR, ".mrp-amount").text.strip()
#                 discount = card.find_element(By.CSS_SELECTOR, ".discount").text.strip()

#                 all_products.append({
#                     "title": title,
#                     "price": price,
#                     "mrp": mrp,
#                     "discount": discount
#                 })
#             except Exception as e:
#                 print(f"Error scraping a product: {e}")

#     return all_products
def scrape_reliance_best_selling(driver, pages=30):
    base_url = "https://www.reliancedigital.in/collection/best-selling-phones-250422?page_no={}&page_size=12&page_type=number"
    all_products = []

    for page in range(1, pages + 1):
        print(f"[Reliance] Scraping Page {page}...")
        driver.get(base_url.format(page))
        time.sleep(4)

        product_cards = driver.find_elements(By.CSS_SELECTOR, "div.card-info-container")

        for card in product_cards:
            try:
                title = card.find_element(By.CSS_SELECTOR, ".product-card-title").text.strip()
                price = card.find_element(By.CSS_SELECTOR, ".price-container .price").text.strip()
                mrp = card.find_element(By.CSS_SELECTOR, ".mrp-amount").text.strip()
                discount = card.find_element(By.CSS_SELECTOR, ".discount").text.strip()

                # Extract URL and image
                link_element = card.find_element(By.XPATH, ".//a[contains(@class, 'product-card')]")
                product_url = link_element.get_attribute("href")

                image_element = card.find_element(By.CSS_SELECTOR, "img")
                image_url = image_element.get_attribute("src")

                all_products.append({
                    "title": title,
                    "price": price,
                    "mrp": mrp,
                    "discount": discount,
                    "url": product_url,
                    "image_url": image_url
                })
            except Exception as e:
                print(f"Error scraping a product: {e}")

    return all_products

# def save_data(data, csv_filename, json_filename):
#     # Save to CSV
#     with open(csv_filename, "w", newline='', encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=["title", "price", "mrp", "discount"])
#         writer.writeheader()
#         writer.writerows(data)

#     # Save to JSON
#     with open(json_filename, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)
def save_data(data, csv_filename, json_filename):
    # Save to CSV
    keys = ["title", "price", "mrp", "discount", "url", "image_url"]
    with open(csv_filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    # Save to JSON
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
 

if __name__ == "__main__":
    driver = setup_driver()
    try:
        products = scrape_reliance_best_selling(driver, pages=30)
        save_data(products, "data/reliance_mobiles.csv", "data/reliance_mobiles.json")
        print(f"\n✅ Scraped and saved {len(products)} products from Reliance Digital.")
    finally:
        driver.quit()

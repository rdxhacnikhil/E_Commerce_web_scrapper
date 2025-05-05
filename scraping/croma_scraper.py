# # croma_scraper.py

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
# import csv

# def init_driver():
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     return webdriver.Chrome(options=options)

# def scrape_croma_products(pages=3):
#     base_url = "https://www.croma.com/phones-wearables/c/1?page="
#     driver = init_driver()
#     results = []

#     for page in range(1, pages + 1):
#         print(f"[Croma] Scraping Page {page}...")
#         driver.get(base_url + str(page))
#         time.sleep(3)

#         products = driver.find_elements(By.CLASS_NAME, "cp-product")

#         for product in products:
#             try:
#                 title = product.find_element(By.CLASS_NAME, "product-title").text.strip()
#                 link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
#                 image = product.find_element(By.TAG_NAME, "img").get_attribute("src")
#                 new_price = product.find_element(By.CSS_SELECTOR, "[data-testid='new-price']").text.strip()
#                 old_price = product.find_element(By.CSS_SELECTOR, "[data-testid='old-price']").text.strip() if product.find_elements(By.CSS_SELECTOR, "[data-testid='old-price']") else ""
#                 discount = product.find_element(By.CLASS_NAME, "discount-newsearch-plp").text.strip() if product.find_elements(By.CLASS_NAME, "discount-newsearch-plp") else ""
#                 rating = product.find_element(By.CLASS_NAME, "rating-text").text.strip() if product.find_elements(By.CLASS_NAME, "rating-text") else ""
#                 reviews = product.find_element(By.XPATH, ".//span[contains(text(),'(')]").text.strip("()") if product.find_elements(By.XPATH, ".//span[contains(text(),'(')]") else ""

#                 results.append({
#                     "Title": title,
#                     "Link": link,
#                     "Image": image,
#                     "New Price": new_price,
#                     "Old Price": old_price,
#                     "Discount": discount,
#                     "Rating": rating,
#                     "Reviews": reviews
#                 })
#             except Exception as e:
#                 print("Error scraping product:", e)

#     driver.quit()
#     return results

# def save_to_csv(data, filename="croma_products.csv"):
#     if not data:
#         print("No data to save.")
#         return
#     keys = data[0].keys()
#     with open(filename, "w", newline="", encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=keys)
#         writer.writeheader()
#         writer.writerows(data)
#     print(f"[Croma] Saved {len(data)} products to {filename}")

# def run_croma_scraper():
#     data = scrape_croma_products(pages=5)
#     save_to_csv(data)
# 
# croma_scraper.py (updated)
# croma_scraper.py
# croma_scraper.py


# def setup_driver():
#     options = Options()
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_argument("--start-maximized")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_argument("--disable-infobars")
#     options.add_argument("--disable-notifications")
#     driver = webdriver.Chrome(options=options)
#     return driver

# def scrape_croma_products(driver):
#     driver.get("https://www.croma.com/phones-wearables/c/1")
#     products = []
    
#     print("[Croma] Initial page load...")
#     time.sleep(3)  # Initial load time

#     # Scroll and load mechanism
#     previous_count = 0
#     max_retries = 5
#     retries = 0

#     while retries < max_retries:
#         # Scroll to bottom in increments
#         for _ in range(3):
#             driver.execute_script("window.scrollBy(0, 800)")
#             time.sleep(1)
        
#         try:
#             # Click View More using action chain
#             view_more = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-viewmore"))
#             )
#             ActionChains(driver).move_to_element(view_more).click().perform()
#             print("[Croma] Clicked View More")
#             retries = 0
#             time.sleep(2)
#         except Exception as e:
#             print(f"[Croma] View More error: {str(e)[:60]}")
#             retries += 1

#         # Check product load progress
#         current_products = driver.find_elements(By.CSS_SELECTOR, "div.cp-product.typ-plp.plp-srp-typ")
#         print(f"[Croma] Current products: {len(current_products)}")

        
#         if len(current_products) == previous_count:
#             retries += 1
#         previous_count = len(current_products)

#     # Final extraction with explicit waits
#     product_cards = WebDriverWait(driver, 15).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cp-product.typ-plp.plp-srp-typ"))
#     )
#     print(f"[Croma] Found {len(product_cards)} products for scraping")

#     for card in product_cards:
#         try:
#             # Scroll to card before extraction
#             driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
#             time.sleep(0.5)
            
#             product = {
#                 'name': card.find_element(By.CSS_SELECTOR, "h3.product-title.plp-prod-title").text.strip(),
#                 'price': WebDriverWait(card, 5).until(
#                     EC.visibility_of_element_located((By.CSS_SELECTOR, "span.amount.plp-srp-new-amount"))
#                 ).text.replace('₹', '').replace(',', '').strip(),
#                 'url': card.find_element(By.CSS_SELECTOR, "a[href^='/']").get_attribute("href"),
#                 'rating': (card.find_element(By.CSS_SELECTOR, "span.rating-text").text.split()[0] 
#                           if card.find_elements(By.CSS_SELECTOR, "span.rating-text") 
#                           else 'N/A')
#             }
#             products.append(product)
#         except Exception as e:
#             print(f"[Croma] Partial extraction: {str(e)[:50]}")

#     print(f"[Croma] Successfully scraped {len(products)}/{len(product_cards)} products")
#     return products
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
def setup_driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    return driver

def save_data(products, filename="data/croma_limited.csv"):
    if not products:
        print("[Croma] No data to save.")
        return
    keys = products[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(products)
    print(f"[Croma] Saved {len(products)} products to {filename}")

def scrape_croma_products(driver, max_products=1000):
    driver.get("https://www.croma.com/phones-wearables/c/1")
    products = []

    print("[Croma] Initial page load...")
    time.sleep(3)

    previous_count = 0
    max_retries = 5
    retries = 0

    while retries < max_retries:
        for _ in range(3):
            driver.execute_script("window.scrollBy(0, 800)")
            time.sleep(1)

        try:
            view_more = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-viewmore"))
            )
            ActionChains(driver).move_to_element(view_more).click().perform()
            print("[Croma] Clicked View More")
            retries = 0
            time.sleep(2)
        except Exception as e:
            print(f"[Croma] View More error: {str(e)[:60]}")
            retries += 1

        current_products = driver.find_elements(By.CSS_SELECTOR, "div.cp-product.typ-plp.plp-srp-typ")
        print(f"[Croma] Current products: {len(current_products)}")

        if len(current_products) >= max_products:
            print(f"[Croma] Reached max limit of {max_products} products.")
            break

        if len(current_products) == previous_count:
            retries += 1
        previous_count = len(current_products)

    # Final scraping of the visible product cards
    product_cards = driver.find_elements(By.CSS_SELECTOR, "div.cp-product.typ-plp.plp-srp-typ")[:max_products]
    print(f"[Croma] Scraping {len(product_cards)} products...")

    for card in product_cards:
        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
            time.sleep(0.5)

            product = {
                'name': card.find_element(By.CSS_SELECTOR, "h3.product-title.plp-prod-title").text.strip(),
                'price': WebDriverWait(card, 5).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "span.amount.plp-srp-new-amount"))
                ).text.replace('₹', '').replace(',', '').strip(),
                'url': card.find_element(By.CSS_SELECTOR, "a[href^='/']").get_attribute("href"),
                'rating': (
                    card.find_element(By.CSS_SELECTOR, "span.rating-text").text.split()[0]
                    if card.find_elements(By.CSS_SELECTOR, "span.rating-text") else 'N/A'
                ),
                'image': card.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
            }
            products.append(product)

            if len(products) >= max_products:
                print(f"[Croma] Limit reached while extracting: {len(products)}")
                break

        except Exception as e:
            print(f"[Croma] Partial extraction error: {str(e)[:50]}")

    save_data(products)
    return products
if __name__ == "__main__":
    driver = setup_driver()
    try:
        scrape_croma_products(driver, max_products=1000)  # Adjust max_products if needed
    finally:
        driver.quit()



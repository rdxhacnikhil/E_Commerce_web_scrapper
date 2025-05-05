# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager
# # from bs4 import BeautifulSoup
# # import time
# # import pandas as pd
# # import os

# # # Set up Selenium WebDriver
# # options = webdriver.ChromeOptions()
# # options.add_argument("--headless")  # Run in headless mode
# # options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # URL to scrape
# # url = "https://www.croma.com/searchB?q=laptop%3Arelevance&text=laptop"
# # driver.get(url)

# # # Wait for JavaScript to load content
# # time.sleep(3)  # Adjust based on page load time

# # # Parse page source with BeautifulSoup
# # soup = BeautifulSoup(driver.page_source, "html.parser")

# # # Find all product containers
# # products = soup.find_all("div", class_="cp-product typ-plp plp-srp-typ")

# # # List to store scraped data
# # laptop_data = []

# # for product in products:
# #     try:
# #         # Extract title
# #         title_elem = product.select_one("h3.product-title a")
# #         title = title_elem.text.strip() if title_elem else "N/A"

# #         # Extract product URL
# #         product_url = title_elem["href"] if title_elem else "N/A"

# #         # Extract image URL
# #         image_elem = product.select_one("div.product-img img")
# #         image_url = image_elem["data-src"] if image_elem else "N/A"

# #         # Extract current price
# #         current_price_elem = product.select_one("span.amount.plp-srp-new-amount")
# #         current_price = current_price_elem.text.strip() if current_price_elem else "N/A"

# #         # Extract original price
# #         original_price_elem = product.select_one("span.amount#old-price")
# #         original_price = original_price_elem.text.strip() if original_price_elem else "N/A"

# #         # Extract discount
# #         discount_elem = product.select_one("span.discount.discount-newsearch-plp")
# #         discount = discount_elem.text.strip() if discount_elem else "N/A"

# #         # Extract rating
# #         rating_elem = product.select_one("span.rating-text")
# #         rating = rating_elem.text.strip().split()[0] if rating_elem else "N/A"

# #         # Extract number of reviews
# #         reviews_elem = product.select_one("span.rating-text-icon span span")
# #         reviews = reviews_elem.text.strip() if reviews_elem else "N/A"

# #         # Extract offer tag
# #         offer_elem = product.select_one("span.tagsForPlp")
# #         offer = offer_elem.text.strip() if offer_elem else "N/A"

# #         # Extract delivery info
# #         delivery_elem = product.select_one("span.delivery-text-msg span")
# #         delivery = delivery_elem.text.strip() if delivery_elem else "N/A"

# #         # Store data
# #         laptop_data.append({
# #             "title": title,
# #             "product_url": product_url,
# #             "image_url": image_url,
# #             "current_price": current_price,
# #             "original_price": original_price,
# #             "discount": discount,
# #             "rating": rating,
# #             "reviews": reviews,
# #             "offer": offer,
# #             "delivery": delivery
# #         })

# #     except Exception as e:
# #         print(f"Error processing product: {e}")
# #         continue

# # # Close the driver
# # driver.quit()

# # # Define output path (data folder one level up from scripts)
# # output_dir = os.path.join(os.path.dirname(__file__), "..", "data")
# # os.makedirs(output_dir, exist_ok=True)  # Create data folder if it doesn't exist
# # output_file = os.path.join(output_dir, "croma_laptops.csv")

# # # Save to CSV
# # df = pd.DataFrame(laptop_data)
# # df.to_csv(output_file, index=False)
# # print(f"Data saved to {output_file}")
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
# import os

# # Set up Selenium WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run in headless mode
# options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # URL to scrape
# url = "https://www.croma.com/searchB?q=laptop%3Arelevance&text=laptop"
# driver.get(url)
# laptop_data = []
# # Wait for JavaScript to load content
# time.sleep(3)  # Adjust based on page load time

# # Parse page source with BeautifulSoup
# soup = BeautifulSoup(driver.page_source, "html.parser")

# # Find all product containers
# products = soup.find_all("div", class_="cp-product typ-plp plp-srp-typ")

# # List to store scraped data
# laptop_data = []

# for product in products:
#     try:
#         # Extract title
#         title_elem = product.select_one("h3.product-title a")
#         title = title_elem.text.strip() if title_elem else "N/A"

#         # Extract product URL
#         product_url = title_elem["href"] if title_elem else "N/A"

#         # Extract image URL
#         image_elem = product.select_one("div.product-img img")
#         image_url = image_elem["data-src"] if image_elem else "N/A"

#         # Extract current price
#         current_price_elem = product.select_one("span.amount.plp-srp-new-amount")
#         current_price = current_price_elem.text.strip() if current_price_elem else "N/A"

#         # Extract original price
#         original_price_elem = product.select_one("span.amount#old-price")
#         original_price = original_price_elem.text.strip() if original_price_elem else "N/A"

#         # Extract discount
#         discount_elem = product.select_one("span.discount.discount-newsearch-plp")
#         discount = discount_elem.text.strip() if discount_elem else "N/A"

#         # Extract rating
#         rating_elem = product.select_one("span.rating-text")
#         rating = rating_elem.text.strip().split()[0] if rating_elem else "N/A"

#         # Extract number of reviews
#         reviews_elem = product.select_one("span.rating-text-icon span span")
#         reviews = reviews_elem.text.strip() if reviews_elem else "N/A"

#         # Extract offer tag
#         offer_elem = product.select_one("span.tagsForPlp")
#         offer = offer_elem.text.strip() if offer_elem else "N/A"

#         # Extract delivery info
#         delivery_elem = product.select_one("span.delivery-text-msg span")
#         delivery = delivery_elem.text.strip() if delivery_elem else "N/A"

#         # Store data
#         laptop_data.append({
#             "title": title,
#             "product_url": product_url,
#             "image_url": image_url,
#             "current_price": current_price,
#             "original_price": original_price,
#             "discount": discount,
#             "rating": rating,
#             "reviews": reviews,
#             "offer": offer,
#             "delivery": delivery
#         })

#     except Exception as e:
#         print(f"Error processing product: {e}")
#         continue

# # Close the driver
# driver.quit()

# # Define output path (data folder one level up from scripts)
# output_dir = os.path.join(os.path.dirname(__file__), "..", "data")
# os.makedirs(output_dir, exist_ok=True)  # Create data folder if it doesn't exist
# output_file = os.path.join(output_dir, "croma_laptops.csv")

# # Save to CSV
# df = pd.DataFrame(laptop_data)
# df.to_csv(output_file, index=False)
# print(f"Data saved to {output_file}")
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
# import os

# # Set up Selenium WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run in headless mode
# options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # URL to scrape
# url = "https://www.croma.com/searchB?q=laptop%3Arelevance&text=laptop"
# driver.get(url)

# # List to store scraped data
# laptop_data = []

# # Loop to scrape multiple pages (assuming each page contains 30 products)
# page_number = 1
# while len(laptop_data) < 1000:
#     # Wait for JavaScript to load content
#     time.sleep(3)  # Adjust based on page load time
    
#     # Parse page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, "html.parser")

#     # Find all product containers
#     products = soup.find_all("div", class_="cp-product typ-plp plp-srp-typ")

#     # Scrape product details
#     for product in products:
#         try:
#             # Extract title
#             title_elem = product.select_one("h3.product-title a")
#             title = title_elem.text.strip() if title_elem else "N/A"

#             # Extract product URL
#             product_url = title_elem["href"] if title_elem else "N/A"

#             # Extract image URL
#             image_elem = product.select_one("div.product-img img")
#             image_url = image_elem["data-src"] if image_elem else "N/A"

#             # Extract current price
#             current_price_elem = product.select_one("span.amount.plp-srp-new-amount")
#             current_price = current_price_elem.text.strip() if current_price_elem else "N/A"

#             # Extract original price
#             original_price_elem = product.select_one("span.amount#old-price")
#             original_price = original_price_elem.text.strip() if original_price_elem else "N/A"

#             # Extract discount
#             discount_elem = product.select_one("span.discount.discount-newsearch-plp")
#             discount = discount_elem.text.strip() if discount_elem else "N/A"

#             # Extract rating
#             rating_elem = product.select_one("span.rating-text")
#             rating = rating_elem.text.strip().split()[0] if rating_elem else "N/A"

#             # Extract number of reviews
#             reviews_elem = product.select_one("span.rating-text-icon span span")
#             reviews = reviews_elem.text.strip() if reviews_elem else "N/A"

#             # Extract offer tag
#             offer_elem = product.select_one("span.tagsForPlp")
#             offer = offer_elem.text.strip() if offer_elem else "N/A"

#             # Extract delivery info
#             delivery_elem = product.select_one("span.delivery-text-msg span")
#             delivery = delivery_elem.text.strip() if delivery_elem else "N/A"

#             # Store data
#             laptop_data.append({
#                 "title": title,
#                 "product_url": product_url,
#                 "image_url": image_url,
#                 "current_price": current_price,
#                 "original_price": original_price,
#                 "discount": discount,
#                 "rating": rating,
#                 "reviews": reviews,
#                 "offer": offer,
#                 "delivery": delivery
#             })
#         except Exception as e:
#             print(f"Error processing product: {e}")
#             continue

#     # Check if 1000 products are scraped
#     if len(laptop_data) >= 1000:
#         break

#     # Go to next page
#     try:
#         next_button = driver.find_element_by_xpath('//a[@aria-label="Next"]')
#         next_button.click()
#         page_number += 1
#         print(f"Scraping page {page_number}...")
#         time.sleep(3)
#     except Exception as e:
#         print("No more pages or error navigating to next page.")
#         break

# # Close the driver
# driver.quit()

# # Define output path (data folder one level up from scripts)
# output_dir = os.path.join(os.path.dirname(__file__), "..", "data")
# os.makedirs(output_dir, exist_ok=True)  # Create data folder if it doesn't exist
# output_file = os.path.join(output_dir, "croma_laptops.csv")

# # Save to CSV
# df = pd.DataFrame(laptop_data)
# df.to_csv(output_file, index=False)
# print(f"Data saved to {output_file}")
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
# import os

# # Set up Selenium WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # URL to scrape
# url = "https://www.croma.com/searchB?q=laptop%3Arelevance&text=laptop"
# driver.get(url)
# time.sleep(3)

# # Data container
# laptop_data = []

# # Scraping loop with pagination
# while len(laptop_data) < 1000:
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     products = soup.find_all("div", class_="cp-product typ-plp plp-srp-typ")

#     if not products:
#         print("No products found on the page. Breaking.")
#         break

#     for product in products:
#         try:
#             title_elem = product.select_one("h3.product-title a")
#             title = title_elem.text.strip() if title_elem else "N/A"
#             product_url = title_elem["href"] if title_elem else "N/A"
#             image_elem = product.select_one("div.product-img img")
#             image_url = image_elem["data-src"] if image_elem else "N/A"
#             current_price_elem = product.select_one("span.amount.plp-srp-new-amount")
#             current_price = current_price_elem.text.strip() if current_price_elem else "N/A"
#             original_price_elem = product.select_one("span.amount#old-price")
#             original_price = original_price_elem.text.strip() if original_price_elem else "N/A"
#             discount_elem = product.select_one("span.discount.discount-newsearch-plp")
#             discount = discount_elem.text.strip() if discount_elem else "N/A"
#             rating_elem = product.select_one("span.rating-text")
#             rating = rating_elem.text.strip().split()[0] if rating_elem else "N/A"
#             reviews_elem = product.select_one("span.rating-text-icon span span")
#             reviews = reviews_elem.text.strip() if reviews_elem else "N/A"
#             offer_elem = product.select_one("span.tagsForPlp")
#             offer = offer_elem.text.strip() if offer_elem else "N/A"
#             delivery_elem = product.select_one("span.delivery-text-msg span")
#             delivery = delivery_elem.text.strip() if delivery_elem else "N/A"

#             laptop_data.append({
#                 "title": title,
#                 "product_url": product_url,
#                 "image_url": image_url,
#                 "current_price": current_price,
#                 "original_price": original_price,
#                 "discount": discount,
#                 "rating": rating,
#                 "reviews": reviews,
#                 "offer": offer,
#                 "delivery": delivery
#             })

#             # Stop if we've collected enough data
#             if len(laptop_data) >= 1000:
#                 break

#         except Exception as e:
#             print(f"Error processing product: {e}")
#             continue

#     if len(laptop_data) >= 1000:
#         break

#     # Try going to the next page
#     try:
#         next_button = driver.find_element(By.CSS_SELECTOR, "a.pagination__next")
#         if "disabled" in next_button.get_attribute("class"):
#             print("No more pages.")
#             break
#         else:
#             driver.execute_script("arguments[0].click();", next_button)
#             time.sleep(3)
#     except Exception as e:
#         print("No more pages or error navigating to next page.")
#         break

# # Close the driver
# driver.quit()

# # Save to CSV
# output_dir = os.path.join(os.path.dirname(__file__), "..", "data")
# os.makedirs(output_dir, exist_ok=True)
# output_file = os.path.join(output_dir, "croma_laptops.csv")

# df = pd.DataFrame(laptop_data)
# df.to_csv(output_file, index=False)
# print(f"Scraped {len(laptop_data)} products.")
# print(f"Data saved to {output_file}")
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
# import os

# # Set up Selenium WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # URL to scrape
# url = "https://www.croma.com/searchB?q=laptop%3Arelevance&text=laptop"
# driver.get(url)
# time.sleep(3)

# laptop_data = []
# seen_products = set()  # Store unique titles or product URLs

# ...

# unique_key = product_url.strip()

# if unique_key not in seen_products:
#     seen_products.add(unique_key)
#     laptop_data.append(entry)

# # Scraping loop
# while True:
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     products = soup.find_all("div", class_="cp-product typ-plp plp-srp-typ")

#     for product in products:
#         try:
#             title_elem = product.select_one("h3.product-title a")
#             title = title_elem.text.strip() if title_elem else "N/A"
#             product_url = title_elem["href"] if title_elem else "N/A"
#             image_elem = product.select_one("div.product-img img")
#             image_url = image_elem["data-src"] if image_elem else "N/A"
#             current_price_elem = product.select_one("span.amount.plp-srp-new-amount")
#             current_price = current_price_elem.text.strip() if current_price_elem else "N/A"
#             original_price_elem = product.select_one("span.amount#old-price")
#             original_price = original_price_elem.text.strip() if original_price_elem else "N/A"
#             discount_elem = product.select_one("span.discount.discount-newsearch-plp")
#             discount = discount_elem.text.strip() if discount_elem else "N/A"
#             rating_elem = product.select_one("span.rating-text")
#             rating = rating_elem.text.strip().split()[0] if rating_elem else "N/A"
#             reviews_elem = product.select_one("span.rating-text-icon span span")
#             reviews = reviews_elem.text.strip() if reviews_elem else "N/A"
#             offer_elem = product.select_one("span.tagsForPlp")
#             offer = offer_elem.text.strip() if offer_elem else "N/A"
#             delivery_elem = product.select_one("span.delivery-text-msg span")
#             delivery = delivery_elem.text.strip() if delivery_elem else "N/A"

#             entry = {
#                 "title": title,
#                 "product_url": product_url,
#                 "image_url": image_url,
#                 "current_price": current_price,
#                 "original_price": original_price,
#                 "discount": discount,
#                 "rating": rating,
#                 "reviews": reviews,
#                 "offer": offer,
#                 "delivery": delivery
#             }

#             if entry not in laptop_data:  # Avoid duplicates
#                 laptop_data.append(entry)

#             if len(laptop_data) >= 1000:
#                 break

#         except Exception as e:
#             print(f"Error processing product: {e}")
#             continue

#     if len(laptop_data) >= 1000:
#         print("Reached 1000 products.")
#         break

#     # Try clicking "View More"
#     try:
#         view_more_btn = driver.find_element(By.CLASS_NAME, "btn-viewmore")
#         if view_more_btn.is_displayed():
#             driver.execute_script("arguments[0].click();", view_more_btn)
#             time.sleep(3)
#         else:
#             print("No more View More button visible.")
#             break
#     except (NoSuchElementException, ElementClickInterceptedException):
#         print("No more 'View More' button or error clicking it.")
#         break

# # Close browser
# driver.quit()

# # Save data
# output_dir = os.path.join(os.path.dirname(__file__), "..", "data")
# os.makedirs(output_dir, exist_ok=True)
# output_file = os.path.join(output_dir, "croma_laptops.csv")

# df = pd.DataFrame(laptop_data)
# df.to_csv(output_file, index=False)
# print(f"Scraped {len(laptop_data)} laptop products.")
# print(f"Data saved to {output_file}")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd
import os
import json
# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL to scrape
url = "https://www.croma.com/searchB?q=laptop%3Arelevance&text=laptop"
driver.get(url)
time.sleep(3)

laptop_data = []
seen_products = set()  # Store unique product URLs to avoid duplicates

# Scraping loop
while True:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    products = soup.find_all("div", class_="cp-product typ-plp plp-srp-typ")

    for product in products:
        try:
            title_elem = product.select_one("h3.product-title a")
            title = title_elem.text.strip() if title_elem else "N/A"
            product_url = title_elem["href"] if title_elem else "N/A"

            # Use product URL as unique key
            unique_key = product_url.strip()
            if unique_key in seen_products:
                continue
            seen_products.add(unique_key)

            image_elem = product.select_one("div.product-img img")
            image_url = image_elem["data-src"] if image_elem else "N/A"
            current_price_elem = product.select_one("span.amount.plp-srp-new-amount")
            current_price = current_price_elem.text.strip() if current_price_elem else "N/A"
            original_price_elem = product.select_one("span.amount#old-price")
            original_price = original_price_elem.text.strip() if original_price_elem else "N/A"
            discount_elem = product.select_one("span.discount.discount-newsearch-plp")
            discount = discount_elem.text.strip() if discount_elem else "N/A"
            rating_elem = product.select_one("span.rating-text")
            rating = rating_elem.text.strip().split()[0] if rating_elem else "N/A"
            reviews_elem = product.select_one("span.rating-text-icon span span")
            reviews = reviews_elem.text.strip() if reviews_elem else "N/A"
            offer_elem = product.select_one("span.tagsForPlp")
            offer = offer_elem.text.strip() if offer_elem else "N/A"
            delivery_elem = product.select_one("span.delivery-text-msg span")
            delivery = delivery_elem.text.strip() if delivery_elem else "N/A"

            entry = {
                "title": title,
                "product_url": product_url,
                "image_url": image_url,
                "current_price": current_price,
                "original_price": original_price,
                "discount": discount,
                "rating": rating,
                "reviews": reviews,
                "offer": offer,
                "delivery": delivery
            }

            laptop_data.append(entry)

            if len(laptop_data) >= 1000:
                break

        except Exception as e:
            print(f"Error processing product: {e}")
            continue

    if len(laptop_data) >= 1000:
        print("Reached 1000 products.")
        break

    # Try clicking "View More"
    try:
        view_more_btn = driver.find_element(By.CLASS_NAME, "btn-viewmore")
        if view_more_btn.is_displayed():
            driver.execute_script("arguments[0].click();", view_more_btn)
            time.sleep(3)
        else:
            print("No more View More button visible.")
            break
    except (NoSuchElementException, ElementClickInterceptedException):
        print("No more 'View More' button or error clicking it.")
        break

# Close browser
driver.quit()

# Save data
# output_dir = os.path.join(os.path.dirname(__file__), "..", "data")
# os.makedirs(output_dir, exist_ok=True)
# output_file = os.path.join(output_dir, "croma_laptops.csv")

# df = pd.DataFrame(laptop_data)
# df.to_csv(output_file, index=False)
# print(f"Scraped {len(laptop_data)} laptop products.")
# print(f"Data saved to {output_file}")
import json

# Convert output path to absolute
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.abspath(os.path.join(script_dir, "..", "data"))
os.makedirs(output_dir, exist_ok=True)

output_csv = os.path.join(output_dir, "croma_laptops.csv")
backup_csv = os.path.join(script_dir, "croma_laptops_backup.csv")
json_file = os.path.join(output_dir, "croma_laptops.json")

# Save CSV with fallback
try:
    df = pd.DataFrame(laptop_data)
    df.to_csv(output_csv, index=False, encoding="utf-8-sig")
    df.to_csv(backup_csv, index=False, encoding="utf-8-sig")
    print(f"[✔] CSV saved to: {output_csv}")
    print(f"[✔] Backup CSV saved to: {backup_csv}")
except Exception as e:
    print(f"[✘] CSV Save Failed: {e}")

# Redundant JSON Save
try:
    with open(json_file, "w", encoding="utf-8") as jf:
        json.dump(laptop_data, jf, indent=2, ensure_ascii=False)
    print(f"[✔] JSON backup saved to: {json_file}")
except Exception as e:
    print(f"[✘] JSON Save Failed: {e}")

# Print DataFrame summary
print("\n=== First 3 Products ===")
print(df.head(3))
print("\n=== Last 3 Products ===")
print(df.tail(3))
print(f"\nTotal Products: {len(df)}")

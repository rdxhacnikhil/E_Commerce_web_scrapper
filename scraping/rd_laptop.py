# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, WebDriverException
# import time
# import csv
# import os
# import random

# def create_driver(headless=False):
#     options = uc.ChromeOptions()

#     # Configure options to mimic human behavior
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_argument("--start-maximized")
#     options.add_argument("--disable-popup-blocking")
#     user_agent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100, 120)}.0.0.0 Safari/537.36"
#     options.add_argument(f"user-agent={user_agent}")

#     print("Using User-Agent:", user_agent)

#     # Configure undetected chromedriver
#     driver = uc.Chrome(
#         options=options,
#         headless=headless,
#         version_main=136  # Replace with your exact Chrome version if needed
#     )

#     return driver

# def handle_popups(driver):
#     """Handle various popups that might appear"""
#     try:
#         close_selectors = [
#             'button[class*="close"]',
#             'button[id*="wzrk-cancel"]',
#             'button[class*="cancel"]',
#             'div[class*="close"]'
#         ]
#         for selector in close_selectors:
#             try:
#                 elements = driver.find_elements(By.CSS_SELECTOR, selector)
#                 for element in elements:
#                     try:
#                         element.click()
#                         time.sleep(1)
#                     except:
#                         continue
#             except:
#                 continue
#     except:
#         pass

# def scrape_laptops(driver):
#     product_data = []
#     base_url = "https://www.reliancedigital.in/collection/popular-laptops?page="  # Modify the base URL as per your platform's page query
#     page_number = 1  # Starting page

#     while True:
#         url = f"{base_url}{page_number}"  # Constructing the URL for the next page
#         print(f"Scraping page {page_number}: {url}")

#         try:
#             retry_count = 0
#             while retry_count < 3:
#                 try:
#                     driver.get(url)
#                     WebDriverWait(driver, 15).until(
#                         EC.presence_of_element_located((By.TAG_NAME, 'body'))
#                     )
#                     break
#                 except (TimeoutException, WebDriverException):
#                     retry_count += 1
#                     print(f"Retry {retry_count} for page load")
#                     if retry_count == 3:
#                         raise
#                     time.sleep(5)

#             # Optional delay for realism
#             time.sleep(random.uniform(2, 4))

#             handle_popups(driver)

#             # Extract product elements
#             product_selectors = [
#                 "a.card-wrapper__body",
#                 "div.sp__product",
#                 "div.product-list",
#                 "div.product-item",
#                 "div.pd__product"
#             ]

#             products = []
#             for selector in product_selectors:
#                 try:
#                     products = driver.find_elements(By.CSS_SELECTOR, selector)
#                     if products:
#                         print(f"Found {len(products)} products with selector: {selector}")
#                         break
#                 except Exception as e:
#                     print(f"Error with selector {selector}: {e}")
#                     continue

#             if not products:
#                 print("No products found on this page")
#                 break  # No more products, stop the loop

#             # Extract product data from current page
#             for product in products:
#                 try:
#                     title = ""
#                     for title_selector in ["h5.card-title", "p.sp__name", ".product-title"]:
#                         try:
#                             title = product.find_element(By.CSS_SELECTOR, title_selector).text.strip()
#                             if title:
#                                 break
#                         except Exception as e:
#                             print(f"Error extracting title: {e}")
#                             continue

#                     price = ""
#                     for price_selector in ["span.card-discount-price", "span.sc-bdVaJa", ".price"]:
#                         try:
#                             price = product.find_element(By.CSS_SELECTOR, price_selector).text.strip()
#                             if price:
#                                 break
#                         except Exception as e:
#                             print(f"Error extracting price: {e}")
#                             continue

#                     # URL
#                     try:
#                         url = product.get_attribute("href")
#                         if not url:
#                             url_elem = product.find_element(By.CSS_SELECTOR, "a")
#                             url = url_elem.get_attribute("href")
#                     except Exception as e:
#                         print(f"Error extracting URL: {e}")
#                         url = ""

#                     # Image URL
#                     try:
#                         image = product.find_element(By.CSS_SELECTOR, "img.fy__img, img").get_attribute("src")
#                     except Exception as e:
#                         print(f"Error extracting image: {e}")
#                         image = ""

#                     product_data.append({
#                         "title": title,
#                         "price": price,
#                         "url": url,
#                         "image_url": image
#                     })

#                 except Exception as e:
#                     print(f"Error extracting product: {str(e)[:100]}")

#             # Move to the next page
#             page_number += 1

#         except Exception as e:
#             print(f"Error during scraping: {str(e)[:200]}")
#             driver.save_screenshot("error_screenshot.png")
#             print("Saved error screenshot as error_screenshot.png")
#             break

#     return product_data


# def save_to_csv(data, filename="laptops.csv"):
#     if not data:
#         print("No data to save")
#         return

#     os.makedirs("data", exist_ok=True)
#     filepath = os.path.join("data", filename)

#     with open(filepath, "w", newline="", encoding="utf-8") as f:
#         fieldnames = ["title", "price", "url", "image_url"]
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data)

#     print(f"Saved {len(data)} products to {filepath}")

# if __name__ == "__main__":
#     driver = None
#     try:
#         print("Starting browser...")
#         driver = create_driver()

#         print("Scraping laptop data...")
#         products = scrape_laptops(driver)

#         print("Saving results...")
#         save_to_csv(products)

#     except Exception as e:
#         print(f"Fatal error: {e}")
#     finally:
#         if driver:
#             print("Closing browser...")
#             try:
#                 driver.quit()
#             except:
#                 pass
# import time
# import csv
# import os
# from bs4 import BeautifulSoup
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# from fake_useragent import UserAgent

# def scroll_to_load_all(driver, pause_time=2):
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     while True:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(pause_time)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             print("Reached end of page.")
#             break
#         last_height = new_height
#         print("Scrolled...")

# def scrape_reliance_laptops():
#     print("Starting browser...")
#     user_agent = UserAgent().random
#     print("Using User-Agent:", user_agent)

#     options = uc.ChromeOptions()
#     options.add_argument(f"user-agent={user_agent}")
#     options.headless = True
#     options.add_argument("--window-size=1920,1080")

#     driver = uc.Chrome(options=options)
    
#     try:
#         print("Scraping laptop data...")
#         driver.get( "https://www.reliancedigital.in/collection/popular-laptops")
#         time.sleep(5)

#         scroll_to_load_all(driver)

#         with open("page_source.html", "w", encoding="utf-8") as f:
#             f.write(driver.page_source)
#         print("Saved page source to page_source.html")

#         soup = BeautifulSoup(driver.page_source, "html.parser")
#         products = soup.select("a.card-wrapper__body")
#         print(f"Found {len(products)} products with selector: a.card-wrapper__body")

#         data = []
#         for product in products:
#             name = product.find("h5", class_="card-title").text.strip()
#             link = "https://www.reliancedigital.in" + product["href"]
#             price_tag = product.select_one("span.card-discount-price")
#             price = price_tag.text.strip() if price_tag else "N/A"
#             mrp_tag = product.select_one("p.card-wrapper__amount span")
#             mrp = mrp_tag.text.strip() if mrp_tag else "N/A"
#             offer_tag = product.select_one("span.card-offer")
#             offer = offer_tag.text.strip() if offer_tag else "N/A"
#             image_tag = product.find("img")
#             image_url = image_tag["src"] if image_tag else "N/A"

#             data.append([name, price, mrp, offer, link, image_url])

#         print("Saving results...")
#         os.makedirs("data", exist_ok=True)
#         with open("data/laptops.csv", "w", newline="", encoding="utf-8") as f:
#             writer = csv.writer(f)
#             writer.writerow(["Name", "Price", "MRP", "Offer", "Link", "Image URL"])
#             writer.writerows(data)

#         print(f"Saved {len(data)} products to data/laptops.csv")

#     finally:
#         if driver:
#             try:
#                 driver.quit()
#             except Exception as e:
#                 print(f"Ignored exception while closing browser: {e}")

# if __name__ == "__main__":
#     scrape_reliance_laptops()
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, WebDriverException
# import time
# import csv
# import os
# import random

# def create_driver(headless=False):
#     options = uc.ChromeOptions()
    
#     # Configure options to mimic human behavior
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_argument("--start-maximized")
#     options.add_argument("--disable-popup-blocking")
#     user_agent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100, 120)}.0.0.0 Safari/537.36"
#     options.add_argument(f"user-agent={user_agent}")

#     # Configure undetected chromedriver
#     driver = uc.Chrome(
#         options=options,
#         headless=headless,
#         version_main=136  # Must match your Chrome version
#     )
    
#     return driver

# def handle_popups(driver):
#     """Handle various popups that might appear"""
#     try:
#         # Try multiple possible popup close buttons
#         close_selectors = [
#             'button[class*="close"]',
#             'button[id*="wzrk-cancel"]',
#             'button[class*="cancel"]',
#             'div[class*="close"]'
#         ]
        
#         for selector in close_selectors:
#             try:
#                 elements = driver.find_elements(By.CSS_SELECTOR, selector)
#                 for element in elements:
#                     try:
#                         element.click()
#                         time.sleep(1)
#                     except:
#                         continue
#             except:
#                 continue
#     except:
#         pass

# def scrape_laptops(driver):
#     product_data = []
#     url = "https://www.reliancedigital.in/collection/popular-laptops"
    
#     try:
#         # Load page with retry mechanism
#         retry_count = 0
#         while retry_count < 3:
#             try:
#                 driver.get(url)
#                 WebDriverWait(driver, 15).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-card"))
#                 )
#                 break
#             except (TimeoutException, WebDriverException) as e:
#                 retry_count += 1
#                 print(f"Retry {retry_count} for page load")
#                 if retry_count == 3:
#                     raise
#                 time.sleep(5)
        
#         # Handle popups
#         handle_popups(driver)
        
#         # Scroll to load all products
#         last_height = driver.execute_script("return document.body.scrollHeight")
#         while True:
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(2)
#             new_height = driver.execute_script("return document.body.scrollHeight")
#             if new_height == last_height:
#                 break
#             last_height = new_height
        
#         # Find all product cards
#         products = driver.find_elements(By.CSS_SELECTOR, "div.product-card")
#         print(f"Found {len(products)} products")
        
#         for product in products:
#             try:
#                 # Extract title
#                 title = product.find_element(By.CSS_SELECTOR, "div.product-card-title").text.strip()
                
#                 # Extract price
#                 price = product.find_element(By.CSS_SELECTOR, "div.price").text.strip()
                
#                 # Extract MRP
#                 mrp = product.find_element(By.CSS_SELECTOR, "div.mrp-amount").text.strip()
                
#                 # Extract URL
#                 url = product.find_element(By.CSS_SELECTOR, "a.product-card-image").get_attribute('href')
                
#                 # Extract image URL
#                 image = product.find_element(By.CSS_SELECTOR, "img.fy__img").get_attribute('src')
                
#                 product_data.append({
#                     "title": title,
#                     "price": price,
#                     "mrp": mrp,
#                     "url": url,
#                     "image_url": image
#                 })
#             except Exception as e:
#                 print(f"Error extracting product: {str(e)[:100]}")
        
#     except Exception as e:
#         print(f"Error during scraping: {str(e)[:200]}")
#         driver.save_screenshot("error_screenshot.png")
#         print("Saved error screenshot as error_screenshot.png")
    
#     return product_data

# def save_to_csv(data, filename="laptops.csv"):
#     if not data:
#         print("No data to save")
#         return
    
#     os.makedirs("data", exist_ok=True)
#     filepath = os.path.join("data", filename)
    
#     with open(filepath, "w", newline="", encoding="utf-8") as f:
#         fieldnames = ["title", "price", "mrp", "url", "image_url"]
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data)
    
#     print(f"Saved {len(data)} products to {filepath}")

# if __name__ == "__main__":
#     driver = None
#     try:
#         print("Starting browser...")
#         driver = create_driver()
        
#         print("Scraping laptop data...")
#         products = scrape_laptops(driver)
        
#         print("Saving results...")
#         save_to_csv(products)
        
#     except Exception as e:
#         print(f"Fatal error: {e}")
#     finally:
#         if driver:
#             print("Closing browser...")
#             try:
#                 driver.quit()
#             except:
#                 pass  # Ignore quit errors
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import csv
import os
import random

def create_driver(headless=False):
    options = uc.ChromeOptions()
    
    # Configure options to mimic human behavior
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-popup-blocking")
    user_agent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100, 120)}.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")

    # Configure undetected chromedriver
    driver = uc.Chrome(
        options=options,
        headless=headless,
        version_main=136  # Must match your Chrome version
    )
    
    return driver

def handle_popups(driver):
    """Handle various popups that might appear"""
    try:
        # Try multiple possible popup close buttons
        close_selectors = [
            'button[class*="close"]',
            'button[id*="wzrk-cancel"]',
            'button[class*="cancel"]',
            'div[class*="close"]'
        ]
        
        for selector in close_selectors:
            try:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                for element in elements:
                    try:
                        element.click()
                        time.sleep(1)
                    except:
                        continue
            except:
                continue
    except:
        pass

def scrape_laptops(driver, max_pages=50):
    product_data = []
    base_url = "https://www.reliancedigital.in/collection/popular-laptops?page="
    
    for page_num in range(1, max_pages + 1):
        url = f"{base_url}{page_num}"
        print(f"\nScraping page {page_num}/{max_pages} - {url}")
        
        try:
            # Load page with retry mechanism
            retry_count = 0
            while retry_count < 3:
                try:
                    driver.get(url)
                    WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-card"))
                    )
                    break
                except (TimeoutException, WebDriverException) as e:
                    retry_count += 1
                    print(f"Retry {retry_count} for page load")
                    if retry_count == 3:
                        raise
                    time.sleep(5)
            
            # Handle popups
            handle_popups(driver)
            
            # Scroll to load all products
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            
            # Find all product cards
            products = driver.find_elements(By.CSS_SELECTOR, "div.product-card")
            print(f"Found {len(products)} products on page {page_num}")
            
            for product in products:
                try:
                    # Extract title
                    title = product.find_element(By.CSS_SELECTOR, "div.product-card-title").text.strip()
                    
                    # Extract price
                    price = product.find_element(By.CSS_SELECTOR, "div.price").text.strip()
                    
                    # Extract MRP
                    mrp = product.find_element(By.CSS_SELECTOR, "div.mrp-amount").text.strip()
                    
                    # Extract URL
                    product_url = product.find_element(By.CSS_SELECTOR, "a.product-card-image").get_attribute('href')
                    
                    # Extract image URL
                    image = product.find_element(By.CSS_SELECTOR, "img.fy__img").get_attribute('src')
                    
                    product_data.append({
                        "title": title,
                        "price": price,
                        "mrp": mrp,
                        "url": product_url,
                        "image_url": image,
                        "page": page_num
                    })
                except Exception as e:
                    print(f"Error extracting product: {str(e)[:100]}")
            
            # Random delay between pages to mimic human behavior
            time.sleep(random.uniform(3, 7))
            
        except Exception as e:
            print(f"Error during scraping page {page_num}: {str(e)[:200]}")
            driver.save_screenshot(f"error_page_{page_num}.png")
            print(f"Saved error screenshot as error_page_{page_num}.png")
            continue
    
    return product_data

def save_to_csv(data, filename="laptops.csv"):
    if not data:
        print("No data to save")
        return
    
    os.makedirs("data", exist_ok=True)
    filepath = os.path.join("data", filename)
    
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["title", "price", "mrp", "url", "image_url", "page"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"\nSaved {len(data)} products to {filepath}")

if __name__ == "__main__":
    driver = None
    try:
        print("Starting browser...")
        driver = create_driver()
        
        print("Scraping laptop data across 5 pages...")
        products = scrape_laptops(driver, max_pages=50)
        
        print("\nSaving results...")
        save_to_csv(products)
        
    except Exception as e:
        print(f"Fatal error: {e}")
    finally:
        if driver:
            print("Closing browser...")
            try:
                driver.quit()
            except:
                pass  # Ignore quit errors
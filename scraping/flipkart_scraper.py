# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import pandas as pd
# from datetime import datetime
# import time
# import os

# def scrape_flipkart_selenium():
#     options = Options()
#     options.add_argument("--headless")  # Run browser in headless mode
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")

#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     url = "https://www.flipkart.com/search?q=mobiles&sid=tyy,4io&sort=popularity"
#     driver.get(url)

#     time.sleep(5)  # Wait for JavaScript to render

#     soup = BeautifulSoup(driver.page_source, 'lxml')
#     driver.quit()

#     products = []
#     product_containers = soup.select("div.yKfJKb.row")
#     if not product_containers:
#         print("No product containers found.")
#         return []

#     for product in product_containers:
#         title_tag = product.select_one(".KzDlHZ")
#         price_tag = product.select_one(".Nx9bqj._4b5DiR")
#         rating_tag = product.select_one(".XQDdHH")
#         reviews_tag = product.select_one(".Wphh3N")
#         delivery_tags = product.select(".yiggsN")
#         delivery_text = next((d.text.strip() for d in delivery_tags if "delivery" in d.text.lower()), None)

#         if not title_tag or not price_tag:
#             continue

#         products.append({
#             'timestamp': datetime.now().isoformat(),
#             'title': title_tag.text.strip(),
#             'price': int(price_tag.text.replace("₹", "").replace(",", "").strip()),
#             'rating': float(rating_tag.text.strip()) if rating_tag else None,
#             'reviews': reviews_tag.text.strip() if reviews_tag else None,
#             'delivery': delivery_text
#         })

#     return products

# def save_to_csv(data, filename='../data/flipkart_mobiles_history.csv'):
#     df = pd.DataFrame(data)
#     os.makedirs(os.path.dirname(filename), exist_ok=True)
#     df.to_csv(filename, mode='a', header=not os.path.exists(filename), index=False)

# # Run the scraper
# if __name__ == "__main__":
#     products = scrape_flipkart_selenium()
#     if products:
#         print(f"Scraped and saved {len(products)} products.")
#         save_to_csv(products)
#     else:
#         print("No products scraped.")
# scraping.py (or wherever your scraper resides)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
import time
import pandas as pd
import os
import json

def setup_driver():
    options = Options()
    # options.add_argument('--headless')  # Disable for debugging
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    
    # Set realistic user agent
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    options.add_argument(f'user-agent={user_agent}')
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def scrape_product(item):
    """Extract data from a single product item"""
    try:
        # Try multiple selector patterns for each field
        title = (item.select_one("div.KzDlHZ") or 
                 item.select_one("div._4rR01T") or
                 item.select_one("a.s1Q9rs") or
                 item.select_one("a.IRpwTa"))
        
        price = (item.select_one("div._30jeq3") or
                 item.select_one("div._30jeq3._1_WHN1") or
                 item.select_one("div.Nx9bqj"))
        
        rating = (item.select_one("div.XQDdHH") or
                  item.select_one("div._3LWZlK") or
                  item.find('div', {'class': lambda x: x and 'rating' in x.lower()}))
        
        reviews = (item.select_one("span.Wphh3N") or
                   item.select_one("span._2_R_DZ") or
                   item.find('span', text=lambda x: x and ('ratings' in x.lower() or 'reviews' in x.lower())))
        
        specs = [li.text for li in item.select("li.J+igdf, li.rgWa7D, li._3YhLQA")]
        delivery = (item.select_one("div.yiggsN") or
                    item.select_one("div._3tcB5a") or
                    item.find('div', text=lambda x: x and 'delivery' in x.lower()))

        if not title or not price:
            return None

        return {
            "timestamp": datetime.now().isoformat(),
            "title": title.text.strip(),
            "price": int(price.text.replace("₹", "").replace(",", "").strip()),
            "rating": float(rating.text.strip().split()[0]) if rating else None,
            "reviews": reviews.text.strip() if reviews else None,
            "specifications": " | ".join(specs) if specs else None,
            "delivery": delivery.text.strip() if delivery else None
        }
    except Exception as e:
        print(f"Error parsing product: {str(e)[:100]}")
        return None

def scrape_flipkart_mobiles(driver, pages=3):
    all_products = []
    
    for page in range(1, pages + 1):
        url = f"https://www.flipkart.com/search?q=mobiles&page={page}"
        print(f"\nScraping page {page}: {url}")
        
        try:
            driver.get(url)
            
            # Wait for either type of product container to load
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-id], div._1AtVbE, div._2kHMtA"))
            )
            time.sleep(2)  # Additional delay for stability
            
            # Save page source for debugging
            if not os.path.exists('debug'):
                os.makedirs('debug')
            with open(f'debug/page_{page}.html', 'w', encoding='utf-8') as f:
                f.write(driver.page_source)
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            # Find all potential product containers
            listings = soup.select("div[data-id], div._1AtVbE, div._2kHMtA, div._1xHGtK")
            print(f"Found {len(listings)} product containers")
            
            # Debug: Save first product container HTML
            if listings:
                with open(f'debug/product_sample_{page}.html', 'w', encoding='utf-8') as f:
                    f.write(str(listings[0]))
            
            # Extract data from each product
            page_products = []
            for idx, item in enumerate(listings, 1):
                product = scrape_product(item)
                if product:
                    page_products.append(product)
                    print(f"[Page {page}] Product {idx}: {product['title'][:30]}... (₹{product['price']})")
            
            all_products.extend(page_products)
            print(f"Page {page} complete - Valid products: {len(page_products)}")
            
        except Exception as e:
            print(f"Error scraping page {page}: {str(e)[:100]}")
            continue
    
    return all_products

def save_data(data, filename='flipkart_mobiles.csv'):
    try:
        df = pd.DataFrame(data)
        
        # Save to CSV
        df.to_csv(filename, index=False)
        print(f"\nSaved {len(data)} products to {filename}")
        
        # Also save as JSON for debugging
        json_file = filename.replace('.csv', '.json')
        df.to_json(json_file, orient='records', indent=2)
        print(f"Data also saved as {json_file} for inspection")
        
    except Exception as e:
        print(f"Failed to save data: {e}")

if __name__ == "__main__":
    print("Starting Flipkart Mobile Scraper...")
    
    driver = setup_driver()
    try:
        data = scrape_flipkart_mobiles(driver, pages=3)
        if data:
            save_data(data)
            print("\nScraping completed successfully!")
        else:
            print("\nScraping completed but no products were found.")
            print("Please check the debug HTML files in the 'debug' folder.")
    except Exception as e:
        print(f"\nScraping failed: {e}")
    finally:
        driver.quit()
        print("Driver closed.")
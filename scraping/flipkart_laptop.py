import os
import csv
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    return driver




def scrape_product(item):
    try:
        # Title and product URL
        link_tag = item.select_one("a.CGtC98")
        title_tag = item.select_one("img")
        title = title_tag['alt'].strip() if title_tag and 'alt' in title_tag.attrs else "No Title"
        product_url = f"https://www.flipkart.com{link_tag['href']}" if link_tag and 'href' in link_tag.attrs else "No URL"

        # Image URL
        image_url = title_tag['src'] if title_tag and 'src' in title_tag.attrs else "No Image"

        # Price
        price_tag = item.select_one("div.Nx9bqj._4b5DiR")
        price = price_tag.text.strip().replace("₹", "").replace(",", "") if price_tag else "0"

        # # Rating
        rating_tag = item.select_one("div.XQDdHH")
        rating = rating_tag.text.strip() if rating_tag else "No Rating"
        

        # Specs (sometimes inside ul tag)
        specs_tags = item.select("ul.gUuXy- li")
        specs = [li.text.strip() for li in specs_tags] if specs_tags else []

        return {
            'title': title,
            'price': price,
            'rating': rating,
            # 'reviews': reviews,
            'specs': specs,
            'product_url': product_url,
            'image_url': image_url
        }
    except Exception as e:
        print("Error parsing product:", e)
        return None


def scrape_flipkart_laptops(driver, pages=40):
    all_products = []

    for page in range(1, pages + 1):
        url = f"https://www.flipkart.com/search?q=laptop&page={page}"
        print(f"\nScraping page {page}: {url}")

        try:
            driver.get(url)
            print("Page title:", driver.title)
            time.sleep(3 + random.uniform(1, 2))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.tUxRFH"))
            )
            time.sleep(2)

            if not os.path.exists('debug'):
                os.makedirs('debug')
            with open(f'debug/page_laptop_{page}.html', 'w', encoding='utf-8') as f:
                f.write(driver.page_source)

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            listings = soup.select("div.tUxRFH")
            print(f"Found {len(listings)} product containers")

            if listings:
                with open(f'debug/product_sample_laptop_{page}.html', 'w', encoding='utf-8') as f:
                    f.write(str(listings[0]))

            page_products = []
            for idx, item in enumerate(listings, 1):
                product = scrape_product(item)
                if product:
                    page_products.append(product)
                    print(f"[Page {page}] Product {idx}: {product['title'][:30]}... (₹{product['price']})")

            all_products.extend(page_products)
            print(f"Page {page} complete - Valid products: {len(page_products)}")
            if not page_products:
                print(f"No valid products found on page {page}. Stopping early.")
                break

        except Exception as e:
            print(f"Error scraping page {page}: {str(e)[:100]}")
            continue

    return all_products


def save_data(data, filename='flipkart_laptops.csv'):
    if not data:
        print("No data to save.")
        return

    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in data:
            row['specs'] = ', '.join(row['specs'])  # Join specs list for CSV
            writer.writerow(row)

    print(f"\nSaved {len(data)} products to {filename}")



if __name__ == "__main__":
    driver = setup_driver()
    try:
        data = scrape_flipkart_laptops(driver, pages=3)
        save_data(data, filename='flipkart_laptops.csv')
    finally:
        driver.quit()

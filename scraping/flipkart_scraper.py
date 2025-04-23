from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import os

def scrape_flipkart_selenium():
    options = Options()
    options.add_argument("--headless")  # Run browser in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    url = "https://www.flipkart.com/search?q=mobiles&sid=tyy,4io&sort=popularity"
    driver.get(url)

    time.sleep(5)  # Wait for JavaScript to render

    soup = BeautifulSoup(driver.page_source, 'lxml')
    driver.quit()

    products = []
    product_containers = soup.select("div.yKfJKb.row")
    if not product_containers:
        print("No product containers found.")
        return []

    for product in product_containers:
        title_tag = product.select_one(".KzDlHZ")
        price_tag = product.select_one(".Nx9bqj._4b5DiR")
        rating_tag = product.select_one(".XQDdHH")
        reviews_tag = product.select_one(".Wphh3N")
        delivery_tags = product.select(".yiggsN")
        delivery_text = next((d.text.strip() for d in delivery_tags if "delivery" in d.text.lower()), None)

        if not title_tag or not price_tag:
            continue

        products.append({
            'timestamp': datetime.now().isoformat(),
            'title': title_tag.text.strip(),
            'price': int(price_tag.text.replace("₹", "").replace(",", "").strip()),
            'rating': float(rating_tag.text.strip()) if rating_tag else None,
            'reviews': reviews_tag.text.strip() if reviews_tag else None,
            'delivery': delivery_text
        })

    return products

def save_to_csv(data, filename='../data/flipkart_mobiles_history.csv'):
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, mode='a', header=not os.path.exists(filename), index=False)

# Run the scraper
if __name__ == "__main__":
    products = scrape_flipkart_selenium()
    if products:
        print(f"Scraped and saved {len(products)} products.")
        save_to_csv(products)
    else:
        print("No products scraped.")


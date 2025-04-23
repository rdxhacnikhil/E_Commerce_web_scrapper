# from scraping.flipkart_scraper import scrape_flipkart_mobiles, save_to_csv
from scraping.flipkart_scraper import scrape_flipkart_selenium, save_to_csv

if __name__ == "__main__":
    data = scrape_flipkart_selenium()
    save_to_csv(data)
    print(f"Scraped and saved {len(data)} products.")

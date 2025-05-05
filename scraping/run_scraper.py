# scraping/run_scraper.py

import argparse
from common.driver_setup import setup_driver
from scraping.flipkart_mobiles import scrape_flipkart_mobiles

from scraping.flipkart_laptop import scrape_flipkart_electronics

def main():
    parser = argparse.ArgumentParser(description="Flipkart Scraper")
    parser.add_argument("--mobiles", action="store_true", help="Scrape mobiles")
    parser.add_argument("--electronics", action="store_true", help="Scrape electronics")
    parser.add_argument("--pages", type=int, default=2, help="Number of pages to scrape")
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode")
    args = parser.parse_args()

    driver = setup_driver(headless=args.headless)
    try:
        if args.mobiles:
            scrape_flipkart_mobiles(driver, pages=args.pages)
        if args.electronics:
            scrape_flipkart_electronics(driver, pages=args.pages)
        if not args.mobiles and not args.electronics:
            print("❗ Please specify at least one target: --mobiles or --electronics")
    finally:
        driver.quit()
        print("✅ Driver closed.")

if __name__ == "__main__":
    main()

# from scraping.flipkart_scraper import scrape_flipkart_mobiles, save_to_csv
from scraping.flipkart_scraper import scrape_flipkart_mobiles, save_data
from scraping.flipkart_scraper import setup_driver, scrape_flipkart_mobiles, save_data


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


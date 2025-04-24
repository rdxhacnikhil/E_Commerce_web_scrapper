# # from scraping.flipkart_scraper import scrape_flipkart_mobiles, save_to_csv
# # from scraping.flipkart_scraper import scrape_flipkart_mobiles, save_data
# # from scraping.flipkart_scraper import setup_driver, scrape_flipkart_mobiles, save_data


# # if __name__ == "__main__":
# #     print("Starting Flipkart Mobile Scraper...")

# #     driver = setup_driver()
# #     try:
# #         data = scrape_flipkart_mobiles(driver, pages=40)
# #         if data:
# #             save_data(data)
# #             print("\nScraping completed successfully!")
# #         else:
# #             print("\nScraping completed but no products were found.")
# #             print("Please check the debug HTML files in the 'debug' folder.")
# #     except Exception as e:
# #         print(f"\nScraping failed: {e}")
# #     finally:
# #         driver.quit()
# #         print("Driver closed.")
# # run_scraper.py

# import argparse
# from scraping.flipkart_scraper import scrape_flipkart_mobiles, setup_driver, save_data
# from scraping.amazon_scraper import get_amazon_mobile_data
# import os

# def main():
#     parser = argparse.ArgumentParser(description="Mobile Scraper CLI")
#     parser.add_argument(
#         "--site",
#         choices=["flipkart", "amazon", "all"],
#         required=True,
#         help="Choose which site to scrape: flipkart, amazon, or all"
#     )
#     parser.add_argument(
#         "--pages",
#         type=int,
#         default=40,
#         help="Number of pages to scrape"
#     )

#     args = parser.parse_args()

#     # Ensure the 'data' directory exists
#     if not os.path.exists('data'):
#         os.makedirs('data')

#     # Setup driver for Flipkart scraper
#     driver = setup_driver()

#     if args.site == "flipkart":
#         print("Starting Flipkart scraper...")
#         products = scrape_flipkart_mobiles(driver, pages=args.pages)
#         save_data(products, filename="data/flipkart_mobiles.csv")

#     elif args.site == "amazon":
#         print("Starting Amazon scraper...")
#         products = get_amazon_mobile_data(pages=args.pages)
#         save_data(products, filename="data/amazon_mobiles.csv")

#     elif args.site == "all":
#         print("Starting both Flipkart and Amazon scrapers...")

#         flipkart_products = scrape_flipkart_mobiles(driver, pages=args.pages)
#         save_data(flipkart_products, filename="data/flipkart_mobiles.csv")

#         amazon_products = get_amazon_mobile_data(pages=args.pages)
#         save_data(amazon_products, filename="data/amazon_mobiles.csv")

#     # Close the driver after scraping
#     driver.quit()

# if __name__ == "__main__":
#     main()
# run_scraper.py
# run_scraper.py (updated)
import argparse
from scraping.flipkart_scraper import scrape_flipkart_mobiles, setup_driver as flipkart_driver_setup, save_data
from scraping.amazon_scraper import get_amazon_mobile_data
from scraping.croma_scraper import scrape_croma_products, setup_driver as croma_driver_setup
import os

def main():
    parser = argparse.ArgumentParser(description="Mobile Scraper CLI")
    parser.add_argument(
        "--site",
        choices=["flipkart", "amazon", "croma", "all"],
        required=True,
        help="Choose which site to scrape: flipkart, amazon, croma, or all"
    )
    # parser.add_argument(
    #     "--pages",
    #     type=int,
    #     default=40,
    #     help="Number of pages to scrape (for Flipkart and Amazon)"
    # )
    parser.add_argument(
    "--limit",
    type=int,
    default=1000,
    help="Maximum number of products to scrape (for Croma)"
    )

    args = parser.parse_args()

    if not os.path.exists('data'):
        os.makedirs('data')

    # Use a single driver instance for all scrapers
    driver = None
    
    try:
        if args.site == "croma":
            print("🔍 Starting Croma scraper...")
            driver = croma_driver_setup()
            products = scrape_croma_products(driver, max_products=args.limit)
            save_data(products, filename="data/croma_mobiles.csv")
            
        elif args.site == "flipkart":
            print("Starting Flipkart scraper...")
            driver = flipkart_driver_setup()
            products = scrape_flipkart_mobiles(driver, pages=args.pages)
            save_data(products, filename="data/flipkart_mobiles.csv")
            
        elif args.site == "amazon":
            print("Starting Amazon scraper...")
            driver = flipkart_driver_setup()  # Shared driver setup
            products = get_amazon_mobile_data(driver, pages=args.pages)
            save_data(products, filename="data/amazon_mobiles.csv")
            
        elif args.site == "all":
            print("Starting all scrapers...")
            driver = croma_driver_setup()
            
            # Croma
            print("🔍 Starting Croma scraper...")
            croma_products = scrape_croma_products(driver)
            save_data(croma_products, filename="data/croma_mobiles.csv")
            
            # Flipkart
            print("Starting Flipkart scraper...")
            flipkart_products = scrape_flipkart_mobiles(driver, pages=args.pages)
            save_data(flipkart_products, filename="data/flipkart_mobiles.csv")
            
            # Amazon
            print("Starting Amazon scraper...")
            amazon_products = get_amazon_mobile_data(driver, pages=args.pages)
            save_data(amazon_products, filename="data/amazon_mobiles.csv")

    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()













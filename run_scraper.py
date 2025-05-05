# from scraping.flipkart_scraper import scrape_flipkart_mobiles, save_to_csv
# from scraping.flipkart_scraper import scrape_flipkart_mobiles, save_data
# from scraping.flipkart_scraper import setup_driver, scrape_flipkart_mobiles, save_data


# if __name__ == "__main__":
#     print("Starting Flipkart Mobile Scraper...")

#     driver = setup_driver()
#     try:
#         data = scrape_flipkart_mobiles(driver, pages=40)
#         if data:
#             save_data(data)
#             print("\nScraping completed successfully!")
#         else:
#             print("\nScraping completed but no products were found.")
#             print("Please check the debug HTML files in the 'debug' folder.")
#     except Exception as e:
#         print(f"\nScraping failed: {e}")
#     finally:
#         driver.quit()
#         print("Driver closed.")
# run_scraper.py

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
# from scraping.reliance_scraper import scrape_reliance_best_selling,scrape_reliance_5g_smartphones, setup_driver as reliance_driver_setup
# from scraping.utils import save_data
# import argparse
# import csv
# from scraping.flipkart_laptop import scrape_flipkart_laptops,setup_driver as flipkart_driver_setup, save_data
# from scraping.flipkart_mobiles import scrape_flipkart_mobiles, setup_driver as flipkart_driver_setup, save_data
# from scraping.amazon_scraper import get_amazon_mobile_data
# from scraping.croma_scraper import scrape_croma_products, setup_driver as croma_driver_setup
# from scraping.amazon_laptop import get_amazon_laptop_data
# import os
# from scraping.amazon_laptop import get_amazon_laptop_data

# def main():
#     parser = argparse.ArgumentParser(description="Run E-Commerce Scraper")
#     parser.add_argument("--site", required=True, choices=["amazon"], help="Which site to scrape")
#     parser.add_argument("--category", required=True, choices=["laptops"], help="Product category to scrape")
#     parser.add_argument("--pages", type=int, default=1, help="Number of pages to scrape")

#     args = parser.parse_args()

#     if args.site == "amazon" and args.category == "laptops":
#         print(f"\n🚀 Scraping Amazon Laptops (Pages: {args.pages})")
#         data = get_amazon_laptop_data(pages=args.pages)
#         save_to_csv(data, "amazon_laptops.csv")
#     parser.add_argument(
#         "--category",
#         choices=["mobiles", "laptops"],
#         default="mobiles",
#         help="Choose category to scrape for Flipkart"
#     )
#     # parser.add_argument(
#     #     "--pages",
#     #     type=int,
#     #     default=1,
#     #     help="Number of pages to scrape (for Flipkart and Amazon)"
#     # )
#     parser.add_argument(
#     "--limit",
#     type=int,
#     default=100,
#     help="Maximum number of products to scrape (for Croma)"
#     )

#     args = parser.parse_args()

#     if not os.path.exists('data'):
#         os.makedirs('data')

#     # Use a single driver instance for all scrapers
#     driver = None
    
#     try:
#         if args.site == "croma":
#             print("🔍 Starting Croma scraper...")
#             driver = croma_driver_setup()
#             products = scrape_croma_products(driver, max_products=args.limit)
#             save_data(products, filename="data/croma_mobiles.csv")
            
#         elif args.site == "flipkart":
#             print("Starting Flipkart scraper...")
#             driver = flipkart_driver_setup()
#             if args.category == "mobiles":
#                 products = scrape_flipkart_mobiles(driver, pages=args.pages)
#                 save_data(products, filename="data/flipkart_mobiles.csv")
#             elif args.category == "laptops":
#                 products = scrape_flipkart_laptops(driver, pages=args.pages)
#                 save_data(products, filename="data/flipkart_laptops.csv")

            
#         elif args.site == "amazon":
#             print("Starting Amazon scraper...")
#             driver = flipkart_driver_setup()  # Shared driver setup
#             products = get_amazon_mobile_data(driver, pages=args.pages)
#             save_data(products, filename="data/amazon_mobiles.csv")
        
#         elif args.site == "reliance":
#             print("📱 Starting Reliance Digital scraper...")
#             driver = reliance_driver_setup()
#             products = scrape_reliance_best_selling(driver, pages=args.pages)
#             save_data(products, filename="data/reliance_mobiles.csv")
#         elif args.site == "reliance_5g":
#             print("Starting Reliance 5G smartphones scraper...")
#             driver = flipkart_driver_setup()  # or a shared setup_driver
#             products = scrape_reliance_5g_smartphones(driver, pages=args.pages)
#             save_data(products, filename="data/reliance_5g_mobiles.csv")

#         elif args.site == "all":
#             print("Starting all scrapers...")
#             driver = croma_driver_setup()
            
#             # Croma
#             print("🔍 Starting Croma scraper...")
#             croma_products = scrape_croma_products(driver)
#             save_data(croma_products, filename="data/croma_mobiles.csv")
            
#             # Flipkart
#             print("Starting Flipkart scraper...")
#             flipkart_products = scrape_flipkart_mobiles(driver, pages=args.pages)
#             save_data(flipkart_products, filename="data/flipkart_mobiles.csv")
            
#             # Amazon
#             print("Starting Amazon scraper...")
#             amazon_products = get_amazon_mobile_data(driver, pages=args.pages)
#             save_data(amazon_products, filename="data/amazon_mobiles.csv")

#             # Reliance
#             print("📱 Starting Reliance Digital scraper...")
#             # reliance_products = scrape_reliance_products(driver, pages=args.pages)
#             products_1 = scrape_reliance_best_selling(driver, pages=args.pages)
#             save_data(products_1, filename="data/reliance_best_selling.csv")

#             products_2 = scrape_reliance_5g_smartphones(driver, pages=args.pages)
#             save_data(products_2, filename="data/reliance_5g_smartphones.csv")

#     finally:
#         if driver:
#             driver.quit()

# if __name__ == "__main__":
#     main()
# import argparse
# import os
# from scraping.flipkart_laptop import scrape_flipkart_laptops, setup_driver as flipkart_driver_setup
# from scraping.flipkart_mobiles import scrape_flipkart_mobiles
# from scraping.amazon_scraper import get_amazon_mobile_data
# from scraping.amazon_laptop import get_amazon_laptop_data, save_data as save_amazon_laptop_data
# from scraping.reliance_scraper import scrape_reliance_best_selling, scrape_reliance_5g_smartphones, setup_driver as reliance_driver_setup
# from scraping.croma_scraper import scrape_croma_products, setup_driver as croma_driver_setup
# from scraping.utils import save_data

# def main():
#     parser = argparse.ArgumentParser(description="Run E-Commerce Scraper")
#     parser.add_argument("--site", required=True, choices=["flipkart", "amazon", "croma", "reliance", "reliance_5g", "all"], help="Which site to scrape")
#     parser.add_argument("--category", choices=["mobiles", "laptops"], default="mobiles", help="Product category to scrape")
#     parser.add_argument("--pages", type=int, default=1, help="Number of pages to scrape")
#     parser.add_argument("--limit", type=int, default=1000, help="Max products (for Croma)")

#     args = parser.parse_args()

#     if not os.path.exists('data'):
#         os.makedirs('data')

#     driver = None

#     try:
#         if args.site == "flipkart":
#             print("🚀 Starting Flipkart scraper...")
#             driver = flipkart_driver_setup()
#             if args.category == "mobiles":
#                 products = scrape_flipkart_mobiles(driver, pages=args.pages)
#                 save_data(products, filename="data/flipkart_mobiles.csv")
#             elif args.category == "laptops":
#                 products = scrape_flipkart_laptops(driver, pages=args.pages)
#                 save_data(products, filename="data/flipkart_laptops.csv")

#         elif args.site == "amazon":
#             print("🚀 Starting Amazon scraper...")
#             if args.category == "mobiles":
#                 driver = flipkart_driver_setup()
#                 products = get_amazon_mobile_data(driver, pages=args.pages)
#                 save_data(products, filename="data/amazon_mobiles.csv")
#             elif args.category == "laptops":
#                 products = get_amazon_laptop_data(pages=args.pages)
#                 save_amazon_laptop_data(products, filename="amazon_laptops.csv")

#         elif args.site == "croma":
#             print("🔍 Starting Croma scraper...")
#             driver = croma_driver_setup()
#             products = scrape_croma_products(driver, max_products=args.limit)
#             save_data(products, filename="data/croma_mobiles.csv")

#         elif args.site == "reliance":
#             print("📱 Starting Reliance Digital scraper...")
#             driver = reliance_driver_setup()
#             products = scrape_reliance_best_selling(driver, pages=args.pages)
#             save_data(products, filename="data/reliance_mobiles.csv")

#         elif args.site == "reliance_5g":
#             print("📱 Starting Reliance 5G smartphones scraper...")
#             driver = flipkart_driver_setup()
#             products = scrape_reliance_5g_smartphones(driver, pages=args.pages)
#             save_data(products, filename="data/reliance_5g_mobiles.csv")

#         elif args.site == "all":
#             print("🚀 Running all scrapers...")

#             # Croma
#             print("🔍 Croma scraping...")
#             driver = croma_driver_setup()
#             croma_products = scrape_croma_products(driver, max_products=args.limit)
#             save_data(croma_products, filename="data/croma_mobiles.csv")
#             driver.quit()

#             # Flipkart
#             driver = flipkart_driver_setup()
#             flipkart_products = scrape_flipkart_mobiles(driver, pages=args.pages)
#             save_data(flipkart_products, filename="data/flipkart_mobiles.csv")

#             flipkart_laptops = scrape_flipkart_laptops(driver, pages=args.pages)
#             save_data(flipkart_laptops, filename="data/flipkart_laptops.csv")
#             driver.quit()

#             # Amazon
#             driver = flipkart_driver_setup()
#             amazon_mobiles = get_amazon_mobile_data(driver, pages=args.pages)
#             save_data(amazon_mobiles, filename="data/amazon_mobiles.csv")
#             driver.quit()

#             amazon_laptops = get_amazon_laptop_data(pages=args.pages)
#             save_amazon_laptop_data(amazon_laptops, filename="amazon_laptops.csv")

#             # Reliance
#             driver = reliance_driver_setup()
#             reliance_best = scrape_reliance_best_selling(driver, pages=args.pages)
#             save_data(reliance_best, filename="data/reliance_best_selling.csv")

#             reliance_5g = scrape_reliance_5g_smartphones(driver, pages=args.pages)
#             save_data(reliance_5g, filename="data/reliance_5g_smartphones.csv")
#             driver.quit()

#     finally:
#         if driver:
#             driver.quit()

# if __name__ == "__main__":
#     main()
import argparse
import os

from scraping.flipkart_laptop import scrape_flipkart_laptops, setup_driver as flipkart_driver_setup
from scraping.flipkart_mobiles import scrape_flipkart_mobiles
from scraping.amazon_scraper import get_amazon_mobile_data
from scraping.amazon_laptop import get_amazon_laptop_data, save_data as save_amazon_laptop_data
# from scraping.reliance_scraper import scrape_reliance_best_selling, scrape_reliance_5g_smartphones, setup_driver as reliance_driver_setup
# from scraping.croma_scraper import scrape_croma_products, setup_driver as croma_driver_setup
# from scraping.croma_laptop import scrape_croma_laptops, save_data as save_croma_laptop_data
from scraping.utils import save_data

def main():
    parser = argparse.ArgumentParser(description="Run E-Commerce Scraper")
    parser.add_argument("--site", required=True, choices=["flipkart", "amazon", "croma", "reliance", "reliance_5g", "all"], help="Which site to scrape")
    parser.add_argument("--category", choices=["mobiles", "laptops"], default="mobiles", help="Product category to scrape")
    parser.add_argument("--pages", type=int, default=1, help="Number of pages to scrape")
    parser.add_argument("--limit", type=int, default=1000, help="Max products (for Croma)")

    args = parser.parse_args()

    if not os.path.exists('data'):
        os.makedirs('data')

    driver = None

    try:
        if args.site == "flipkart":
            print("🚀 Starting Flipkart scraper...")
            driver = flipkart_driver_setup()
            if args.category == "mobiles":
                products = scrape_flipkart_mobiles(driver, pages=args.pages)
                save_data(products, filename="data/flipkart_mobiles.csv")
            elif args.category == "laptops":
                products = scrape_flipkart_laptops(driver, pages=args.pages)
                save_data(products, filename="data/flipkart_laptops.csv")

        elif args.site == "amazon":
            print("🚀 Starting Amazon scraper...")
            if args.category == "mobiles":
                # driver = flipkart_driver_setup()
                products = get_amazon_mobile_data(pages=args.pages)
                save_data(products, filename="data/amazon_mobiles.csv")
            elif args.category == "laptops":
                products = get_amazon_laptop_data(pages=args.pages)
                filename = os.path.join("data", "amazon_laptops.csv")
                # save_amazon_laptop_data(products, filename=filename)
                save_amazon_laptop_data(products, filename="data/amazon_laptops.csv")

        # elif args.site == "croma":
        #     print("🔍 Starting Croma scraper...")
        #     if args.category == "mobiles":
        #         driver = croma_driver_setup()
        #         # products = scrape_croma_products(driver, max_products=args.limit)
        #         products = scrape_croma_laptops(pages=args.pages)
        #         save_data(products, filename="data/croma_mobiles.csv")
        #     elif args.category == "laptops":
        #         # products = scrape_croma_laptops(max_scrolls=args.pages)
        #         products = scrape_croma_laptops(pages=args.pages)
        #         save_croma_laptop_data(products, filename="data/croma_laptops.csv")

        # elif args.site == "reliance":
        #     print("📱 Starting Reliance Digital scraper...")
        #     driver = reliance_driver_setup()
        #     products = scrape_reliance_best_selling(driver, pages=args.pages)
        #     save_data(products, filename="data/reliance_mobiles.csv")

        # elif args.site == "reliance_5g":
        #     print("📱 Starting Reliance 5G smartphones scraper...")
        #     driver = flipkart_driver_setup()
        #     products = scrape_reliance_5g_smartphones(driver, pages=args.pages)
        #     save_data(products, filename="data/reliance_5g_mobiles.csv")

        elif args.site == "all":
            print("🚀 Running all scrapers...")

            # Croma
            # print("🔍 Croma scraping...")
            # driver = croma_driver_setup()
            # croma_products = scrape_croma_products(driver, max_products=args.limit)
            # save_data(croma_products, filename="data/croma_mobiles.csv")
            # driver.quit()

            # croma_laptops = scrape_croma_laptops(max_scrolls=args.pages)
            # save_croma_laptop_data(croma_laptops, filename="data/croma_laptops.csv")

            # Flipkart
            driver = flipkart_driver_setup()
            flipkart_products = scrape_flipkart_mobiles(driver, pages=args.pages)
            save_data(flipkart_products, filename="data/flipkart_mobiles.csv")

            flipkart_laptops = scrape_flipkart_laptops(driver, pages=args.pages)
            save_data(flipkart_laptops, filename="data/flipkart_laptops.csv")
            driver.quit()

            # Amazon
            driver = flipkart_driver_setup()
            amazon_mobiles = get_amazon_mobile_data(driver, pages=args.pages)
            save_data(amazon_mobiles, filename="data/amazon_mobiles.csv")
            driver.quit()

            amazon_laptops = get_amazon_laptop_data(pages=args.pages)
            save_amazon_laptop_data(amazon_laptops, filename="data/amazon_laptops.csv")

            # Reliance
            # driver = reliance_driver_setup()
            # reliance_best = scrape_reliance_best_selling(driver, pages=args.pages)
            # save_data(reliance_best, filename="data/reliance_best_selling.csv")

            # reliance_5g = scrape_reliance_5g_smartphones(driver, pages=args.pages)
            # save_data(reliance_5g, filename="data/reliance_5g_smartphones.csv")
            # driver.quit()

    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()













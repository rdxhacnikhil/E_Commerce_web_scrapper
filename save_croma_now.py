from scraping.croma_scraper import setup_driver, scrape_croma_products
from scraping.flipkart_scraper import save_data  # Make sure save_data is accessible

driver = setup_driver()
driver.get("https://www.croma.com/phones-wearables/c/1")
print("Waiting for page and partial scroll...")
import time; time.sleep(3)

# Only scrape visible products (current ~1344)
product_cards = driver.find_elements_by_css_selector("div.cp-product.typ-plp.plp-srp-typ")

products = []
for card in product_cards:
    try:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
        time.sleep(0.5)
        product = {
            'name': card.find_element_by_css_selector("h3.product-title.plp-prod-title").text.strip(),
            'price': card.find_element_by_css_selector("span.amount.plp-srp-new-amount").text.replace('₹', '').replace(',', '').strip(),
            'url': card.find_element_by_css_selector("a[href^='/']").get_attribute("href"),
            'rating': card.find_element_by_css_selector("span.rating-text").text.split()[0] 
                if card.find_elements_by_css_selector("span.rating-text") else 'N/A'
        }
        products.append(product)
    except Exception as e:
        print(f"Error extracting: {str(e)[:50]}")

print(f"Saving {len(products)} products scraped so far...")
save_data(products, filename="data/croma_partial.csv")

driver.quit()

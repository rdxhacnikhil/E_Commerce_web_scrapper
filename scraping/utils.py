from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd
def setup_driver():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver
# scraping/utils.py
import os
import pandas as pd

def save_data(products, filename):
    df = pd.DataFrame(products)
    
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, index=False)

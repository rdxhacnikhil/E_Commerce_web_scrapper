# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import pandas as pd
# def setup_driver():
#     options = Options()
#     options.add_argument("--headless")  # Run in headless mode
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     driver = webdriver.Chrome(options=options)
#     return driver
# # scraping/utils.py
# import os
# import pandas as pd

# def save_data(products, filename):
#     df = pd.DataFrame(products)
#     os.makedirs(os.path.dirname(filename), exist_ok=True)  # Ensure target folder exists
#     if os.path.exists(filename):
#         df.to_csv(filename, mode='a', header=False, index=False)
#     else:
#         df.to_csv(filename, index=False)
# scraping/utils.py

import os
import pandas as pd
import json

def save_data(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✅ Saved {len(data)} records to {filename}")
    json_file = filename.replace('.csv', '.json')
    df.to_json(json_file, orient='records', indent=2)
    print(f"🧾 Also saved JSON: {json_file}")

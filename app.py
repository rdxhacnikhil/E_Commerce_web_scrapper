from flask import Flask, jsonify
from flask_cors import CORS
import json
import os
import re

app = Flask(__name__)
CORS(app)

def clean_mobile_name(text):
    if '(' in text:
        return text.split('(')[0].strip()
    elif ':' in text:
        return text.split(':')[0].strip()
    else:
        return text.strip()

def extract_color(text):
    color_match = re.search(r'\(([^)]+)\)', text) or re.search(r'\[([^]]+)\]', text)
    if color_match:
        details = color_match.group(1).strip()
        parts = [p.strip() for p in details.split(',')]
        return parts[-1] if parts else "Unknown"
    return "Unknown"

def is_mobile_product(name):
    non_mobile_keywords = [
        'smartwatch', 'watch', 'cover', 'case', 'earbuds', 'earphone', 'headphone',
        'neckband', 'airpods', 'charger', 'cable', 'power bank', 'adapter', 'buds',
        'selfie stick', 'headset', 'memory card', 'otg', 'stand', 'strap'
    ]
    name_lower = name.lower()
    return not any(keyword in name_lower for keyword in non_mobile_keywords)

def to_str_or_na(value):
    return 'N/A' if value is None else str(value)

def parse_reviews(reviews): #"1,234 Reviews"    → 1234
    if isinstance(reviews, str) and re.search(r'\d', reviews):
        return int(re.sub(r'[^\d]', '', reviews))
    return 0

@app.route('/api/products', methods=['GET'])
def get_products():
    products = []
    seen_flipkart = set()
    seen_amazon = set()
    seen_croma = set()

    # Process Flipkart data
    flipkart_file = 'flipkart_mobiles.json'
    if os.path.exists(flipkart_file):
        with open(flipkart_file, 'r') as f:
            flipkart_data = json.load(f)
            for entry in flipkart_data:
                title = entry.get('title', '')
                if title not in seen_flipkart and is_mobile_product(title):
                    seen_flipkart.add(title)
                    mobile_name = clean_mobile_name(title)
                    color = extract_color(title)
                    product = {
                        "mobile_name": mobile_name.lower(),
                        "color": color,
                        "source": "Flipkart",
                        "price": to_str_or_na(entry.get('price')),
                        "ratings_count": parse_reviews(entry.get('reviews')),
                    }
                    products.append(product)

    # Process Amazon data
    amazon_file = 'amazon_mobiles.json'
    if os.path.exists(amazon_file):
        with open(amazon_file, 'r') as f:
            amazon_data = json.load(f)
            for entry in amazon_data:
                name = entry.get('name', '')
                if name not in seen_amazon and is_mobile_product(name):
                    seen_amazon.add(name)
                    mobile_name = clean_mobile_name(name)
                    color = extract_color(name)
                    product = {
                        "mobile_name": mobile_name.lower(),
                        "color": color,
                        "source": "Amazon",
                        "price": to_str_or_na(entry.get('price')),
                        "ratings_count": parse_reviews(entry.get('reviews')),
                    }
                    products.append(product)

    # Process Croma data
    croma_file = 'croma_mobiles.json'
    if os.path.exists(croma_file):
        with open(croma_file, 'r') as f:
            croma_data = json.load(f)
            for entry in croma_data:
                name = entry.get('name', '')
                if name not in seen_croma and is_mobile_product(name):
                    seen_croma.add(name)
                    mobile_name = clean_mobile_name(name)
                    color = extract_color(name)
                    product = {
                        "mobile_name": mobile_name.lower(),
                        "color": color,
                        "source": "Croma",
                        "price": to_str_or_na(entry.get('price')),
                        "ratings_count": None,
                    }
                    products.append(product)

    if not products:
        return jsonify({'error': 'No valid products found'}), 404

    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
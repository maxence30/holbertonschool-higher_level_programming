#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    products = []

    if source == "json":
        with open('products.json', 'r') as file:
            products = json.load(file)

    elif source == "csv":
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            products = list(reader)

    else:
        return render_template(
            'product_display.html',
            error="Wrong source"
        )

    if product_id:
        products = [
            product for product in products
            if str(product.get('id')) == product_id
        ]

    return render_template(
        'product_display.html',
        products=products
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
#!/usr/bin/python3

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/products')
def products():
    source = request.args.get('source')

    if source != "sql":
        return render_template(
            'product_display.html',
            error="Wrong source"
        )

    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Products"
    )

    products = cursor.fetchall()

    conn.close()

    return render_template(
        'product_display.html',
        products=products
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
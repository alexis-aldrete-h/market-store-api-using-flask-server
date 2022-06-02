
from crypt import methods
from math import prod
from flask import Flask
from flask import abort
from about_me import me
from mock_data import catalog
import json

app = Flask('assignment2')

@app.route("/", methods=["GET"])
def home():
    return "This is the home page"

@app.route("/about")
def about():
    return (me["first"] +" "+ me["last"])

@app.route("/myaddress")
def address():
    return (me["address"]["street"] + " " + me["address"]["number"])


    ################## ENDPOINTS ##################

@app.route("/api/catalog", methods=["GET"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog/count", methods=["GET"])
def get_count():
    counts = len(catalog)
    return json.dumps(counts) 

@app.route("/api/catalog/<id>", methods=["GET"])
def get_product(id):
    for prod in catalog:
        if prod["_id"]==id:
            return json.dumps(prod)

    return abort(404, "Id does not match any product")

@app.route("/api/catalog/total", methods=["GET"])
def get_total():
    total = 0
    for product in catalog:
        price = product["price"]
        total += price
    return json.dumps(total)

@app.route("/api/products/<category>", methods=["GET"])
def get_category(category):
    products = []
    for product in catalog:
        if product["category"]==category.lower():
            products.append(product)
    return json.dumps(products)

@app.route("/api/categories", methods=["GET"])
def get_categories():
    categories = []
    for product in catalog:
        category = product["category"]
        if category not in categories:
            categories.append(category)
    return json.dumps(categories)

@app.route("/api/catalog/cheapest", methods=["GET"])
def get_cheapest():
    cheapestProduct = catalog[0]

    for product in catalog:
        if product["price"] < cheapestProduct["price"]:
            cheapestProduct = product
    return json.dumps(cheapestProduct)
    
app.run(debug=True)
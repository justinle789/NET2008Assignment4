import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Shirt", "color": "Black", "price": "30 CAD"},
    {"id": 2, "name": "Watch", "color": "Silver", "price": "150 CAD"},
    {"id": 3, "name": "Headphones", "color": "Grey", "price": "299 CAD"},
]


def _find_next_id():
    return max(product["id"] for product in products) + 1


def print1():
    return "Product removed"


def print2():
    return "not working"


@app.route("/")
def index():
    return "<h2>Welcome to Products API</h2>"


@app.get("/products")
def get_products():
    return jsonify(products)


@app.route("/products/1")
def add_Product1():
    return products[0]


@app.route("/products/2")
def add_Product2():
    return products[1]


@app.route("/products/3")
def add_Product3():
    return products[2]


@app.post("/products")
def add_products():
    if request.is_json:
        product = request.get_json()
        product["id"] = _find_next_id()
        products.append(product)
        return product, 201
    return {"error": "Request must be JSON"}, 415


@app.delete("/products/<id>")
def delete_productss(id:int):
    id = int(id) - 1
    for el in products:
        if el['id'] == int(id):
            del products[int(id)]
    return jsonify(products)

@app.put("/products/<id>")
def add_fourthProduct(id:int):
    fourthProduct = {"id": "4", "name": "type-c cable", "color": "white", "price": "15 CAD"}
    products.append(fourthProduct)
    return jsonify(products)

@app.route("/products/4")
def product4():
    return products[3]

if __name__ == "main":
    app.run()







# url = "http: //127.0.0.1:5000/products"
# responspes = reequest.get(url)

# API: an interface that enables communications between programs that use different languages
# Client
#       Clients only make requests.
# Server
#       Servers only makes responses.
#
# JSON is used instead of html
#        Notation used to describe information.
#               Like text
#        Alternatives
#                Xml
#                      old fashion


# @app.delete("/products/<id>", methods=['Delete'])
# def delete_products(id):
#
#
#     for el1, el2, el3, el4 in products:
#          if el1["id"] == id:
#
#             #deleted = products.index(id)
#             # IDN = int(el["id"]) - 1
#             #products.remove(id)                     # <------------
#             #return jsonify(products)                # <------------
#             # response = request.delete(url)
#             # response.json()

# @app.get("/products/<id>")
# def get_saidProduct(id):
#     url = "http://127.0.0.1:5000/products/" + id
#     return request.get(url)

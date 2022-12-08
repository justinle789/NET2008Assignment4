import requests

url = "http://127.0.0.1:5000/products/3"
response1 = requests.delete(url)

Second_URL = "http://127.0.0.1:5000/products/4"
response2 = requests.put(Second_URL)



# products = [
#     {"id":1, "name": "Shirt", "color": "Black", "price": "30 CAD" },
#     {"id":2, "name": "Watch", "color": "Silver", "price": "150 CAD" },
#     {"id":3, "name": "Headphones", "color": "Grey", "price": "299 CAD" },
# ]
#
# def delete_productss(id):
#     for el in products:
#         if el['id'] == 1:
#             del products[id]
#
#
# delete_productss(1)
# for el in products:
#     print(el)



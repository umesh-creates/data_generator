import json
import random
products = {
    # product_id (pk)
    'products_id' : [i for i in range(50)],
    'product_name': [],
    'category': [],
    'brand': [],
    'cost_price' : [],
    'selling_price' : []
}

# product_name 
# category
# brand 
with open('catalog.json') as f:
    catalog = json.load(f)

for category in catalog['categories']:
    print(category)
    for brand in catalog[]

# print(random.choice(list[catalog['devices'].keys()]))

# cost_price
# selling_price
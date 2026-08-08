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

for electronic_product in list(catalog['items']['Electronics_products'].keys())[:20]:
    pass
    # print(electronic_product) # product_name
    # print(list(catalog['categories'].keys())[0]) # category
    # print(random.choice(list(catalog['categories']['Electronics'].keys()))) # brand

for clothing_item in list(catalog['items']['Clothing_items'].keys())[:20]:
    pass
    # print(clothing_item) 
    # print(list(catalog['categories'].keys())[1])
    # print(random.choice(list(catalog['categories']['Clothing'].keys())))

for home_products in list(catalog['items']['Home_kitchen_products'].keys())[:10]:
    # pass
    print(home_products)
    print(list(catalog['categories'].keys())[2])
    print(random.choice(list(catalog['categories']['Home & Kitchen'].keys())))

# cost_price

# selling_price
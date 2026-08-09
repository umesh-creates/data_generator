print('wait...')
import json
import random
import pandas as pd
products = {
    # product_id (pk)
    'products_id' : [f"P_ID{(i+1):02d}" for i in range(50)],
    'product_name': [],
    'category': [],
    'brand': [],
    'cost_price' : [],
    'selling_price' : []
}
print('15%', 'completed ✅')
# product_name 
# category
# brand 
# cost_price
# selling_price
with open('catalog.json') as f:
    catalog = json.load(f)
    
print('30%', 'completed ✅')

count = 0
for electronic_product in catalog['items']['Electronics_products']:
    if count == 20:
        break
    else:
        products['product_name'].append(electronic_product) # product_name
        products['category'].append(list(catalog['categories'].keys())[0]) # category
        brand = random.choice(list(catalog['categories']['Electronics'].keys())) # brand
        products['brand'].append(brand)

        brand_value = catalog['categories']['Electronics'][brand] # brand value
        product_value = catalog['items']['Electronics_products'][electronic_product] # product_value

        selling_price = int(product_value * brand_value) # selling value
        cost_price = int(selling_price/1.2) # cost price
        products['cost_price'].append(cost_price)
        products['selling_price'].append(selling_price)

        count += 1

print('50%', 'completed ✅')

count = 0
for clothing_item in catalog['items']['Clothing_items']:
    if count == 20:
        break
    else:
        products['product_name'].append(clothing_item)
        products['category'].append(list(catalog['categories'].keys())[1])
        brand = random.choice(list(catalog['categories']['Clothing'].keys()))
        products['brand'].append(brand)

        brand_value = catalog['categories']['Clothing'][brand]
        product_value = catalog['items']['Clothing_items'][clothing_item]
        selling_price = int(brand_value * product_value)
        cost_price = int(selling_price/1.2)
        products['cost_price'].append(cost_price)
        products['selling_price'].append(selling_price)

        count += 1
print(print('80%', 'completed ✅'))
count = 0
for home_products in catalog['items']['Home_kitchen_products']:
    if count == 10:
        break
    else:
        products['product_name'].append(home_products) 
        products['category'].append(list(catalog['categories'].keys())[2])
        brand = random.choice(list(catalog['categories']['Home & Kitchen'].keys()))
        products['brand'].append(brand)

        brand_value = catalog['categories']['Home & Kitchen'][brand]
        product_value = catalog['items']['Home_kitchen_products'][home_products]
        selling_price = int(brand_value * product_value)
        cost_price = int(selling_price/1.2)
        products['selling_price'].append(selling_price)
        products['cost_price'].append(cost_price)

        count += 1
print('100%', 'completed ✅')
# import in csv file
pd.DataFrame(products).to_csv('products.csv', index=False)
print('DONE ✅')
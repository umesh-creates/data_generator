print('wait...')
import pandas as pd
import random
'''
order_item_id (PK) 1 to 1000 series
order_id (FK) random between (1 to 1000) {orders}
product_id (FK) random betwenn (1 to 50) {products}
quantity random between (1 to 10)
'''
order_items = {
    'order_item_id' : [f"ORD_ITEM{i:02d}" for i in range(1, 1001)],
    'order_id' : [f"ORD_ID{i:02d}" for i in range(1, 1001)],
    'product_id' : [],
    'quantity' : []
}

for _ in range(1000):
    rand_product_id = random.randrange(1,51)
    order_items['product_id'].append(f"P_ID{rand_product_id:02d}")

for _ in range(1000):
    rand_quantity = random.randrange(1,11)
    order_items['quantity'].append(rand_quantity)

pd.DataFrame(order_items).to_csv('order_items.csv', index=False)
print('DONE ✅')
print('wait...')
import random
from datetime import date, timedelta
import pandas as pd
'''
order_id (PK) 1 to 1000 series
customer_id (FK) random between (1 to 50) {customers}
order_date random between (2025, 1, 1 to 2025, 12, 31) series
payment_mode random between (Cash, Credit card, Debit Card, UPI)
order_status random between [ "Pending", "Confirmed", "Shipped", "Delivered", "Cancelled", "Returned"]
    weights = [5, 10, 15, 60, 7, 3]
'''
orders = {
    'order_id' : [f"ORD_ID{i:02d}" for i in range(1, 1001)],
    'customer_id' : [],
    'order_date' : [],
    'payment_mode' : [],
    'order_status' : []
}
print('10%', 'completed ✅')

for _ in range(1000):
    cust_id = random.randrange(1,51) 
    orders['customer_id'].append(f"cust_id{cust_id:02d}")

print('30%', 'completed ✅')

start_date = date(2025, 1, 1)
end_date = date(2025, 12, 31)
date_range = (end_date - start_date).days

for _ in range(1000):
    days = random.randint(0, date_range)
    random_date = start_date + timedelta(days=days)
    orders['order_date'].append(random_date.strftime('%Y-%m-%d'))

orders['order_date'].sort()

print('50%','completed ✅')

for _ in range(1000):
    rand_payment_mode = random.choice(['Cash', 'Credit card', 'Debit Card', 'UPI'])
    orders['payment_mode'].append(rand_payment_mode)

print('80%','completed ✅')

order_status = [ "Pending", "Confirmed", "Shipped", "Delivered", "Cancelled", "Returned"]
weights = [5, 10, 15, 60, 7, 3]
for _ in range(1000):
    rand_order_status = random.choices(order_status, weights= weights, k=1)[0]
    orders['order_status'].append(rand_order_status)

print('100%', 'completed ✅')

pd.DataFrame(orders).to_csv('orders.csv', index=False)

print('DONE ✅')
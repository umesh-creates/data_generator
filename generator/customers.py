print('wait...')
from faker import Faker
import random
from datetime import date, timedelta
import pandas as pd

customers = {
    'customer_id' : [f"cust_id{i:02d}" for i in range(1, 50+1)], # primary key
    'customer_name' : [],
    'gender' : [],
    'age' : [],
    'city' : [],
    'state' : [],
    'join_date' : []
}
print('10%','completed ✅')
# customer name
fake = Faker('en_IN')
count = 1
while True:
    if count == 51:
        break
    else:
        fake_name = fake.name()
        if fake_name not in customers['customer_name']:
            customers['customer_name'].append(fake_name)
            count += 1
        else:
            continue

print('30%', 'completed ✅')
# gender
gender_categories = ['male', 'female', 'other']
for i in range(50):
    customers['gender'].append(random.choices(gender_categories, weights = [30, 60, 10], k=1)[0])

print('40%', 'completed ✅')
# age
for i in range(50):
    customers['age'].append(random.randrange(13, 81))

print('50%', 'completed ✅')
# city & state
state_city_map = {
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Thane"],
    "Karnataka": ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Agra"]
}

for i in range(50):
    state = random.choice(list(state_city_map.keys()))
    customers['state'].append(state)
    city = random.choice(state_city_map[state])
    customers['city'].append(city)

print('80%', 'completed ✅')
# join_date
start_date = date(2024, 1, 1)
end_date = date(2024, 12, 31)
days_range = (end_date - start_date).days

dates = sorted([start_date + timedelta(days=random.randint(0, days_range)) for _ in range(50)])

for date in dates:
    customers['join_date'].append(date.strftime("%Y-%m-%d"))

print('100%', 'completed ✅')
# insert into csv file
df = pd.DataFrame(customers)
df.to_csv('customers.csv', index=False)
print('done✅')

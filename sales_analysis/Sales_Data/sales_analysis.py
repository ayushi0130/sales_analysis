
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# merging the 12 months sales data into a single CSV file

files = [file for file in os.listdir('./Sales_Data')]
all_months_data = pd.DataFrame()
for file in files:
    df = pd.read_csv('./Sales_Data/'+file)
    all_months_data = pd.concat([all_months_data,df])

all_months_data.to_csv('all_data.csv',index=False)

# Read the updated dataframe

all_data = pd.read_csv('all_data.csv')
print(all_data.head())

#clean the data
nan_df = all_data[all_data.isna().any(axis=1)]
print(nan_df)

all_data = all_data.dropna(how='all')

# find 'or' and delete it
temp_df = all_data[all_data['Order Date'].str[0:2] == 'Or']

all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

# converted column to the correct type

all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

# Add month column

all_data['Month']=all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('Int32')
print(all_data.head())

# Add sales column:

all_data['Sales'] = all_data['Quantity Ordered']*all_data['Price Each']

# Add a city column
def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]

all_data['City'] = all_data['Purchase Address'].apply(lambda x: f'{get_city(x)} ({get_state(x)})')


# 1 what was the best month for sale? how much was earned that month?
result = all_data.groupby('Month').sum()
month = range(1,13)
plt.bar(month,result['Sales'])
plt.xticks(month)
plt.ylabel('sales in USD($)')
plt.xlabel('Month Number')
plt.show()

# 2 what city had the highest no. of sales

result = all_data.groupby('City').sum()
cities = [city for city, df in all_data.groupby('City')]
plt.bar(cities,result['Sales'])
plt.xticks(cities,  rotation = 'vertical', size = 8)
plt.ylabel('sales in USD($)')
plt.xlabel('City')
plt.show()

# 3 what time should we display advertisements to maximize likelihood of customer's buying product?

all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])

all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
print(all_data.head())


hours = [hour for hour, df in all_data.groupby('Hour')]
plt.plot(hours,all_data.groupby(['Hour']).count())
plt.xticks(hours)
plt.xlabel('Hour')
plt.ylabel('Number of orders')
plt.grid()
plt.show()

# 4 what products are most often sold together?

df = all_data[all_data['Order ID'].duplicated(keep=False)]

df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

df = df[['Order ID','Grouped']].drop_duplicates()

from itertools import combinations
from collections import Counter

count = Counter()

for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list,2)))

for key, value in count.most_common(10):
    print(key,value)

# 5 what product sold the most? why do you think it sold the most?

product_group = all_data.groupby('Product')
print(product_group.head(20))
quantity_order = product_group['Quantity Ordered'].sum()

products = [product for product, df in product_group]

plt.bar(products,quantity_order)
plt.ylabel('Quantity Ordered')
plt.xlabel('Product')
plt.xticks(products,rotation = 'vertical', size = 8)
plt.show()

prices = all_data.groupby('Product')['Price Each'].mean()

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products,quantity_order,color = 'g')
ax2.plot(products,prices,'b-')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered',color = 'g')
ax2.set_ylabel('price($)',color = 'b')
ax1.set_xticklabels(products,rotation= 'vertical',size = 8 )

plt.show()
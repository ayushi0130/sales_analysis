import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Diwali_Sales_Data.csv',encoding='unicode escape')
print(df.head())
print(df.shape)
print(df.info())

df.drop(['Status','unnamed1'],axis=1,inplace=True)
df.dropna(inplace=True)
print(df.isnull().sum())

df['Amount'] = df['Amount'].astype('int')
print(df['Amount'].dtypes)

print(df.columns)
# for rename the column name
df.rename(columns={'Marital_Status':'Married'})

# df.describe() will give the summary of all column
print(df.describe())

print(df[['Age','Orders','Amount']].describe())

# Exploatry data analysis (EDA):

# Gender:

ax = sns.countplot(x = 'Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

#  Amount vs Gender :
sales_gen = df.groupby(['Gender'],as_index=False).sum(['Amount']).sort_values(by='Amount',ascending = False)
sns.barplot(x ='Gender',y = 'Amount',data = sales_gen)
plt.show()

#Age:

ax = sns.countplot(data = df,x='Age Group',hue='Gender')

for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# total anount vs Age Group:
sales_age = df.groupby(['Age Group'],as_index=False).sum(['Amount']).sort_values(by = 'Amount',ascending= False)
sns.barplot(x= 'Age Group',y = 'Amount',data= sales_age)
plt.show()

#state:
sales_states = df.groupby(['State'],as_index=False).sum(['Orders']).sort_values(by = 'Orders',ascending= False).head(10)
sns.set_theme(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_states,x='State',y='Orders')
plt.show()

# total ammount/sales from 10 states:
sales_states = df.groupby(['State'],as_index=False).sum(['Amount']).sort_values(by = 'Amount',ascending= False).head(10)
sns.set_theme(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_states,x='State',y='Amount')
plt.show()

#Marital status:

ax = sns.countplot(data=df,x= 'Marital_Status')
sns.set_theme(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

#marital status by amount:

sales_status = df.groupby(['Marital_Status','Gender'],as_index=False).sum(['Amount']).sort_values(by = 'Amount',ascending= False)
sns.set_theme(rc={'figure.figsize':(7,5)})
sns.barplot(data=sales_status,x= 'Marital_Status',y='Amount',hue='Gender')
plt.show()

#Occupation:
sns.set_theme(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data=df,x= 'Occupation')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Amount by Occupation
sales_status = df.groupby(['Occupation'],as_index=False).sum(['Amount']).sort_values(by = 'Amount',ascending= False)
sns.set_theme(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_status,x= 'Occupation',y='Amount')
plt.show()

# Product Category:
sns.set_theme(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data=df,x= 'Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Amount by product category
sales_status = df.groupby(['Product_Category'],as_index=False).sum(['Amount']).sort_values(by = 'Amount',ascending= False)
sns.set_theme(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_status,x= 'Product_Category',y='Amount')
plt.show()

sales_state = df.groupby(['Product_ID'],as_index=False).sum(['Orders']).sort_values(by='Orders',ascending=False).head(10)
sns.set_theme(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state,x= 'Product_ID',y='Orders')
plt.show()

#another method to do the above top 10 products:

# fig1, ax1 = plt.subplots(figsize=(12,7))
# df.groupby(['Product_ID']).sum(['Orders']).nlargest(10,'Orders').sort_values(by='Orders',ascending=False).plot(kind='bar')
# plt.show()
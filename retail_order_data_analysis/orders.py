import pandas as pd
import sqlalchemy as sal

# import csv file and  handling nun values
df = pd.read_csv('orders.csv',na_values=['Not Available', 'unknown'])
df['Ship Mode'].unique()

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')

#Derive new columns discount, sale pricer and profit

df['discount'] = df['list_price']*df['discount_percent']*.01
df['sale_price'] = df['list_price']-df['discount_percent']
df['profit'] = df['sale_price']- df['cost_price']

df['order_date'] = pd.to_datetime(df['order_date'],format ="%Y-%m-%d")

df.drop(columns= ['list_price', 'discount_percent','cost_price'], inplace=True)

engine = sal.creat_engine('mssql://Pankaj\SQLEXPRESS/master?driver=ODBC+Driver+17+FOR+SQL+SERVER')  

conn=engine.connect()

df.to_mysql('df_order', con=conn, index = False, if_exists='Append')

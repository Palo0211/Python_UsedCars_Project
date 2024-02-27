#!/usr/bin/env python
# coding: utf-8

# In[389]:


import pandas as pd


# In[390]:


#import first file

df = pd.read_excel(r'C:\Users\Pawlo\Desktop\Dataanalytics\Logistics_Portfolio_Project\Python project\used_cars_UK.xlsx')
df


# In[391]:


#import second file

df2 = pd.read_excel(r'C:\Users\Pawlo\Desktop\Dataanalytics\Logistics_Portfolio_Project\Python project\used_cars_UK_1.xlsx')
df2


# In[114]:


print(df.columns)


# In[115]:


print(df2.columns)


# In[392]:


#Set column index as main index for future margening columns

df.set_index('Index', inplace=True)
df


# In[393]:


df2.set_index('Index', inplace=True)
df2


# In[394]:


#Merge files based on Index_ID from imported table

df3 = df.merge(df2, how = 'inner', on = 'Index')
df3


# In[395]:


#EDA, checking data type of all collumns

df3.info()


# In[396]:


#EDA, checking NULL values

df3.isnull().sum()


# In[397]:


#EDA, checking unique values

df3.nunique()


# In[398]:


#based on unique values, remove duplicates to not fail with statistics

df3.drop_duplicates()
df3


# In[399]:


#Deleting not useful columns

df3.drop(columns ='Emission')


# In[400]:


#Changing column name  to keep everything in common view

df3.rename(columns={'title': 'Сar_brand'},inplace=True)
df3


# In[275]:


#Checking first 30 rows to clarify if we have to clear datas

df3.head(30)


# In[401]:


#Checking last 30 rows to clarify if we have to clear datas

df3.tail(30)


# In[402]:


#Removing unnecessary elements from the column  data 

df3["Сar_brand"] = df3["Сar_brand"].str.strip("123._/")
df3


# In[403]:


#From the first time all dots were not removed so these was a necessity to use "replace function"

df3["Сar_brand"] = df3["Сar_brand"].str.replace('...', '')
df3


# In[404]:


# Cleaning Mileage(miles) column

df3["Mileage(miles)"] = df3["Mileage(miles)"].replace("[^a-zA-Z0-9]", "", regex=True)
df3


# In[405]:


df3['Seats'] = df3['Seats'].astype(str).str[:-2]
df3


# In[406]:


#Relacing Null values for better visualization

df3['Service history']=df3['Service history'].replace('Null', '')
df3['Previous Owners']=df3['Previous Owners'].replace('Null', '0')
df3['Сar_brand']=df3['Сar_brand'].replace('*','Volvo')

df3


# In[246]:


#Droping empty values

for x in df3.index:
    if df3.loc[x,'Service history']=='':
        df3.drop(x, inplace=True)

df3
        


# In[407]:


#Deleting NaN values 

df3=df3.fillna('')

df3


# In[283]:


result_df=df3[df3['Price']>5000].sort_values(by=['Сar_brand','Fuel type'],ascending = False).head(30)
result_df


# In[408]:


fuel_df = df3[df3['Fuel type'].isin(['Diesel', 'Petrol'])].sort_values(by='Engine', ascending=True).tail(30)
fuel_df


# In[300]:


#Filtering information by Fuel type and Engine type

fuel_df=fuel_df.filter(items=['Car_brand','Fuel type','Engine'])
fuel_df


# In[409]:


df4=df3.set_index('Сar_brand')
df4


# In[410]:


#Group by Body type and their average price

group_by_frame=df3.groupby('Body type')
group_by_frame


# In[413]:


group_by_frame=round(group_by_frame.mean('Price'))
group_by_frame


# In[417]:


#Group by Gearbox and Max Mileage(miles)

group_2=df3.groupby('Gearbox')


# In[418]:


group_2=group_2.max('Mileage(miles)')
group_2


# In[419]:


import os, shutil


# In[420]:


#9) Automatic File Sorter in File Explorer

path = r"C:/Users/Pawlo/Desktop/Dataanalytics/Python_Project/"


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[24]:


#great work! ~Lyndsay


# # Yu, Christopher

# # Lab 1.1

# In[9]:


get_ipython().system('sudo apt-get install python3-mysqldb')
get_ipython().system('sudo pip3 install -U sqlalchemy sql_magic')


# In[8]:


#basic code to connect to a database. 
from sqlalchemy import create_engine

conn_string = 'mysql://{user}:{password}@{host}/{db}?charset={encoding}'.format(
    host = 'db.ipeirotis.org', 
    user = 'student',
    db = 'citibike_fall2017',
    password = 'dwdstudent2015',
    encoding = 'utf8mb4')

engine = create_engine(conn_string)
con = engine.connect()
print(con)


# In[5]:


#An sql query status_fall2017 table)
stations = con.execute("SELECT DISTINCT id, name, capacity, lat, lon  FROM status_fall2017 LIMIT 5")

for s in stations:
    print(s)
    print("-----")


# # Lab 1.12

# In[6]:


#basic code to connect to a database. 
from sqlalchemy import create_engine

conn_string = 'mysql://{user}:{password}@{host}/{db}?charset={encoding}'.format(
    host = '35.245.25.171:3306', 
    user = 'root',
    db = 'techub',
    password = 'dwdstudent2015',
    encoding = 'utf8mb4')

engine = create_engine(conn_string)
con = engine.connect()
print(con)


# # Lab 1.2
# 

# In[20]:


#basic code to connect to a database. 
from sqlalchemy import create_engine

conn_string = 'mysql://{user}:{password}@{host}/{db}?charset={encoding}'.format(
    host = 'db.ipeirotis.org', 
    user = 'student',
    db = 'bike_sharing',
    password = 'dwdstudent2015',
    encoding = 'utf8mb4')

engine = create_engine(conn_string)
con = engine.connect()
print(con)


# In[23]:


jan_users2011 = con.execute("SELECT DISTINCT instant, casual, registered FROM daily WHERE yr = 0 and mnth = 1;")

for s in  jan_users2011:
    print("Jan", s[0], "Casual", s[1], "Registered", s[2])
    print("-----")


# In[ ]:





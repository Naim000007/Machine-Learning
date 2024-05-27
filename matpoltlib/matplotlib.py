#!/usr/bin/env python
# coding: utf-8

# Types of Data
# Numerical Data
# Categorical Data

# In[15]:


# import the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('default')


# In[5]:


# ploting a simple function 
price =[48000, 54000,57000, 49000,47000,45000]
year = [2015,2016,2017,2018,2019,2020]
plt.plot(year, price) #catagorical first 


# In[9]:


batsman = pd.read_csv("sharma-kohli.csv")
batsman


# In[10]:


plt.plot(batsman['index'], batsman["V Kohli"])


# In[11]:


plt.plot(batsman['index'], batsman["RG Sharma"])


# In[16]:


#ploting multiple plots 
plt.plot(batsman['index'], batsman["V Kohli"])
plt.plot(batsman['index'], batsman["RG Sharma"])


# In[18]:


#lables title 
plt.plot(batsman['index'], batsman["V Kohli"])
plt.plot(batsman['index'], batsman["RG Sharma"])
plt.title("Rohit Sharma vs Virat Kohili Career Comparison")
plt.xlabel("season")
plt.ylabel("Runs Scored")


# In[35]:


#colors (hex) and line (width and style) and markert (size)
plt.plot(batsman['index'], batsman["V Kohli"],color="green", linestyle="solid", marker ="D", markersize=10)
plt.plot(batsman['index'], batsman["RG Sharma"], color="red", linestyle="dashed", marker="o", markersize=10)
plt.title("Rohit Sharma vs Virat Kohili Career Comparison")
plt.xlabel("season")
plt.ylabel("Runs Scored")


# In[44]:


#legend -> location 
plt.plot(batsman['index'], batsman["V Kohli"], label="Virat")
plt.plot(batsman['index'], batsman["RG Sharma"], label="Rohit")
plt.title("Rohit Sharma vs Virat Kohili Career Comparison")
plt.xlabel("season")
plt.ylabel("Runs Scored")
plt.legend()
plt.grid()


# In[43]:


#limiting axes 
price =[48000, 54000,57000, 49000,47000,45000,4500000]
year = [2015,2016,2017,2018,2019,2020,2021]
plt.plot(year, price) #catagorical first 
plt.ylim(0,75000)
plt.xlim(2017,2019)


# In[45]:


#show
plt.plot(batsman['index'], batsman["V Kohli"], label="Virat")
plt.plot(batsman['index'], batsman["RG Sharma"], label="Rohit")
plt.title("Rohit Sharma vs Virat Kohili Career Comparison")
plt.xlabel("season")
plt.ylabel("Runs Scored")
plt.legend()
plt.grid()

plt.show()


# In[ ]:


# scatter Plots 
# bivcariate analysis 
# numerical vs numerical 
# use case -> Finding correlation 


# In[50]:


#plt.scatter simple function 
x = np.linspace(-10,10,50)
y = 10*x + 3 + np.random.randint(0,300,50)
y


# In[51]:


plt.scatter(x,y)


# In[55]:


#plt.scatter on pandas data
df = pd.read_csv("batter.csv")
df.head(50)


# In[63]:


plt.scatter(df["avg"], df["strike_rate"])
plt.title("Avg and Sr ANALYSIS Of top 50 batsman")
plt.xlabel("Avarage")
plt.ylabel("Sr")


# In[71]:


#size
tips = sns.load_dataset("tips")
plt.scatter(tips["total_bill"], tips["tip"], s=tips["size"]*20)


# In[73]:


# Bar Chart 
children = [10,20,40,10,30]
color = ["red", "blue", "green", "yellow","pink"]

plt.bar(color, children, color="red")


# In[74]:


plt.barh(color, children, color="red")


# In[ ]:





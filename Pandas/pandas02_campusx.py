#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
# import matplotlib.pyplot as plt

# In[3]:


# Creating a DataFrame 


# In[8]:


#using Lists
student_data = [
    [100, 80,10],
    [90,70, 7],
    [120,100,14],
    [80,50,2]
]
pd.DataFrame(student_data, columns=["iq", "Marks", "Salary"])


# In[42]:


#using dicts 
student_dict = {
    "iq": [100,90,120,80,0,0],
    "Marks": [80,70,100, 50,0,0],
    "Salary": [10,17,14,2,0,0]
}
stundents = pd.DataFrame(student_dict)


# In[13]:


# using read_csv
movies = pd.read_csv("movies.csv")
movies


# In[ ]:


ipl = pd.read_csv("ipl-matches.csv")
ipl


# In[15]:


#shape
movies.shape


# In[16]:


ipl.shape


# In[17]:


#dtypes
movies.dtypes


# In[18]:


#index
movies.index


# In[20]:


#columns 
movies.columns
ipl.columns


# In[23]:


#values
stundents.values
ipl.values


# In[24]:


ipl.head()


# In[25]:


movies.head()


# In[26]:


movies.head(2)


# In[27]:


movies.tail(6)


# In[28]:


#sample -> randomly give a row 
movies.sample(10)


# In[31]:


ipl.sample(5)


# In[32]:


#info -> Info gives high level information of a dataframe
movies.info()


# In[33]:


ipl.info()


# In[34]:


# describe gives a math summery 
movies.describe()


# In[35]:


ipl.describe()


# In[38]:


#isnull -> check null vale ache naki nai , false mane data thik ache ar True mane data missing 
movies.isnull()


# In[39]:


# isnull().sum() -> this tell us missing value in row 
movies.isnull().sum()


# In[40]:


#duplicated  -> it give duplicte value ache naki nai 
movies.duplicated()


# In[46]:


movies.duplicated().sum()


# In[43]:


stundents.duplicated().sum()


# Math Method 

# In[49]:


movies.sum(numeric_only=True)


# In[53]:


stundents.sum()


# In[ ]:





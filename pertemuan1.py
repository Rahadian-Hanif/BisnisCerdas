#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[2]:


sys.version


# In[3]:


import pandas as pd


# In[4]:


import csv


# In[5]:


print (pd.__version__)


# In[6]:


df = pd.read_csv(r'E:\Kuliah\Bisnis Cerdas\tugasPertemuan1.csv')


# In[7]:


df.head()


# In[8]:


df.hist(column='TotalPay', bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)


# In[ ]:





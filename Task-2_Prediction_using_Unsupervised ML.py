#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# Data reading
data=pd.read_csv("Iris.csv")
data


# In[4]:


#Top head records
data.head()


# In[5]:


# last 5 reacords
data.tail()


# In[6]:


# Describing that data
data.describe()


# In[7]:


# Visualizing that data
sns.pairplot(data,hue="Species") #checking the which flower having high and low len


# In[8]:


# Now let's sepparate the data
df=data.values #we are importing the flower data values on one variable df
x=df[:,0:5]
y=df[:,5]

df # so the actual values of the data in this we having 6 columns and 150 rows


# In[9]:


x # x value here i am taking only 5 columns and 150 rows


# In[10]:


y # y value here i am taking it only prints the last varibles in the column


# In[11]:


# Preparing and spliting the data into testing and training
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2) #Here we splitting


# Support Vector Machine

# In[13]:


from sklearn.svm import SVC #importing the support vector machines as svc

# Fitting the training data into the model
model_svc = SVC()
model_svc.fit(x_train,y_train)


# In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
# On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.

# In[14]:


prediction1= model_svc.predict(x_test)
# Now we are going to caluclating the accurace

from sklearn.metrics import accuracy_score
 # from here we are caluclating the accuracy score 
print(accuracy_score(y_test,prediction1)*100)


# In[15]:


# if you want to check manually you can use this form prediction
for i in range(len(prediction1)):
    print(y_test[i],prediction1[i]) #here we can check manually


# In[ ]:





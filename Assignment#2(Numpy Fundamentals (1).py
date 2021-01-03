#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[1]:


import numpy as np
arr1d=np.arange(10)
arr2d=arr1d.reshape(2,5)
arr2d


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[2]:


ones=np.full((2,5),1)
vstack=np.vstack((arr2d,ones))
vstack


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[6]:


hstack=np.hstack((arr2d,ones))
hstack


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[7]:


arr2d.flatten()


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[5]:


array3d=np.arange(15).reshape(3,5)
array3d.flatten()


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[8]:


vector=np.arange(15)
matrix=vector.reshape(5,3)
matrix


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[9]:


array=np.arange(25).reshape(5,5)
square=np.power(array,2)
square


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[15]:


arr=np.random.randint(0,99999,size=(5,6))
meanarr=np.mean(arr)
meanarr


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[16]:


deviation=np.std(arr)
deviation


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[17]:


median=np.median(arr)
median


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[18]:


transpose=np.transpose(arr)
transpose


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[19]:


array1=np.arange(16).reshape(4,4)
diagsum=np.trace(array1)
diagsum


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[20]:


det=np.linalg.det(array1)
det


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[21]:


percentile=np.percentile(array1,(5,90))
percentile


# ## Question:15

# ### How to find if a given array has any null values?

# In[22]:


nan=np.isnan(array1)
nan


# In[ ]:





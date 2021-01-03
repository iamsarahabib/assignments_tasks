#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[6]:


import numpy as np


# 2. Create a null vector of size 10 

# In[7]:


null=np.zeros(10)
null


# 3. Create a vector with values ranging from 10 to 49

# In[8]:


a=np.array(np.arange(10,50))
a


# 4. Find the shape of previous array in question 3

# In[9]:


a.shape


# 5. Print the type of the previous array in question 3

# In[10]:


a.dtype


# 6. Print the numpy version and the configuration
# 

# In[11]:


np.version.version


# 7. Print the dimension of the array in question 3
# 

# In[12]:


a.ndim


# 8. Create a boolean array with all the True values

# In[14]:


array=np.full((2,2),True)
array


# 9. Create a two dimensional array
# 
# 
# 

# In[15]:


array2=np.arange(20).reshape(4,5)
array2


# 10. Create a three dimensional array
# 
# 

# In[16]:


array3=np.arange(30).reshape(3,2,5)
array3


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[17]:


array3[::-1,::-1,::-1]


# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[18]:


null1=np.zeros(10)
null1[4]=1
null1


# 13. Create a 3x3 identity matrix

# In[19]:


np.identity(3)


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[20]:


arr = np.array([1, 2, 3, 4, 5],dtype=np.float64)
arr


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[21]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])  
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
mul=arr1*arr2
mul


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[22]:


arr1+arr2


# 17. Extract all odd numbers from arr with values(0-9)

# In[23]:


arr[arr%2==1]


# 18. Replace all odd numbers to -1 from previous array

# In[24]:


arr[0]=-1
arr[2]=-1
arr[4]=-1
arr


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[25]:


arr = np.arange(10)
arr[5:9]=12
arr


# 20. Create a 2d array with 1 on the border and 0 inside

# In[26]:


arr2d=np.arange(30).reshape(5,6)
arr2d[0]=1
arr2d[::,0:1]=1
arr2d[::,-1]=1
arr2d[4]=1
arr2d[1:4,1:5]=0
arr2d


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[27]:


arr2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
arr2d[1,1]=12
arr2d


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[28]:


arr2d[::]=64
arr2d


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[29]:


array2d=np.array([[0,1,2,3,4],[5,6,7,8,9]])
array2d[0]


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[30]:


array2d=np.array([[0,1,2,3,4],[5,6,7,8,9]])
array2d[1,1]


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[31]:


array2d=np.array([[0,1,2,3,4],[5,6,7,8,9]])
array2d[::,3:4]


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[47]:


random=np.random.randn(10,10)
print(np.max(random))
print(np.min(random))


# In[ ]:


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
---
Find the common items between a and b


# In[33]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[34]:


np.where(np.in1d(a,b))


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[35]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
data[names!='Will']


# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[36]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
data[((names!='Will') & (names!='Joe'))]


# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[37]:


arr2d=np.arange(1,16,dtype=np.float32).reshape(5,3)
arr2d


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[38]:


arr=np.arange(1,17,dtype=np.float32).reshape(2,2,4)
arr


# 33. Swap axes of the array you created in Question 32

# In[39]:


arr.T


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[40]:


array=np.linspace(0,2,10)
sqrt=np.sqrt(array)
print(sqrt)
np.where(sqrt<0.5,0,sqrt)


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[41]:


arr1=np.random.randn(12)
arr2=np.random.randn(12)
maxarr=np.maximum(arr1,arr2)
maxarr


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[42]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
unique=np.unique(names)
unique.sort()
unique


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[43]:


a = np.array([1,2,3,4,5]) 
b = np.array([5,6,7,8,9])
intersect=np.intersect1d(a,b)
print(np.where(a==intersect))
a=np.delete(a,[4])
a


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[44]:


sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = np.array([[10,10,10]])
sampleArray[::,2]=newColumn
sampleArray


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[45]:


x = np.array([[1., 2., 3.], [4., 5., 6.]]) 
y = np.array([[6., 23.], [-1, 7], [8, 9]])
dot=np.dot(x,y)
dot


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[46]:


matrix=np.random.randint(0,100,size=20).reshape(2,10)
print(matrix)
cumsum=np.cumsum(matrix)
cumsum


# In[ ]:





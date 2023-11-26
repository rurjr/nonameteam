#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Array-manipulation-routines" data-toc-modified-id="Array-manipulation-routines-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Array manipulation routines</a></span></li></ul></div>

# # Array manipulation routines

# In[2]:


import numpy as np


# Q1. Let x be a ndarray [10, 10, 3] with all elements set to one. Reshape x so that the size of the second dimension equals 150.

# In[3]:


x = np.ones((10, 10, 3))
y = x.reshape(10, -1, 3)
print(y)


# Q2. Let x be array [[1, 2, 3], [4, 5, 6]]. Convert it to [1 4 2 5 3 6].

# In[4]:


x = np.array([[1, 2, 3], [4, 5, 6]])
y = x.flatten(order='F') 
print(y)


# Q3. Let x be array [[1, 2, 3], [4, 5, 6]]. Get the 5th element.

# In[5]:


x = np.array([[1, 2, 3], [4, 5, 6]])
y = x.flatten()[4]
print(y)


# Q4. Let x be an arbitrary 3-D array of shape (3, 4, 5). Permute the dimensions of x such that the new shape will be (4,3,5).
# 

# In[6]:


x = np.array((3, 4, 5))
x[0]= 4
x[1]
print(x)


# Q5. Let x be an arbitrary 2-D array of shape (3, 4). Permute the dimensions of x such that the new shape will be (4,3).

# In[7]:


x = np.random.rand(3, 4, 5)
x = x.transpose((1, 0, 2))
print(x.shape)


# Q5. Let x be an arbitrary 2-D array of shape (3, 4). Insert a nex axis such that the new shape will be (3, 1, 4).

# In[26]:


#x = np.random.rand(3, 4)
#x = x.transpose((1, 0))
#print(x.shape)


# Q6. Let x be an arbitrary 3-D array of shape (3, 4, 1). Remove a single-dimensional entries such that the new shape will be (3, 4).

# In[9]:


x = np.random.random((3, 4, 1))
y = np.squeeze(x)
print(x.shape)
print( y.shape)


# Q7. Lex x be an array <br/>
# [[ 1 2 3]<br/>
# [ 4 5 6].<br/><br/>
# and y be an array <br/>
# [[ 7 8 9]<br/>
# [10 11 12]].<br/>
# Concatenate x and y so that a new array looks like <br/>[[1, 2, 3, 7, 8, 9], <br/>[4, 5, 6, 10, 11, 12]].
# 

# In[10]:


x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
result = np.concatenate((x, y), axis=1)
print(result)


# Q8. Lex x be an array <br/>
# [[ 1 2 3]<br/>
# [ 4 5 6].<br/><br/>
# and y be an array <br/>
# [[ 7 8 9]<br/>
# [10 11 12]].<br/>
# Concatenate x and y so that a new array looks like <br/>[[ 1  2  3]<br/>
#  [ 4  5  6]<br/>
#  [ 7  8  9]<br/>
#  [10 11 12]]
# 

# In[11]:


x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
result = np.concatenate((x, y), axis=0)
print(result)


# Q8. Let x be an array [1 2 3] and y be [4 5 6]. Convert it to [[1, 4], [2, 5], [3, 6]].

# In[12]:


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
result = np.column_stack((x, y))
print(result)


# Q9. Let x be an array [[1],[2],[3]] and y be [[4], [5], [6]]. Convert x to [[[1, 4]], [[2, 5]], [[3, 6]]].

# In[13]:


x = np.array([[1], [2], [3]])
y = np.array([[4], [5], [6]])
result = np.concatenate((x, y), axis=1)[..., np.newaxis]
print(result)


# Q10. Let x be an array [1, 2, 3, ..., 9]. Split x into 3 arrays, each of which has 4, 2, and 3 elements in the original order.

# In[14]:


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
result = np.split(x, [4, 6])
print(result)


# Q11. Let x be an array<br/>
# [[[  0.,   1.,   2.,   3.],<br/>
#   [  4.,   5.,   6.,   7.]],<br/>
#  
#  [[  8.,   9.,  10.,  11.],<br/>
#   [ 12.,  13.,  14.,  15.]]].<br/>
# Split it into two such that the first array looks like<br/>
# [[[  0.,   1.,   2.],<br/>
#   [  4.,   5.,   6.]],<br/>
#  
#  [[  8.,   9.,  10.],<br/>
#   [ 12.,  13.,  14.]]].<br/>
#   
# and the second one look like:<br/>
#   
# [[[  3.],<br/>
#   [  7.]],<br/>
#  
#  [[  11.],<br/>
#   [ 15.]]].<br/>  

# In[15]:


x = np.array([[[0., 1., 2., 3.], [4., 5., 6., 7.]],
              [[8., 9., 10., 11.], [12., 13., 14., 15.]]])

result = np.split(x, [3], axis=2)
print(result)


# Q12. Let x be an array <br />
# [[  0.,   1.,   2.,   3.],<br>
#  [  4.,   5.,   6.,   7.],<br>
#  [  8.,   9.,  10.,  11.],<br>
#  [ 12.,  13.,  14.,  15.]].<br>
# Split it into two arrays along the second axis.

# In[16]:


x = np.array([[ 0., 1., 2., 3.],
              [ 4., 5., 6., 7.],
              [ 8., 9., 10., 11.],
              [ 12., 13., 14., 15.]])

result = np.split(x, [2], axis=1)
print(result)


# Q13. Let x be an array <br />
# [[  0.,   1.,   2.,   3.],<br>
#  [  4.,   5.,   6.,   7.],<br>
#  [  8.,   9.,  10.,  11.],<br>
#  [ 12.,  13.,  14.,  15.]].<br>
# Split it into two arrays along the first axis.

# In[17]:


x = np.array([[ 0., 1., 2., 3.],
              [ 4., 5., 6., 7.],
              [ 8., 9., 10., 11.],
              [ 12., 13., 14., 15.]])

result = np.split(x, [2], axis=0)
print(result)


# Q14. Let x be an array [0, 1, 2]. Convert it to <br/>
# [[0, 1, 2, 0, 1, 2],<br/>
#  [0, 1, 2, 0, 1, 2]].

# In[39]:


x = np.array([0, 1, 2])
result = np.tile(x, (3, 3, 3))
print(result)


# Q15. Let x be an array [0, 1, 2]. Convert it to <br/>
# [0, 0, 1, 1, 2, 2].

# In[45]:


x = np.array([0, 1, 2])
result = np.tile(x, 2)
n= np.sort(result)
print(n)


# Q16. Let x be an array [0, 0, 0, 1, 2, 3, 0, 2, 1, 0].<br/>
# remove the leading the trailing zeros.

# In[37]:


x = np.array([0, 0, 0, 1, 2, 3, 0, 2, 1, 0])
result = np.trim_zeros(x)
print(result)


# Q17. Let x be an array [2, 2, 1, 5, 4, 5, 1, 2, 3]. Get two arrays of unique elements and their counts.
# 

# In[21]:


x = np.array([2, 2, 1, 5, 4, 5, 1, 2, 3])
unique_elements, counts = np.unique(x, return_counts=True)
print("Unique elements:", unique_elements)
print("Counts:", counts)


# Q18. Lex x be an array <br/>
# [[ 1 2]<br/>
#  [ 3 4].<br/>
# Flip x along the second axis.

# In[22]:


x = np.array([[1, 2], [3, 4]])
result = np.flip(x, axis=1)
print(result)


# Q19. Lex x be an array <br/>
# [[ 1 2]<br/>
#  [ 3 4].<br/>
# Flip x along the first axis.

# In[23]:


x = np.array([[1, 2], [3, 4]])
result = np.flip(x, axis=0)
print(result)


# Q20. Lex x be an array <br/>
# [[ 1 2]<br/>
#  [ 3 4].<br/>
# Rotate x 90 degrees counter-clockwise.

# In[24]:


x = np.array([[1, 2], [3, 4]])
result = np.rot90(x)
print(result)


# Q21 Lex x be an array <br/>
# [[ 1 2 3 4]<br/>
#  [ 5 6 7 8].<br/>
# Shift elements one step to right along the second axis.

# In[25]:


x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
result = np.roll(x, shift=1, axis=1)
print(result)


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Soring,-searching,-and-counting" data-toc-modified-id="Soring,-searching,-and-counting-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Soring, searching, and counting</a></span><ul class="toc-item"><li><span><a href="#Sorting" data-toc-modified-id="Sorting-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Sorting</a></span></li><li><span><a href="#Searching" data-toc-modified-id="Searching-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Searching</a></span></li><li><span><a href="#Counting" data-toc-modified-id="Counting-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Counting</a></span></li></ul></li></ul></div>

# # Soring, searching, and counting

# In[1]:


import numpy as np


# ## Sorting

# Q1. Sort x along the second axis.

# In[3]:


x = np.array([[1,4],[3,1]])
y = np.sort(x, axis=1)
print(y)


# Q2. Sort pairs of surnames and first names and return their indices. (first by surname, then by name).

# In[5]:


surnames =    ('Hertz',    'Galilei', 'Hertz')
first_names = ('Heinrich', 'Galileo', 'Gustav')
indices = np.lexsort((first_names, surnames))
print(indices)


# Q3. Get the indices that would sort x along the second axis.

# In[6]:


x = np.array([[1,4],[3,1]])
y = np.argsort(np.argsort(x, axis=1), axis=1)
print(y)


# Q4. Create an array such that its fifth element would be the same as the element of sorted x, and it divide other elements by their value.

# In[24]:


x = np.random.permutation(10)
sorted_x = np.sort(x)
result = np.empty_like(x, dtype=float)
result[4] = sorted_x[4]  
for i in range(len(x)):
    if i != 4 and x[i] != 0: 
        result[i] = x[i] / x[4]  
print("Original x:", x)
print("Result array:", result)


# Q5. Create the indices of an array such that its third element would be the same as the element of sorted x, and it divide other elements by their value.

# In[10]:


x = np.random.permutation(10)

sorted_indices = np.argsort(x)
indices = np.zeros_like(x)
indices[2] = sorted_indices[2]
for i in range(len(x)):
    if i != 2 and x[i] != 0:  
        indices[i] = i // x[i]
print("Original x:", x)
print("Generated indices:", indices)


# ## Searching

# Q6. Get the maximum and minimum values and their indices of x along the second axis.

# In[11]:


x = np.random.permutation(10).reshape(2, 5)
max_values = np.amax(x, axis=1)
min_values = np.amin(x, axis=1)
argmax_indices = np.argmax(x, axis=1)
argmin_indices = np.argmin(x, axis=1)

print("Array x:")
print(x)
print("Maximum values along axis 1:", max_values)
print("Indices of maximum values:", argmax_indices)
print("Minimum values along axis 1:", min_values)
print("Indices of minimum values:", argmin_indices)



# Q7. Get the maximum and minimum values and their indices of x along the second axis, ignoring NaNs.

# In[13]:


x = np.array([[np.nan, 4], [3, 2]])
max_values = np.nanmax(x, axis=1)
min_values = np.nanmin(x, axis=1)
argmax_indices = np.nanargmax(x, axis=1)
argmin_indices = np.nanargmin(x, axis=1)
print("Array x:")
print(x)
print("Maximum values:", max_values)
print("Indices of maximum:", argmax_indices)
print("Minimum values:", min_values)
print("Indices of minimum:", argmin_indices)


# Q8. Get the values and indices of the elements that are bigger than 2 in x.
# 

# In[16]:


x = np.array([[1, 2, 3], [1, 3, 5]])
y = x > 2
values_greater_than_2 = x[y]
indices = np.nonzero(y)
print("Values bigger than 2 =", values_greater_than_2)
print("Their indices are", indices)


# Q9. Get the indices of the elements that are bigger than 2 in the flattend x.

# In[ ]:





# Q10. Check the elements of x and return 0 if it is less than 0, otherwise the element itself.

# In[20]:


x = np.arange(-5, 4).reshape(3, 3)
result = np.where(x < 0, 0, x)

print(result)


# Q11. Get the indices where elements of y should be inserted to x to maintain order.

# In[22]:


x = [1, 3, 5, 7, 9]
y = [0, 4, 2, 6]
indices = np.searchsorted(x, y)
indices


# ## Counting

# Q12. Get the number of nonzero elements in x.

# In[23]:


x = [[0,1,7,0,0],[3,0,0,2,19]]
nonzero_count = np.count_nonzero(x)
print(nonzero_count)


# In[ ]:





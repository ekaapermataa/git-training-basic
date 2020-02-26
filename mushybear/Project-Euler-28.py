#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Project Euler Problem 28

def g(n):
    s = (n-1) // 2
    return (16*s*s*s + 30*s*s + 26*s + 3) // 3


# In[4]:


n = int(input('Enter an odd side length ≥ 3?'))
print ("Sum of both diagonals for a square spiral with length", n, "=", g(n))


# In[ ]:





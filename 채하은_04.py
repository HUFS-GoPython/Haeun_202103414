#!/usr/bin/env python
# coding: utf-8

# In[6]:


print("세 정수의 최댓값을 구합니다.") 

a = input("1: ") 
b = input("2: ") 
c = input("3: ") 

max = a 

if b > max: 
    max = b 
    
if c > max:
    max = c 
    
print("세 정수의 최댓값은", max, "입니다.")


# In[ ]:





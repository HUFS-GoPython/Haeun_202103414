#!/usr/bin/env python
# coding: utf-8

# In[5]:


tree_hight = int(350)
day_time = int(5)
night = int(2)

if (tree_hight - day_time) % (day_time - night) != 0:
    print(((tree_hight - day_time) // (day_time - night))+2)
else:
    print(((tree_hight - day_time) // (day_time - night))+1)


# In[ ]:





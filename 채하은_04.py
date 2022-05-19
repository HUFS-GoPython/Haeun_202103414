#!/usr/bin/env python
# coding: utf-8

# #### 4. NLTK 임포트하고, text4에서 4자리 단어만 출력하세요.

# In[1]:


from nltk.book import *


# In[3]:


words = set([word for word in text4 if len(word) == 4])
print(words)


# In[ ]:





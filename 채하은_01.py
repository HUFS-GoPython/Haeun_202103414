#!/usr/bin/env python
# coding: utf-8

# #### 1. text5에서 4번 출현하는 단어들을 중복되지 않게 오름차순으로 출력하시오.

# In[19]:


fdist5 = FreqDist(text5) #빈도 분포 함수

#set -> 중복 제거
words = set([word for word in text5 if fdist5[word] == 4 and word.isalpha()])
words = sorted(words) #오름차순 정렬

print(words)


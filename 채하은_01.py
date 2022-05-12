#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 원가
biyott = 480
gimbap = 900
coke = 380
banana = 1050
homerun = 770

# 개수
biyott_number = 3
gimbap_number = 5
coke_number = 6
banana_number = 2
homerun_number = 4

# 소비자가 - 원가 = 이익
biyott_revenue = int(1300 - 480) 
gimbap_revenue = int(2500 - 900) 
coke_revenue = int(800 - 380)
banana_revenue = int(3200 - 1050)
homerun_revenue = int(1500 - 770)

#할인
gimbap_price = int(2500 * 0.85 - 900)
coke_price = int(800 *0.85 - 380)

# 합계
biyott_total = int(biyott_revenue * 3)
gimbap_total = int(gimbap_price * 5)
coke_total = int(coke_price * 6 )
banana_total = int(banana_revenue * 2)
homerun_total = int(homerun_revenue * 4)

total = biyott_total + gimbap_total + coke_total + banana_total + homerun_total


# 총매출
print((f'편의점의 총 매출은 {total}입니다.')) 


# In[ ]:





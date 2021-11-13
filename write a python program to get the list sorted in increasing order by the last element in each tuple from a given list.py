#!/usr/bin/env python
# coding: utf-8

# In[27]:


a=[(2,5),(1,2),(4,4),(2,3),(2,1)]
n=[]
for j in range(1,len(a)):
    for i in range(len(a)-j):
        if a[i][1]>a[i+1][1]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
for i in range(len(a)):
    print(a[i],end="")
print("")    
b=list(a[::])
print(b)

  
    


# In[ ]:





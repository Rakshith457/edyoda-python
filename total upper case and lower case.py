#!/usr/bin/env python
# coding: utf-8

# In[12]:


def string_upper_lower(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    for c in s :
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print(s)
    print("No of Upper case charatcters:",d["UPPER_CASE"])
    print("No of Upper lower charatcters:",d["LOWER_CASE"])
string_upper_lower("The quick Brown Fox")    
    
 


# In[ ]:





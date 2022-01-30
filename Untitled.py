#!/usr/bin/env python
# coding: utf-8

# In[ ]:


i = int(input())
d = 0
t = 1
while i > 0 :
    print(i)
    d = i
    i = i - 1
    t = d * t 
print(t)


# In[3]:


n = int(input('entrer un nombre'))
tabdic = ({})
for i in range(1, n+1):
    if i != 0:
        tabdic.update( {i : i*i} )
print(tabdic)


# In[ ]:


d= []
for i in range(2000, 3001):
    if i % 7 == 0 and i % 5 != 0 :
        d.append(i)
print(d)


# In[9]:


def nomr(a,b):
    chaine = str(input('entrer un mot')) # le mot de type à entrer
    n = int(input('entrer un entier')) # l'index à recuperer
    chaine = list(chaine) #convertion de chaine en liste
    if n>len(chaine):
        print("l'indexe est or plage")
    else:
        del chaine[n] # suppression de la lettre en fonction de l'index recuperer
    str(chaine) #reconvertion de la liste en chaine 
    strchaine = "".join(chaine) #concatenation des la chaine
    print(strchaine)
    nomr(chaine,n)


# In[1]:


import numpy as np
tab = np.array([[0 , 1],[2 , 3],[4 , 5]])

print(tab.tolist())


# In[ ]:


import numpy as np

matrice1 = np.array([0,1,2])
matrice2 = np.array([2,1,0])

covariance = np.cov(matrice1, matrice2)[-1][1]
print(covariance)


# In[ ]:


c = 50
h = 30
d = []
for i in range(3):
    p = float(input("entrez un nombre"))
    d.append(p)
    
from math import *
for i in range(3):
    q = sqrt((2 * c * d[i])/h)
    print(round(q), end = ',')


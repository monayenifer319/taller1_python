#!/usr/bin/env python
# coding: utf-8

# In[95]:


import urllib.request
import pandas as pd
import matplotlib.pyplot as plt


# In[29]:


datos = urllib.request.urlopen('https://colombia.as.com/resultados/futbol/primera/clasificacion/').read()
datos


# In[19]:


pip install beautifulsoup4 


# In[60]:


from bs4 import BeautifulSoup
 
soup = BeautifulSoup(datos)


# In[61]:


equipos = soup.find_all('span', class_='nombre-equipo')


# In[62]:


print (equipos)


# In[66]:


listEquipos = list()
cont = 0
for i in equipos:
    if cont < 20 :
        listEquipos.append(i.text)
    else:
        breack
print(listEquipos, len(listEquipos))


# In[75]:


punt = soup.find_all('td', class_='destacado')
puntos = list()
cont = 0
for i in punt:
    if cont < 20 :
        puntos.append(i.text)
    else:
        breack
print(puntos)


# In[103]:


data = pd.DataFrame(['Nombre' :listEquipos, 'puntos' :puntos], index=list(range(1,21)))
print(data)


# In[ ]:





# In[ ]:





# Diese .py - Datei wurde automatisch aus dem IPython - Notebook (.ipynb) generiert.
# 
# Gelegentlich wurde ich von Teilnehmern gefragt, ob ich die Kursmaterialien nicht 
# auch als normale .py - Datien bereitstellen könne. Dadurch ist es möglich, den Code
# ohne Jupyter zu öffnen, beispielsweise wenn Python-Programme in einem Terminal oder in 
# Eclipse entwickelt werden.
# 
# Dem möchte ich hiermit nachkommen. Ich empfehle dir aber trotzdem, schau' dir lieber die
# IPython - Notebooks direkt an, oder den HTML-Export eben dieser. Dieser reine .py-Export
# ist meiner Meinung nach etwas unübersichtlich.
# 
# Bitte beachte zudem, dass du Pfadangaben ggf. manuell korrigieren musst!
# 
#!/usr/bin/env python
# coding: utf-8

# # PCA zum Visualisieren von Daten
# 
# Datenquelle: https://www.kaggle.com/uciml/human-activity-recognition-with-smartphones/data

# In[2]:


import pandas as pd

df = pd.read_csv("./train.csv.bz2")


# In[3]:


df.head()


# In[9]:


X = df.drop("subject", axis = 1).drop("Activity", axis = 1)
y = df["Activity"]

from sklearn.preprocessing import StandardScaler

s = StandardScaler()
X = s.fit_transform(X)


# In[12]:


from sklearn.decomposition import PCA

p = PCA(n_components = 2)
p.fit(X)

X_transformed = p.transform(X)


# In[15]:



import matplotlib.pyplot as plt

plt.scatter(X_transformed[:, 0], X_transformed[:, 1])
plt.show()


# In[ ]:





# In[ ]:






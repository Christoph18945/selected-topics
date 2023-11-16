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

# In[1]:


import pandas as pd

df = pd.read_csv("./foods.csv")

df.head()


# In[3]:


X = df[["energy_100g", "fat_100g", "carbohydrates_100g", "sugars_100g", "proteins_100g"]].values
y = df["clss"].values


# In[11]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)

from sklearn.preprocessing import StandardScaler

s = StandardScaler()
s.fit(X_train)

X_train = s.transform(X_train)
X_test = s.transform(X_test)


# In[12]:


# One-vs-all: Sklearn hat automatisch erkannt, wir möchten hier
#             mehrere Klassen vorhersagen - daher wird per default
#             die One-vs-all-Methode verwendet. 
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


# In[14]:




# In[13]:


# One-vs-one
from sklearn.multiclass import OneVsOneClassifier

model = OneVsOneClassifier(LogisticRegression())
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


# In[ ]:






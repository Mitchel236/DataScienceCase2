#!/usr/bin/env python
# coding: utf-8

# # Dataset

# ## Library + datasets inladen

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


dfMat = pd.read_csv("student-mat.csv")


# In[3]:


dfPor = pd.read_csv("student-por.csv")


# ## Titel

# In[4]:


st.title("Dataset")
# https://docs.streamlit.io/library/api-reference/text/st.title


# ## Subheadings

# In[5]:


st.subheader('Inleiding dataset en dataframes')
# https://docs.streamlit.io/library/api-reference/text/st.subheader


# In[6]:


body1 = "De dataset Student Alcohol Consumption komt van een survey op school onder wiskunde en Portugese taal studenten. In de dataset zijn meer dan 30 variabelen uiteenlopend van behaalde cijfers tot hoelang de studenten moeten reizen. Er zijn 2 variabelen die gaan over alcohol gebruik, namelijk: Dalc en Walc. Dalc gaat over het alcohol gebruik tijdens werkdagen en Walc gaat over het alcohol gebruikt tijdens weekenden. Het alcohol gebruik wordt hier aangegeven met een schaal van 1 tot 5, het zijn dus numerieke variabelen. Veel van de variabelen in de datasets zijn numerieke variabelen, zoals leeftijd, de opleiding van de ouders en de gezondheid. Er zitten ook een aantal binaire variabelen in de dataset, zoals internet toegang, support van de familie en buitenschoolse aciviteiten."
st.markdown(body1, unsafe_allow_html=False)


# In[7]:


# Kolom structuur maken
col1, col2 = st.columns(2)

# Dataframe weergeven
with col1:
    st.header("Dataframe Wiskunde")
    st.dataframe(dfMat)

with col2:
    st.header("Dataframe Portugee")
    st.dataframe(dfPor)


# In[8]:


st.subheader('Dataset Visualisatie')


# In[9]:


body2 = "Er zitten veel verschillende variabelen in deze dataset, de ene variabele heeft meer relevantie tot alcohol gebruik dan de andere variabele. Wij hebben een selectie gemaakt van de variabelen die naar ons idee het meest relevant zijn. Wij hebben deze variabelen gevisualiseerd om een idee te krijgen over hoe ze eruitzien. Hieronder staan een aantal plots over de variabelen die wij hebben gebruikt. Hierdoor kunnen wij een beter beeld krijgen van de data en de variabelen."
st.markdown(body2, unsafe_allow_html=False)


# In[10]:


dfMatAge = dfMat
dfPorAge = dfPor 

#Mat
dfMatAge = dfMatAge[dfMat.age != 22]
dfMatAge = dfMatAge[dfMat.age != 21]
dfMatAge = dfMatAge[dfMat.age != 20]

#Por
dfPorAge = dfPorAge[dfPor.age != 22]
dfPorAge = dfPorAge[dfPor.age != 21]
dfPorAge = dfPorAge[dfPor.age != 20]


# ### Leeftijd

# In[11]:


st.subheader('Leeftijd')


# In[12]:


check = st.checkbox("Plots zonder 20+ jarige")
if check:
    fig1, axs = plt.subplots(1, 2, constrained_layout = True)
    axs[0].hist(dfMatAge["age"], bins=5)
    axs[0].set_title("Leeftijden Wiskunde studenten")
    axs[0].set_xlabel("Leeftijd")
    axs[0].set_ylabel("Aantal studenten")
    axs[1].hist(dfPorAge["age"], color="g", bins=5)
    axs[1].set_title("Leeftijden Portugees studenten")
    axs[1].set_xlabel("Leeftijd")
    axs[1].set_ylabel("Aantal studenten")
    st.pyplot(fig1)
else:
    fig2, axs = plt.subplots(1, 2, constrained_layout = True)
    axs[0].hist(dfMat["age"],bins=5)
    axs[0].set_title("Leeftijden Wiskunde studenten")
    axs[0].set_xlabel("Leeftijd")
    axs[0].set_ylabel("Aantal studenten")
    axs[1].hist(dfPor["age"], color="g", bins=5)
    axs[1].set_title("Leeftijden Portugees studenten")
    axs[1].set_xlabel("Leeftijd")
    axs[1].set_ylabel("Aantal studenten")
    st.pyplot(fig2)


# ### Drinken score voor Walc en Dalc

# In[13]:


st.subheader('Drinken score voor Walc en Dalc')


# In[14]:


fig3, axs = plt.subplots(2, 2, constrained_layout = True)

axs[0,0].hist(dfMat["Walc"])
axs[0,0].set_title('Wiskunde studenten vs Walc')
axs[0,0].set_xlabel("Walc score")
axs[0,0].set_ylabel("Aantal studenten")

axs[0,1].hist(dfPor["Walc"], color= "g")
axs[0,1].set_title('Portugees studenten vs Walc')
axs[0,1].set_xlabel("Walc score")
axs[0,1].set_ylabel("Aantal studenten")

axs[1,0].hist(dfMat["Dalc"])
axs[1,0].set_title('Wiskunde studenten vs Walc')
axs[1,0].set_xlabel("Dalc score")
axs[1,0].set_ylabel("Aantal studenten")

axs[1,1].hist(dfPor["Dalc"], color= "g")
axs[1,1].set_title('Portugees studenten vs Walc')
axs[1,1].set_xlabel("Dalc score")
axs[1,1].set_ylabel("Aantal studenten")

st.pyplot(fig3)


# ### Geslacht

# In[15]:


st.subheader('Geslacht')


# In[16]:


fig4, axs = plt.subplots(1, 2, constrained_layout = True)

axs[0].hist(dfMat["sex"])
axs[0].set_title('Wiskunde studenten per geslacht')
axs[0].set_xlabel("Geslacht")
axs[0].set_ylabel("Aantal studenten")

axs[1].hist(dfPor["sex"], histtype='bar', color="g")
axs[1].set_title('Portugees studenten per geslacht')
axs[1].set_xlabel("Geslacht")
axs[1].set_ylabel("Aantal studenten")

st.pyplot(fig4)


# ### Eindcijfer

# In[17]:


st.subheader('Eindcijfer')


# In[18]:


fig5, axs = plt.subplots(1, 2, constrained_layout = True)

axs[0].hist(dfMat["G3"])
axs[0].set_title('Cijfers van wiskunde studenten')
axs[0].set_xlabel("Eindcijfer")
axs[0].set_ylabel("Aantal studenten")

axs[1].hist(dfPor["G3"], color="g")
axs[1].set_title('Cijfers van Portugees studenten')
axs[1].set_xlabel("Eindcijfer")
axs[1].set_ylabel("Aantal studenten")

st.pyplot(fig5)


# ### Uitgaan

# In[19]:


st.subheader('Uitgaan')


# In[20]:


fig6, axs = plt.subplots(1, 2, constrained_layout = True)

axs[0].hist(dfMat["goout"], bins =5 )
axs[0].set_title('Uitgaan van wiskunde studenten')
axs[0].set_xlabel("Uitgaans score 1-5")
axs[0].set_ylabel("Aantal studenten")

axs[1].hist(dfPor["goout"], color="g", bins=5)
axs[1].set_title('Uitgaan van Portugees studenten')
axs[1].set_xlabel("Uitgaans score 1-5")
axs[1].set_ylabel("Aantal studenten")

st.pyplot(fig6)


# In[21]:


# code = '''def hi():
#     print("Hier komt een code of plot")'''
# st.code(code, language='python')  
# # https://docs.streamlit.io/library/api-reference/text/st.code


# In[ ]:





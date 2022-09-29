#!/usr/bin/env python
# coding: utf-8

# # Startpagina

# ## Library inladen

# In[1]:


import streamlit as st


# ## Titel

# In[2]:


st.title("Student Alcohol Consumption")  # https://docs.streamlit.io/library/api-reference/text/st.title


# ## Introductie

# In[4]:


body = "In dit blog worden de twee datasets omtrent Student Alcohol Consumption geanalyseerd. Dit is gedaan door middel van berekeningen en visualisaties tussen mogelijke verbanden. De twee datasets zijn Math Student Alcohol Consumption en Portugese Student Alcohol Consumption. Dit blog is gemaakt in Python, en er is gebruik gemaakt van verschillende libraries binnen dit programma. De benoemde datasets komen van Kaggle, hieronder is de link naar de datasets te vinden. Dit blog heeft naast deze pagina, twee pagina’s in de sidebar. In de eerste pagina wordt gekeken naar de datasets in het algemeen, er wordt een analyse gemaakt van de datasets en de belangrijke variabelen binnen deze datasets, dit valt onder het stuk dataverkenning. De tweede pagina bestaat voornamelijk uit visualisaties van mogelijke verbanden, de analyses worden uitgebreid, en er wordt gekeken of er conclusies getrokken kunnen worden tussen verbanden. Dit blog is gemaakt door 4 studenten van de HVA voor de minor Data Science."
st.markdown(body, unsafe_allow_html=False)
# https://docs.streamlit.io/library/api-reference/text/st.markdown


# In[ ]:





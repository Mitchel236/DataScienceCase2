#!/usr/bin/env python
# coding: utf-8

# # Analyse

# ## Library en datasets inladen

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


dfMat = pd.read_csv("student-mat.csv")


# In[3]:


dfPor = pd.read_csv("student-por.csv")


# ## Titel

# In[4]:


st.title("Analyse")
# https://docs.streamlit.io/library/api-reference/text/st.title


# In[5]:


body1 = "Met de beschikbare data over de studenten kunnen we twee dingen bestuderen. Allereerst welke variabelen invloed hebben op de alcoholconsumptie, en ten tweede wat voor invloed alcohol heeft op andere variabelen. Om alles inzichtelijk te maken maken we gebruik van verscheidene plots."
st.markdown(body1, unsafe_allow_html=False)


# ## Subheadings

# In[6]:


st.subheader('Weekend alcohol consumptie per school')


# In[7]:


# Math
fig = go.Figure()

for school in ['GP', 'MS']:    
    dfMatSch = dfMat[dfMat.school == school]    
    fig.add_trace(go.Histogram(x=dfMatSch['Walc'], name=school))

dropdown_buttons = [
{'label': "ALL", 'method': "update", 'args': [{"visible": [True, True]}, {"title": "ALL"}]},
{'label': "GP", 'method': "update", 'args': [{"visible": [True, False]}, {"title": "Gabriel Pereira"}]},
{'label': "MS", 'method': "update", 'args': [{"visible": [False, True]}, {"title": "Mousinho da Silveira"}]},
]

# Update the figure to add dropdown menu
fig.update_layout(
    {'updatemenus': [
    {'active': 0, 'buttons': dropdown_buttons}
    ]})
fig.update_layout(bargap = 0.2)
fig.update_layout({'xaxis': {'title': {'text': 'Weekend alcohol consumptie'}}, 
                  'title': {'text': 'Weekend alcohol consumptie wiskunde studenten'}})

st.plotly_chart(fig)


# In[8]:


# Por
fig = go.Figure()

for school in ['GP', 'MS']:    
    dfPorSch = dfPor[dfPor.school == school]    
    fig.add_trace(go.Histogram(x=dfPorSch['Walc'], name=school))

dropdown_buttons = [
{'label': "ALL", 'method': "update", 'args': [{"visible": [True, True]}, {"title": "ALL"}]},
{'label': "GP", 'method': "update", 'args': [{"visible": [True, False]}, {"title": "Gabriel Pereira"}]},
{'label': "MS", 'method': "update", 'args': [{"visible": [False, True]}, {"title": "Mousinho da Silveira"}]},
]

# Update the figure to add dropdown menu
fig.update_layout(
    {'updatemenus': [
    {'active': 0, 'buttons': dropdown_buttons}
    ]})
fig.update_layout(bargap = 0.2)
fig.update_layout({'xaxis': {'title': {'text': 'Weekend alcohol consumptie'}}, 
                  'title': {'text': 'Weekend alcohol consumptie Portugees studenten'}})
st.plotly_chart(fig)


# In[9]:


st.subheader('Werkdag alcohol consumptie per school')


# In[10]:


# Math
fig = go.Figure()

for school in ['GP', 'MS']:    
    dfMatSch = dfMat[dfMat.school == school]    
    fig.add_trace(go.Histogram(x=dfMatSch['Dalc'], name=school))

dropdown_buttons = [
{'label': "ALL", 'method': "update", 'args': [{"visible": [True, True]}, {"title": "Beide scholen"}]},
{'label': "GP", 'method': "update", 'args': [{"visible": [True, False]}, {"title": "Gabriel Pereira"}]},
{'label': "MS", 'method': "update", 'args': [{"visible": [False, True]}, {"title": "Mousinho da Silveira"}]},
]

# Update the figure to add dropdown menu
fig.update_layout(
    {'updatemenus': [
    {'active': 0, 'buttons': dropdown_buttons}
    ]})
fig.update_layout(bargap = 0.2)
fig.update_layout({'xaxis': {'title': {'text': 'Werkdag alcohol consumptie'}}, 
                  'title': {'text': 'Werkdag alcohol consumptie wiskunde studenten'}})
st.plotly_chart(fig)


# In[11]:


# Por
fig = go.Figure()

for school in ['GP', 'MS']:    
    dfPorSch = dfPor[dfPor.school == school]    
    fig.add_trace(go.Histogram(x=dfPorSch['Dalc'], name=school))

dropdown_buttons = [
{'label': "ALL", 'method': "update", 'args': [{"visible": [True, True]}, {"title": "Beide scholen"}]},
{'label': "GP", 'method': "update", 'args': [{"visible": [True, False]}, {"title": "Gabriel Pereira"}]},
{'label': "MS", 'method': "update", 'args': [{"visible": [False, True]}, {"title": "Mousinho da Silveira"}]},
]

# Update the figure to add dropdown menu
fig.update_layout(
    {'updatemenus': [
    {'active': 0, 'buttons': dropdown_buttons}
    ]})
fig.update_layout(bargap = 0.2)
fig.update_layout({'xaxis': {'title': {'text': 'Werkdag alcohol consumptie'}}, 
                  'title': {'text': 'Werkdag alcohol consumptie Portugees studenten'}})
st.plotly_chart(fig)


# In[12]:


st.subheader('Gemiddelde weekend alcohol consumptie per eindcijfer')


# In[13]:


# nieuwe tabel aanmaken met gemiddeldes, voor zowel de portugese als de wiskunde studenten

dfMatGem = dfMat[['Walc','Dalc','G3']]
dfMatGem = dfMatGem.assign(
    GemG3Walc = lambda x : x.groupby('G3')['Walc'].transform('mean'),
    GemG3Dalc = lambda x : x.groupby('G3')['Dalc'].transform('mean')
    )


# In[14]:


dfPorGem = dfPor[['Walc','Dalc','G3']]
dfPorGem = dfPorGem.assign(
    GemG3Walc = lambda x : x.groupby('G3')['Walc'].transform('mean'),
    GemG3Dalc = lambda x : x.groupby('G3')['Dalc'].transform('mean')
    )


# In[15]:


#Gemiddelde weekend alcohol consumptie per eindcijfer voor wiskunde studenten 

fig = px.scatter(dfMatGem, x="G3", y="GemG3Walc", title='Gemiddelde weekend alcoholconsumptie per eindcijfer  voor wiskunde studenten')

fig.update_layout({'xaxis': {'title': {'text': 'Eindcijfer'}}, 
                   'yaxis': {'title': {'text': 'Gemiddelde weekend alcohol consumptie'}}})


st.plotly_chart(fig)


# In[16]:


#Gemiddelde weekend alcohol consumptie per eindcijfer voor portugese studenten

fig = px.scatter(dfPorGem, x="G3", y="GemG3Walc", title='Gemiddelde weekend alcoholconsumptie per eindcijfer voor Portugees studenten')
fig.update_layout({'xaxis': {'title': {'text': 'Eindcijfer'}}, 
                   'yaxis': {'title': {'text': 'Gemiddelde weekend alcohol consumptie'}}})

st.plotly_chart(fig)


# In[17]:


st.subheader('Gemiddelde werkdag alcohol consumptie per eindcijfer')


# In[18]:


#Gemiddelde werkdag alcohol consumptie per eindcijfer voor wiskunde studenten

fig = px.scatter(dfMatGem, x="G3", y="GemG3Dalc", title='Gemiddelde werkdag alcoholconsumptie per eindcijfer voor wiskunde studenten')

fig.update_layout({'xaxis': {'title': {'text': 'Eindcijfer'}}, 
                   'yaxis': {'title': {'text': 'Gemiddelde werkdag alcohol consumptie'}}})
st.plotly_chart(fig)


# In[19]:


#Gemiddelde werkdag alcohol consumptie per eindcijfer voor portugese studenten

fig = px.scatter(dfPorGem, x="G3", y="GemG3Dalc", title='Gemiddelde werkdag alcoholconsumptie per eindcijfer  voor Portugees studenten')
fig.update_layout({'xaxis': {'title': {'text': 'Eindcijfer'}}, 
                   'yaxis': {'title': {'text': 'Gemiddelde werkdag alcohol consumptie'}}})

st.plotly_chart(fig)


# In[ ]:





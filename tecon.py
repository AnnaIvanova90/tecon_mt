#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st

st.title('Fiber Counter App')

st.subheader('This app is the property of Teсon MT.')


# In[11]:


n = st.number_input('inner diameter, mm')
st.write('The fiber inner diameter is ', n)

L = st.number_input('active lenght, mm')
st.write('The fiber active lenght is ', L)

uploaded_file = st.file_uploader("сhoose a photo", type = 'jpg' )

st.write("""
Please make sure that photo you upload meets the requires.
The photo must be less than 200 MB
""")

st.image(uploaded_file, caption='researched module')


# In[ ]:


import numpy as np
import cv2
from PIL import Image

img = Image.open(uploaded_file)
img = img.save("img.jpg")

image = cv2.imread("img.jpg")


# In[ ]:


image_1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blured = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.adaptiveThreshold(blured, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 50)
Contours, Hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


# In[ ]:


nn = []
for con in Contours:
     area = cv2.contourArea(con)
     if area > 15 and area < 100:
       nn.append(area)
result = len(nn)

S = round(result*n*L*3.14/1000/1000, 2)

fibres = cv2.drawContours(image, Contours, -1, (0, 255, 0), 1)


# In[ ]:


#st.image(count_fibres, caption='counted fibres')
st.image(fibres, caption='found fibres')
st.write('The number of open fibers is', result)
st.write('The active module squre is ', S)


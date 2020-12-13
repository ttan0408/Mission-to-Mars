#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[12]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[13]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[4]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[5]:


#links = browser.find_by_css("a.product-item h3")
#print(links)


# In[6]:


#links[0].click()
#title = browser.find_by_text('Sample').first['href']
#print(title)


# In[7]:


#len(links)


# In[8]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
links = browser.find_by_css("a.product-item h3")
#declare an empty list

for i in range(len(links)):
    #declare an empty list
    hemisphere = {}
    browser.find_by_css("a.product-item h3")[i].click()
    sample_title = browser.find_by_text('Sample').first['href']
    hemisphere['img_url'] = sample_title
    hemisphere['title'] = browser.find_by_css("h2.title").text
    hemisphere_image_urls.append(hemisphere)
    browser.back()


# In[9]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[10]:


# 5. Quit the browser
browser.quit()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[21]:


#get_ipython().system('pip install splinter')


# In[88]:


from bs4 import BeautifulSoup as bs
import requests
import json
from splinter import Browser
import pandas as pd


# In[41]:

def scrape_all(): 
    executable_path = {'executable_path' : 'chromedriver.exe'}
    browser = splinter.Browser('chrome', **executable_path)


# In[61]:


    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html


# In[62]:


    soup = bs(html, 'html.parser')
    print(soup.prettify())


# In[63]:


    content=soup.find("div",class_="content_page")


# In[64]:


    title= content.find_all("div",class_="content_title")
    print(title[0].text.strip())


# In[65]:


    article= soup.find_all("div",class_="article_teaser_body")
    print(article[0].text.strip())


# In[67]:


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html= browser.html


# In[72]:


    soup=bs(html,"html.parser")
    featured_image= soup.find("article", class_="carousel_item")["style"]


# In[83]:


    latter= featured_image.split('/spaceimages/')[1].split("'")[0]


# In[84]:


    former=url.split("?")[0]


# In[85]:


    featured_image_url= former + latter
    featured_image_url


# In[86]:


    facturl= 'https://space-facts.com/mars/'


# In[91]:


    table=pd.read_html(facturl)
    table[0]


# In[92]:


    mars_df = table[0]


# In[93]:


    mars_fact_html = mars_df.to_html(header=False, index=False)
    mars_fact_html


# In[108]:


    url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)


# In[113]:


    hemisphere_image_urls = []

    links = browser.find_by_css("a.product-item h3")
    for item in range(len(links)):
        hemisphere = {}
    
   
        browser.find_by_css("a.product-item h3")[item].click()
    
  
        sample_element = browser.find_link_by_text("Sample").first
        hemisphere["img_url"] = sample_element["href"]
    
    
        hemisphere["title"] = browser.find_by_css("h2.title").text
    
  
        hemisphere_image_urls.append(hemisphere)
    
   
        browser.back()


# In[114]:


    hemisphere_image_urls


# In[ ]:





# In[ ]:




#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import string
import numpy as np
import time
import pandas as pd
df = pd.DataFrame(columns=('bikeNamefind', 'status2','price', 'moreInfo'))
storage = []


def findBikes():
    html_text = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=motorcycle&_sacat=0')
    soup = BeautifulSoup(html_text.content,'lxml')   #lxml parce method
    bikes = soup.find_all('li', class_ ='s-item s-item__pl-on-bottom s-item--watch-at-corner')
    #print(bike)
    for index, bike in enumerate(bikes):

        bikeNamefind = bike.find('h3', class_='s-item__title').text
        if bikeNamefind[0].isdigit() == True:
            #continue
            status = bike.find('div', class_='s-item__subtitle').text
            status2 = bike.find('span', class_='SECONDARY_INFO').text
            price = bike.find('span', class_='s-item__price').text
            moreInfo = bike.div.div.a['href']
            #if status == status2:
            #print([bikeNamefind, status, price])
            df.loc[index] = [bikeNamefind, status2, price, moreInfo]
            #else: 
             #   print([bikeNamefind, status, status2, price])

        else:
            continue
            status = bike.find('div', class_='s-item__subtitle').text
            status2 = bike.find('span', class_='SECONDARY_INFO').text
            price = bike.find('span', class_='s-item__price').text
            #if status == status2:
            #print([bikeNamefind, status, price])
            df.loc[index] = [bikeNamefind, status2, price, moreInfo]
        
                
if __name__ == '__main__':
    while True:
        findBikes()
        time.sleep(100)
        

        #else: 
        #print([bikeNamefind, status, status2, price])

    df.to_csv('test.csv', index = True)

#Inspecting web price


# In[2]:


from bs4 import BeautifulSoup
import requests
import string
import numpy as np
import time
import pandas as pd
df = pd.DataFrame(columns=('bikeName', 'status','price', 'link'))
rowN = 0


def export_csv(df):
    
    df.to_csv('test.csv', index = True)
    
def grab_info(bikes):
    global rowN
    for index, bike in enumerate(bikes):       
        bikeNamefind = bike.find('h3', class_='s-item__title').text
        if bikeNamefind[0].isdigit() == True:
            #continue
            status = bike.find('div', class_='s-item__subtitle').text
            status2 = bike.find('span', class_='SECONDARY_INFO').text
            price = bike.find('span', class_='s-item__price').text
            moreInfo = bike.div.div.a['href']
            row= index+rowN
            print(index)
            df.loc[row] = [bikeNamefind, status2, price, moreInfo]
            #df.loc[index+indexPrev] = [bikeNamefind, status2, price, moreInfo]  

        else:
            #continue
            status = bike.find('div', class_='s-item__subtitle').text
            status2 = bike.find('span', class_='SECONDARY_INFO').text
            price = bike.find('span', class_='s-item__price').text
            moreInfo = bike.div.div.a['href']
            row= index+rowN
            print(index)
            df.loc[row] = [bikeNamefind, status2, price, moreInfo]
    rowN = df.shape[0]



def page(next_page_url):
    html_text = requests.get(next_page_url)
    if html_text.status_code == requests.codes.ok:
        soup = BeautifulSoup(html_text.content,'lxml')   #lxml parce method
        bikes = soup.find_all('li', class_ ='s-item s-item__pl-on-bottom s-item--watch-at-corner')
        grab_info(bikes)
        export_csv(df)
        #print(soup)

        next_page_text = soup.find('ul', class_="srp-results srp-list clearfix").findAll('a')[-3]['type']
        print(next_page_text)
        if next_page_text == 'next':
            next_page_url  = soup.find('ul', class_="srp-results srp-list clearfix").find('nav', class_='pagination').findAll('a')[-1]['href']
            pageNum = (next_page_url)
            page(next_page_url)

page('https://www.ebay.com/sch/i.html?_from=R40&_nkw=motorcycle&_sacat=0&_pgn=1')    
#page('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=motorcycle&_sacat=0')
             
#parse_page('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=motorcycle&_sacat=0')
#print(bikes)
#Inspecting web price


# In[46]:


for i in range(1,10):
    globals()[f"my_variable_{i}"] = i+1
print(my_variable_1)


# In[175]:


page = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=motorcycle&_sacat=0&_pgn=4' 
html_text = requests.get(page)
soup = BeautifulSoup(html_text.content,'html.parser')
bikes = soup.find_all('li', class_ ='s-item s-item__pl-on-bottom s-item--watch-at-corner')
print(soup)


# In[ ]:





import requests,sys,webbrowser,bs4
import urllib
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
chrome_options = Options()  
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

f=open('JJ Food Enfield.csv')
l=f.read()
l=l.split('\n')
out=open('out2.csv','w+')
out.write('Supplier Product Code,Base Price,On-Shelf Price,	Promo Price	,Type of Promo	,R.S.P.	,P.O.R.,Other,,,,Description,Category,SKU,Description2,	Pack Size\n')
for ele in l[1:]:
    try:
        line=ele.split(',')
        print(line[1])    
        driver = webdriver.Chrome(executable_path=r"./chromedriver",chrome_options=chrome_options)
        driver.get("https://www.jjfoodservice.com/search?b=EN-MW&q="+line[1]+"&size=12&sortType=search")
        time.sleep(2)
        r = driver.execute_script("return document.documentElement.outerHTML")
        soup = BeautifulSoup(r,'html.parser')
        dabbe=soup.find_all('div',{'class':'sc-fihHvN esyGev'})
        c=2
        while(len(dabbe)==0):
            print(c)    
            driver = webdriver.Chrome(executable_path=r"./chromedriver",chrome_options=chrome_options)
            driver.get("https://www.jjfoodservice.com/search?b=EN-MW&q="+line[1]+"&size=12&sortType=search")
            time.sleep(c)
            r = driver.execute_script("return document.documentElement.outerHTML")
            soup = BeautifulSoup(r,'html.parser')
            dabbe=soup.find_all('div',{'class':'sc-fihHvN esyGev'})
            if c==10:
                break
            c+=2
        driver.quit()    
        print(len(dabbe))
        promo=''
        description=''
        description2=''  
        category=''
        basePrice=''
        onPrice=''  
        for dabba in dabbe:
            #check for Type of Promo
            offer=dabba.find_all('span',{'class':'sc-ekulBa iUnWbq'})
            if(len(offer)==1):
                promo=offer[0].text
            elif (len(offer)>1):
                print(ele,len(offer))
            #description
            d=dabba.find('h1',{'class':'sc-crNyjn esoVxW'})
            try:
                description=d.text
            except:
                print(d.text)
            try:    
                description2=description.split('-')[-1]
            except:
                print(d)
            #category
            cat=soup.find('label',{'class':'sc-fqCOlO kYvrne'})
            try:
                category=cat.text
            except:
                print(cat)
            #pesa
            p=soup.find_all('div',{'class':'sc-ivVeuv exHQsL'})
            try:
                basePrice=p[1].text.split(':')[1]
            except:
                print(p)
            try:
                onPrice=p[0].text.split(':')[1]
            except:
                print(p)
            #incsv
            out.write(line[1]+','+basePrice+','+onPrice+',,'+promo+',,,,,,,'+description+','+category+',,'+description2+',\n')
    except:
        print('error')










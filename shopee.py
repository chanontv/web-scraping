from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import time
import re
import pandas as pd

#open browser 
driver = webdriver.Chrome(ChromeDriverManager().install())
keyword = 'notebook'
url = f'https://shopee.co.th/search?keyword={keyword}'
driver.get(url)
driver.execute_script('document.body.style.zoom="10%"')
time.sleep(4)

#get source code
html = driver.page_source
data = soup(html,'html.parser')
data = str(data.find_all('script',type='application/ld+json'))
driver.close()

#transform & insert data to list
name = []
productId = []
lowprice = []
highprice = []

for value in (data.split(',"')):
    if re.search("name",value):
        value_x = (str(value.split('":')[1]).replace('"',''))
        name.append(value_x)
    if re.search("productID",value):
        value_x = (str(value.split('":')[1]).replace('"',''))
        productId.append(value_x)
    if re.search('price":',value):
        value_x = (str(value.split('":')[1]).replace('"',''))
        lowprice.append(value_x)
        highprice.append(value_x)
    if re.search("lowPrice",value):
        value_x = (str(value.split('":')[1]).replace('"',''))
        lowprice.append(value_x)
    if re.search("highPrice",value):
        value_x = (str(value.split('":')[1]).replace('"',''))
        highprice.append(value_x)
    
#generate dataframe
df = pd.DataFrame([name[2:],productId,lowprice,highprice]).transpose()
df.columns = ['Title','ProductID','LowPrice','HighPrice']

#save file
df.to_csv('data\shopee_data.csv',index=False)
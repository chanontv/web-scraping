from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup 
import time

#open browser
keyword = 'elonmusk'
url = f'https://twitter.com/{keyword}'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.execute_script('document.body.style.zoom="20%"')
time.sleep(5)
driver.execute_script('window.scrollTo(0,350)','') 
time.sleep(3)

#get source code
html = driver.page_source
data = BeautifulSoup(html,'html.parser')
post = data.find_all('span',{'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
driver.close()

#transform & insert data to list
result_post = []
middot = ''
for i in post:
    if middot == '·':
        result_post.append(i.text)
    middot = i.text

#check result
[print(i) for i in result_post]
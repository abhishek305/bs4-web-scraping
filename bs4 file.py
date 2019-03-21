from bs4 import BeautifulSoup
import requests

source=requests.get('https://medium.com').text

soup =BeautifulSoup(source,'lxml')
article=soup.find_all()   #enter the tag u want to fetch eg find('div') or find_all()
print(article) #mention prettify for a good format

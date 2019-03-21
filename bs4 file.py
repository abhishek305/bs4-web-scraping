from bs4 import BeautifulSoup
import requests

source=requests.get('https://medium.com').text

soup =BeautifulSoup(source,'lxml')
article=soup.find_all()
print(article)

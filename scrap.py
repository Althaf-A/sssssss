import bs4
import requests
res=requests.get('https://en.wikipedia.org/wiki/Django_(web_framework)')
soup=bs4.BeautifulSoup(res.text,'lxml')
x=soup.select('.toc')
# print(x[0].getText())
print(x[0])

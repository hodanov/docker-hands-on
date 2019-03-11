import requests
from lxml.html import fromstring
from pyquery import PyQuery
from bs4 import BeautifulSoup

url = 'https://www.google.com/'

r = requests.get(url)
tree = fromstring(r.content)
print('===============Requests===============')
print(tree.findtext('.//title'))
print('===============Requests===============\n')

pq = PyQuery(url=url)
print('===============PyQuery===============')
print(pq('head title'))
print('===============PyQuery===============\n')

bs = BeautifulSoup(r.content, 'html.parser')
print('===============BeautifulSoup===============')
print(bs.head.title)
print('===============BeautifulSoup===============\n')

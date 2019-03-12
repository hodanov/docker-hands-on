import requests
from pyquery import PyQuery
from bs4 import BeautifulSoup

url = 'https://www.google.com/'
r = requests.get(url)
context = {
    'PyQuery': '',
    'BeautifulSoup': '',
}

pq = PyQuery(r.text)
context['PyQuery'] = pq('head title').text()

bs = BeautifulSoup(r.text, 'html.parser')
context['BeautifulSoup'] = bs.head.title.string

print(context)

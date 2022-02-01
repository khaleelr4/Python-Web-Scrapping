from traceback import print_tb
from turtle import title
import requests
from bs4 import BeautifulSoup

url = 'https://7starhd.com.co'

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent , 'html.parser')
# print(soup.prettify())

# title = soup.find()
# print(title)

anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href' != "#")):
        linkText = link.get("href")
        all_links.add(all_links)
        print(linkText)
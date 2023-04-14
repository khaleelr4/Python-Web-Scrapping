import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'https://7starhdx.com'

page = requests.get(url)
# print(page.ok)

soup = BeautifulSoup(page.content , 'html.parser')
# print(soup.prettify())

content = soup.find_all('div' , class_='thumb col-md-2 col-sm-4 col-xs-6')
movies = list()

for item in content:
    name = item.figure.figcaption.a.p.text
    link = item.figure.figcaption.a.get('href')
    movies.append((name, link))

print(movies)

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '7star movies names'

sheet['A1'] = 'Name movie'
sheet['B1'] = 'Links'

for movie in movies:
    sheet.append(movie)

wb.save('movies_2023.xlsx')
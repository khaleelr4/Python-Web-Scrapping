import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'https://9animetv.to/home'

page = requests.get(url)
# print(page.ok)

soup = BeautifulSoup(page.content , 'html.parser')
# print(soup.prettify())

content = soup.find_all('div' , class_='film-detail')
movies = list()

for item in content:
    name = item.h3.a.text
    link = item.h3.a.get('href')
    movies.append((name, link))

print(movies)

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '9anime movies and shows'

sheet['A1'] = 'Name movie'
sheet['B1'] = 'Links'

for movie in movies:
    sheet.append(movie)

wb.save('anime_movies_2023.xlsx')
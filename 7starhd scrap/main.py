import requests
from bs4 import BeautifulSoup
from Movie import Movie

url = 'https://7starhd.com.co'

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent , 'html.parser')
# print(soup.prettify())

# title = soup.find()
# print(title)

section = soup.find('section', class_="home-wrapper");

movieList = list()

movie_box_list = section.find_all('div', class_='thumb')

for movieObj in movie_box_list:
    figure = movieObj.find('figure');
    figcaption = figure.find('figcaption');

    title = figcaption.find('p').get_text();
    link = figcaption.find('a').get('href');
    img = figure.find('img').get('src');

    # create the movie object
    movieObj = Movie(title, link, img)

    # append that movie object in the movielist
    movieList.append(movieObj)


# Make a seperate class Excel.py

# store the data in the movieList to the excel file



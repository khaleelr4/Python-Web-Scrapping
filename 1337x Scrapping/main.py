import requests
from bs4 import BeautifulSoup
import pandas as pd
import _csv

url = "https://www.1377x.to/popular-movies"

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent , "html.parser")
# print(soup.prettify())

section = soup.find("div" , class_='col-9')
# print(section)
featureList = section.find("div" , class_="featured-list")
# print(featureList)
tablediv = featureList.find("div" , class_="table-list-wrap")
# print(tablediv)
table = tablediv.find("table" , class_="table-list")

tableHead = table.find("thead")
# print(tableHead)
tableBody = table.find("tbody").find_all('tr');
# print(tableHead)
for row in tableBody:
    
    # name, link, seeds adn peers size time
    
    
    data_1 = row.find('td', class_="name");
    data_2 = row.find('td', class_="seeds");
    data_3 = row.find("td" , class_="leeches")
    data_4 = row.find('td', class_="size")
    data_5 = row.find('td', class_="coll-date")
    
    name = None
    link = None
    seeds = None
    leeches = None
    size = None
    timestamp = None

    if data_1 is not None:
        data = data_1.find_all('a')[1];

        name = data.get_text()
        link = data.get('href')

    if data_2 is not None:
        seeds = data_2.get_text()

    if data_3 is not None:
        leeches = data_3.get_text()

    if data_4 is not None:
        size = data_4.get_text()

    if data_5 is not None:
        timestamp = data_5.get_text()
    
    print(f"Name: {name}, Link: {link}, Seeds: {seeds}, Peers: {leeches}, Size: {size}, timestamp: {timestamp}");
  
    dictionary = {'data_1':[data_1] , 'data_2':[data_2] , 'data_3':[data_3] , 'data_4':[data_4] , 'data_5':[data_5]}
    df = pd.DataFrame(dictionary)
    file = df.to_csv('fileneme.csv' , index=False)

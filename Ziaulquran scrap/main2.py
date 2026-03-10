from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

base_url = "https://ziaulquran.com/shop/page/"

data = []
page = 1

while True:

    url = base_url + str(page) + "/"
    print("Opening:", url)

    driver.get(url)
    time.sleep(3)

    products = driver.find_elements(By.CSS_SELECTOR, "li.product")

    # stop if no products
    if len(products) == 0:
        print("Finished scraping")
        break

    for product in products:

        try:
            name = product.find_element(By.CSS_SELECTOR, "h2").text
        except:
            name = ""

        try:
            price = product.find_element(By.CSS_SELECTOR, ".price").text
        except:
            price = ""

        try:
            link = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        except:
            link = ""

        sku = ""

        data.append({
            "name": name,
            "price": price,
            "sku": sku,
            "link": link
        })

    page += 1


driver.quit()

df = pd.DataFrame(data)

print(df)

df.to_csv("books_data.csv", index=False, encoding="utf-8")

print("Saved to books_data.csv")

def get_sku(link):

    driver.get(link)
    time.sleep(2)

    try:
        sku = driver.find_element(By.CSS_SELECTOR, ".sku").text
    except:
        sku = get_sku(link)

    return sku
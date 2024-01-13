from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from time import sleep
import re



file_path = r"C:\Users\Kamil\OneDrive\Inżynieria danych i Data Science\BMW-3-market_analysis_and_price_prediction\data\BMW3_data.csv"


url_site = "https://www.otomoto.pl/osobowe/bmw/seria-3?page="

cars = pd.DataFrame()


pages=110

def get_car_info(car_url):
    response_car = requests.get(car_url)
    soup_car = BeautifulSoup(response_car.text, features='html.parser')
    
    if not soup_car.find("h3", attrs={"class": "offer-title big-text ezl3qpx2 ooa-ebtemw er34gjf0"}):
        return pd.DataFrame()
    
    title = soup_car.find("h3", attrs={"class": "offer-title big-text ezl3qpx2 ooa-ebtemw er34gjf0"}).text
    price = soup_car.find("h3", attrs={"class": "offer-price__number eqdspoq4 ooa-o7wv9s er34gjf0"}).text
    attribute_table =  soup_car.find('div', attrs={"class": "ooa-1gtr7l5 e18eslyg2"})
    
    car_dict = {}
    car_dict['Nazwa'] = title
    car_dict['Cena'] = price
    
    for attribute in soup_car.find_all('div', attrs={"class": "ooa-162vy3d e18eslyg3"}):
        attributes = attribute.find_all(['p', 'a'])
        attribute_name = attributes[0].text
        attribute_value = attributes[1].text
        
        car_dict[attribute_name] = attribute_value
    
    car = pd.DataFrame(car_dict, index=[0])
    return car



    
    

for i in range(1, pages + 1):
    url = url_site + str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    
    car_list = soup.find('div', attrs={"class": "ooa-r53y0q ezh3mkl11"})
    
    for car in car_list.find_all("section", attrs={"class": "ooa-10gfd0w e1oqyyyi1"}):
        link = car.find('a', attrs={'href': re.compile("^https://")}).get("href")
        name = car.find("a").text
        
        if "otomoto.pl" not in link:
            continue
#        print(link)
        car_info = get_car_info(link)
        cars = pd.concat([cars, car_info]) 
    print(i)

cars.to_csv(file_path, index=False)
print('File created')
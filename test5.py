import requests
import csv
from pprint import pprint
from bs4 import BeautifulSoup

def user_url(energie, marque, kms_max, kms_min, prix_max, prix_min, annees_max, annees_min) :
    url_lacentrale = 'https://www.lacentrale.fr/listing?makesModelsCommercialNames=BMW'
    url = url_lacentrale.format(energie_url = energie, marque_url = marque, kms_max_url = kms_max, kms_min_url = kms_min, prix_max_url = prix_max, prix_min_url = prix_min, annees_max_url = annees_max, annees_min_url = annees_min)
    print(url)
    return url

def scrap_listing(url) :
    result = requests.get(url)
    print(result)
    return result.text
    

def format_url():
    url_requests = user_url('dies', 'BMW', '150000', '50000', '150000', '2500', '2016', '2014')
    html_page = scrap_listing(url_requests)

    soup = BeautifulSoup(html_page, 'html.parser')

    #print(soup.prettify())
    cards = soup.find_all('div', 'Vehiculecard_Vehiculecard_cardBody')
    for card in cards :
        brand_car = brand_car.find('div', 'Text_Text_text Vehiculecard_Vehiculecard_title Text_Text_subtitle2')
        brand_car = brand_car.get_text()
        print('brand_car')
        motor_car = motor_car.find('div', 'Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2' )
        motor_car = motor_car.get_text()
        print('motor_car')

        characteristic_list = []
        for characteristic_car in card.find_all('div', 'Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2') :
            characteristic_car = characteristic_car.get_text()
            characteristic_list.append(characteristic_car)
            print(characteristic_car.replace(" ", "").replace("km", '').replace('\xa0', ''))
            car_km_new = characteristic_list[1].replace(" ", "").replace("km", '').replace('\xa0', '')
            


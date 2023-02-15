import requests
import csv
from pprint import pprint
from bs4 import BeautifulSoup

def User_URL(energie, marque, kms_max, kms_min, prix_max, prix_min, annees_max, annees_min) :
    url_lacentrale = 'https://www.lacentrale.fr/listing?energies=ess%2Celec&makesModelsCommercialNames=BMW&mileageMax=150000&mileageMin=50000&priceMax=150000&priceMin=25000&yearMax=2016&yearMin=2014'
    url = url_lacentrale.format(energie_url = energie, marque_url = marque, kms_max_url = kms_max, kms_min_url = kms_min, prix_max_url = prix_max, prix_min_url = prix_min, annees_max_url = annees_max, annees_min_url = annees_min)
    print(url)
    return url

def scrap_listing(url) :
    result = requests.get(url)
    print(result)
    return result.text


URL_request = User_URL('dies', 'BMW', '150000', '50000', '150000', '2500', '2016', '2014')
html_page = scrap_listing(URL_request)

soup = BeautifulSoup(html_page, 'html.parser')

#print(soup.prettify())


for card in soup.find_all('div', 'Vehiculecard_Vehiculecard_cardBody'):
    car_name = card.find('h3')
    car_name_var = car_name.get_text()
    print(car_name_var)
    car_energy = card.find('div', 'Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2')
    car_energy_var = car_energy.get_text()
    print(car_energy_var)


#a = soup.find_all('h3' , class_car_name = 'Text_Text_text Vehiculecard_Vehiculecard_title Text_Text_subtitle2')
#print(a)
#for card in soup.find_all('h3' , class_car_name = 'Text_Text_text Vehiculecard_Vehiculecard_title Text_Text_subtitle2'):
    #print(soup.title)
#b = soup.get_text()
#print(b)
#a = soup.find_all('div', 'Vehiculecard_Vehiculecard_cardBody')
#print('hello')

#pprint(soup.get_text(b))

#for card in soup.find_all('div', 'searchCardContainer'):
    #b = card.get('h3', 'Text_Text_text Vehiculecard_Vehiculecard_title Text_Text_subtitle2')
    #print(soup.get_text(b))
#print(soup.get_text(a))
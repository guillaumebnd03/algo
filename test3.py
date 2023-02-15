import requests
import csv
from pprint import pprint
from bs4 import BeautifulSoup

def User_URL(energie, marque, kms_max, kms_min, prix_max, prix_min, annees_max, annees_min) :
    url_lacentrale = 'https://www.lacentrale.fr/listing?makesModelsCommercialNames=BMW'
    url = url_lacentrale.format(energie_url = energie, marque_url = marque, kms_max_url = kms_max, kms_min_url = kms_min, prix_max_url = prix_max, prix_min_url = prix_min, annees_max_url = annees_max, annees_min_url = annees_min)
    print(url)
    return url

def scrap_listing(url) :
    result = requests.get(url)
    print(result)
    return result.text
    

def format_url():
    URL_request = User_URL('dies', 'BMW', '150000', '50000', '150000', '2500', '2016', '2014')
    html_page = scrap_listing(URL_request)

    soup = BeautifulSoup(html_page, 'html.parser')

    #print(soup.prettify())

    '''for page in range (1, 10+1):
        for card in soup.find_all('div', 'Vehiculecard_Vehiculecard_cardBody'):
            car_name = card.find('h3')
            car_name_var = car_name.get_text()
            print('La marque est', car_name_var)
            car_energy = card.find('div', 'Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2')
            car_energy_var = car_energy.get_text()
            print('L energie utilisée est', car_energy_var)
            car_kms_min = card.find('div','Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2' )
            car_kms_min_var = car_kms_min.get_text()
            print('Le nombres de kilometre est', car_kms_min_var)
            car_price_min = card.find('span','Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2' )
            car_price_min_var = car_price_min.get_text()
            print('Le prix est', car_price_min_var)
            car_annees_max = card.find('div','Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2' )
            car_annees_max_var = car_annees_max.get_text()
            print('L annee de la voiture est', car_annees_max_var)'''

    car_spec_lst = []
    for elem in card.find_all('div', 'Text_Text_text Vehiculecard_Vehicule_characteristicsItems Text_Text_body2'):
        car_spec_var=elem.get_text()
        car_spec_lst.append(car_spec_var)
        print(car_spec_var)



with open("file.csv", "w") as fd :
    csv_writer = csv.writer(fd)
    csv_writer.writerows([['brand', 'model', 'years'],
                            ['ford', 'focus', '2016'],
                            ['bmw', 'serie 3', '2020']])
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

if __name__ == "__main__" :
    format_url()



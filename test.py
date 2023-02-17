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
    url_requests = user_url('dies', 'BMW', '150000', '50000', '100000', '70000', '2020', '2016')
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
            characteristic_list[1] = car_km_new

        price_car = price_car.find('span','Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2' )
        price_car = price_car.get_text()
        price_new = price.replace(' ','').replace('€', '')
        price = price_new
        print(int(price))
        print ("------------------------------")

        csv_script([brand_car, model_car, motor_car, characteristic_list[0], characteristic_list[1], characteristic_list[2], characteristic_list[3], price], csv_writer)

def csv_script(data, csv_writer):

    csv_writer.writerow([data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]])

def error(soup):

    error_info = soup.find('span', 'Text_Text_text Text_Text_headline2')
    error = error_info.get_text()
    error_info = error.replace(' ','').replace('\xa0', '')
    error_info = int(error_info)
    return(error_info)
    
def main():

csv_document = open('file_test.csv', 'w')   
    csv_writer = csv.writer(csv_document)
    csv_writer.writerow(['Brand', 'Model', 'Motor', 'Year', 'mileage', 'Box', 'Energy', 'Price'])
    url_request = user_url('dies', 'BMW', '150000', '50000', 1, '100000', '70000', '2020', '2016')
    html_page = scrap_listing(url_request)
    soup = BeautifulSoup(html_page, 'html.parser')
    error_info = error(soup)
    
    if error_info > 0 :
        for one_page in range (1,11):   
            url_request = user_url('dies', 'BMW', '150000', '50000', str(one_page), '100000', '70000', '2020', '2016')  
            html_page = scrap_listing(url_request)  
            scrap(html_page, csv_writer)
    else:
        print("error 0 annonce")
    csv_document.close()



main()  #code execute


            
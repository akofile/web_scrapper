import requests
from bs4 import BeautifulSoup
import asyncio

def getpage(ax,number):
    name='{}prof.html'.format(ax)
    url = 'http://spravochnik.rosmintrud.ru/professions/{}'.format(number)
    r = requests.get(url)
    with open(name, 'w') as output_file:
      output_file.write(r.text)
    return name

#Должен быть блокирующим
def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    return text


def parse(filename):
    results = []
    text = read_file(filename)

    soup = BeautifulSoup(text, 'lxml')

    name_spec = soup.find('div', {'class': 'profession-head-information'}).find('h1').text
    kod_name_okz_n = soup.find('li', {'class': 'sidebar-item content-info'}, title="Общероссийский классификатор занятий").find_all('p')[1].text
    kod_name_okpdtr_n = soup.find('li', {'class': 'sidebar-item content-info'}, title="Общероссийский классификатор профессий рабочих, должностей служащих и тарифных разрядов").find_all('p')[1].text


    svyazka = soup.find('span', id = 'tooltip_content_fgos').find('span', {'class': 'real-text'}).text

    obl_prof_d = soup.find('div', {'class': 'profession-head-information'}).find('p', {'class': 'profession-head-sign'}, title="Посмотреть подробнее").text






    return obl_prof_d







potok=1

print(parse('1150prof.html'))

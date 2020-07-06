from bs4 import BeautifulSoup
import requests
import codecs
import os

list = [
    'aktau',
    'aktobe',
    'almaty',
    'atyrau',
    'karaganda',
    'kokshetau',
    'kostanay',
    'kyzylorda',
    'nur-sultan',
    'pavlodar',
    'petropavlovsk',
    'semey',
    'taldykorgan',
    'taraz',
    'temirtau',
    'turkestan',
    'uralsk',
    'ustkamenogorsk',
    'shymkent',
    'ekibastuz'
]

lines_seen = set()

for j in list:
    for i in range(1, 9):
        source = requests.get('https://i-teka.kz/' + str(j) + '/spisokaptek?page=' + str(i)).text

        soup =  BeautifulSoup(source, 'lxml')
        address_result = ''
        name_result = ''

        for title, address in zip(soup.find_all("div", class_="title-row"), soup.find_all("div", class_="address")):
            pharma_title = title.a.text
            name_result = pharma_title + ' - '

            pharma_address = address.text 
            address_result = pharma_address + '\n'

            with open('notes.txt', 'a', encoding='utf8') as f: 
                f.write(name_result + " " + address_result)
            name_result = ''
            address_result = ''

with open('notes.txt', 'r', encoding='utf8') as f:
    txt = f.read().replace(' ', '')

with open('notes.txt', 'w', encoding='utf8') as f:
    f.write(txt)

with open('notes.txt', encoding='utf8') as result:
        uniqlines = set(result.readlines())
        with open('notes2.txt', 'w', encoding='utf8') as rmdup:
            rmdup.writelines(set(uniqlines))
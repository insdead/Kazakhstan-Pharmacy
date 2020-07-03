from bs4 import BeautifulSoup
import requests
import codecs

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


for j in list:
    for i in range(1, 9):
        source = requests.get('https://i-teka.kz/' + str(j) + '/spisokaptek?page=' + str(i)).text

        soup =  BeautifulSoup(source, 'lxml')
        result = ''
        _name = ''
        _n = '\n'
        with open('notes2.txt', 'a', encoding='utf8') as f: 
                f.write(_n)

        for article in soup.find_all("div", class_="title-row"):
            name = article.a.text
            _name = name + ' - '
            with open('notes.txt', 'a', encoding='utf8') as f: 
                f.write(_name)
            _name = ''
            

        for article in soup.find_all("div", class_="address"):
            name = article.text
            result = name + '\n'
            with open('notes2.txt', 'a', encoding='utf8') as f: 
                f.write(result)
            result = ''


with open('notes.txt', 'r', encoding='utf8') as f:
    txt = f.read().replace(' ', '')

with open('notes.txt', 'w', encoding='utf8') as f:
    f.write(txt)


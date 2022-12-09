from typing import Dict
import requests
from bs4 import BeautifulSoup

def get_page(url: str) -> str:
    page = requests.get(url)
    return page.content

def get_soup(page):
    return BeautifulSoup(page, 'html.parser')

def next_page():
    while True:
        if table == None:
            return seite[1]
        else:
            continue
        


page = get_page('https://www.resale.info/angebotelink-user.php?myid=29549&user=1&remote=1&inq=1')
soup = get_soup(page)

tables: list = soup.select('div#container table')

table = get_soup(str(tables[1]))
rows = table.select('tr')

del rows[0:5]
del rows[16]

tds: list = soup.select('td')

positions: list[Dict] = []

for row in rows:
    if len(row) == 10:
        tds: list = row.select('td')

        print()

        # id kategorii
        category = (tds[0].get_text())
        print(category)

        # ilość
        quantity = (tds[1].get_text())
        print(quantity)

        # zdjęcie
        photo_cell = get_soup(str(tds[2]))
        photo = photo_cell.select('img')[0]['src']
        print(photo)

        # link i kategoria
        type_cell = get_soup(str(tds[3]))
        link = type_cell.select('a')[0]['href']
        type_of_machinery = type_cell.select('a')[0].get_text()
        print(link)
        print(type_of_machinery)

        # manufaktura
        manufacturer_cell = get_soup(str(tds[4]))
        manufacturer = manufacturer_cell.select('a')[0].get_text()
        print(manufacturer)

        # model
        model_cell = get_soup(str(tds[5]))
        model = model_cell.select('a')[0].get_text()
        print(model)

        # cena
        price = (tds[7].get_text())
        print(price)

        # seller-no
        seller_no = (tds[10].get_text())
        print(seller_no)

        # no
        no = (tds[11].get_text())
        print(no)

        positions.append({
            "category": category,
            "quantity": quantity,
            "photo": photo,
            "link": link,
            "type of machinery": type_of_machinery,
            "manufacturer": manufacturer,
            "model": model,
            "price": price,
            "seller-no": seller_no,
            "no": no
        })

print(positions)




 
from typing import Dict
import requests
from bs4 import BeautifulSoup

def get_page(url: str) -> str:
    page = requests.get(url)
    return page.content

def get_soup(page):
    return BeautifulSoup(page, 'html.parser')


def get_page_table_content(url: str) -> list[Dict]:

    page: str = get_page(url)
    soup = get_soup(page)

    tables: list = soup.select('div#container table')

    table = get_soup(str(tables[2]))
    rows = table.select('tr')

    del rows[0:5]

    tds: list = soup.select('td')

    positions: list[Dict] = []

    for row in rows:
        if len(row) == 10:
            tds: list = row.select('td')

            # id kategorii
            category = (tds[0].get_text())

            # ilość
            quantity = (tds[1].get_text())

            # zdjęcie
            try:
                photo_cell = get_soup(str(tds[2]))
                photo = photo_cell.select('img')[0]['src']
            except IndexError:
                photo = ''

            # link i kategoria
            type_cell = get_soup(str(tds[3]))
            link = type_cell.select('a')[0]['href']
            type_of_machinery = type_cell.select('a')[0].get_text()

            # manufaktura
            manufacturer_cell = get_soup(str(tds[4]))
            manufacturer = manufacturer_cell.select('a')[0].get_text()

            # model
            model_cell = get_soup(str(tds[5]))
            model = model_cell.select('a')[0].get_text()

            # cena
            price = (tds[7].get_text())
            if price == "\u00a0 ":
                price = ""
            else:
                price = (tds[7].get_text())

            # seller-no
            seller_no = (tds[10].get_text())

            # no
            no = (tds[11].get_text())

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

    return positions



 
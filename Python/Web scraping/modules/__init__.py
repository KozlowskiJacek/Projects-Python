from typing import Dict
from .scrapper import get_page_table_content

class ResaleScrapper:

    def __init__(self, user_id: int):
        self.base_link = f"https://www.resale.info/angebotelink-user.php?myid={str(user_id)}&seite="

    def get_offers(self):

        url_counter = 1
        output: list[Dict] = []

        while True:
            url: str = self.base_link + str(url_counter)
            table_content: list[Dict] = get_page_table_content(url)

            if len(table_content) == 0:
                break

            output.extend(table_content)
            url_counter += 1

        return output


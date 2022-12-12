import json
from modules import ResaleScrapper

user_id = 123456

resale_scrapper = ResaleScrapper(user_id)
content = resale_scrapper.get_offers()

with open('output.json', 'w', encoding="utf-8") as file:
    file.write(json.dumps(content))
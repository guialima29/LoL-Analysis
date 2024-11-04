from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup

@dataclass
class System:
    def __init__(self, name):
        page = requests.get(f'https://www.op.gg/champions/{name}/build')
        soup = BeautifulSoup(page.text, 'html.parser')

        info_elements = soup.find_all('div',class_='info-box--left')
        rate_elements = soup.find_all('div', class_='rate-container')

        info = []
        quotes = []

        for info_elements in info_elements:
            cname = info_elements.find('strong').text
            ctier = info_elements.find('div',class_='tier-info').find('span').text

            info.append(
                {
                    'name': cname,
                    'tier': ctier,
                }
            )

        for rate_elements in rate_elements:
            text = rate_elements.find('span').text
            numbers = rate_elements.find('strong').text

            quotes.append(
                {
                    'text': text,
                    'rate': numbers,
                }
            )

        print(f"{info[0]['name']}")
        print(f"{info[0]['tier']}:")
        print()
        for i in range(3):
            for key, value in quotes[i].items():
                print(f"{value}")

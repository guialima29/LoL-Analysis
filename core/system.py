from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup

@dataclass
class System:
    name: str
    info: list = None
    quotes: list = None

    def __post_init__(self):
        page = requests.get(f'https://www.op.gg/champions/{name}/build')
        if page.status_code != 200:
                print(f"Erro ao acessar a página do campeão: Status {page.status_code}")
                self.info, self.quotes = [], []
                return
        soup = BeautifulSoup(page.text, 'html.parser')

        info_elements = soup.find_all('div',class_='info-box--left')
        rate_elements = soup.find_all('div', class_='rate-container')

        self.info = []
        self.quotes = []

        for info_elements in info_elements:
            cname = element.find('strong').text if element.find('strong') else "N/A"
            ctier = element.find('div', class_='tier-info').find('span').text if element.find('div', class_='tier-info') else "N/A"

            self.info.append({"name":cname,"tier":ctier})

        for rate_elements in rate_elements:
            text = element.find('span').text if element.find('span') else "N/A"
            numbers = element.find('strong').text if element.find('strong') else "N/A"

            self.quotes.append({"text":text,"rate":numbers})



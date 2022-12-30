# Provides function that searches through coins that the user
# enters as symbols (Ex. Bitcoin -> BTC)


import requests
from bs4 import BeautifulSoup as BS
from dataclasses import dataclass


@dataclass
class Coin:
    name: str
    price: str


def monitor(lst):
    url = 'https://crypto.com/price'
    page = requests.get(url)
    soup = BS(page.text, 'lxml')
    table = soup.find('table', class_='chakra-table css-1qpk7f7')
    new_lst = []
    for chosen_coin in lst:
        for coin in table.find_all('tr', class_='css-1cxc880'):
            name = coin.find('span', class_='chakra-text css-1jj7b1a').text
            if chosen_coin == name:
                pass
            else:
                continue
            price = coin.find('div', class_='css-b1ilzc').text
            new_lst.append(Coin(name, price))
    return new_lst


def main():
    print(monitor())


if __name__ == '__main__':
    main()
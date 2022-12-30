# Main folder that runs the monitor and sends the webhooks

from user import *
import time
import requests
from bs4 import BeautifulSoup as BS
from dataclasses import dataclass


@dataclass
class Coin:
    name: str
    price: str


def monitor():
    url = 'https://crypto.com/price'
    page = requests.get(url)
    soup = BS(page.text, 'lxml')
    table = soup.find('table', class_='chakra-table css-1qpk7f7')
    new_lst = []
    for coin in table.find_all('tr', class_='css-1cxc880'):
        name = coin.find('span', class_='chakra-text css-1jj7b1a').text
        price = coin.find('div', class_='css-b1ilzc').text
        new_lst.append(Coin(name, price))
    return new_lst


def main():
    get_coin_input()
    while True:
        webhook = 'https://discord.com/api/webhooks/1058247494699589693/CzgWQYevOdZ3dbLnu4Ik1jQqBBbdJ699NbBMEsMyje-t_Am9o8AyUn3U25IeAYo2S-_V'
        lst = monitor()
        sleep = {
            'content': 'Sleeping 2 minutes...'
        }
        requests.post(webhook, data=sleep)
        time.sleep(120)
        new_lst = monitor()
        for coin in lst:
            for coin1 in new_lst:
                if coin1.name == coin.name:
                    if coin1.price != coin.price:
                        data = {
                            'name': coin.name,
                            'content': coin.name + " has changed from " + coin.price + " to " + coin1.price
                        }
                        requests.post(webhook, data=data)
                        print("Webhook sent")


if __name__ == '__main__':
    main()
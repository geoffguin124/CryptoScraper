# Main folder that runs the selected monitor
# and sends the webhooks


import time
import requests
from src import coin_no_input as cni
from src import coin_input as ci
import user as user


def main():
    type_input = input("Enter 1 for all coins and 2 for selecting coins: ")
    webhook = 'WEBHOOK_KEY'
    if type_input == '1':
        hook = {
            'content': 'Starting Monitor...'
        }
        requests.post(webhook, data=hook)
        while True:
            lst = cni.monitor()
            time.sleep(10)
            new_lst = cni.monitor()
            for coin in lst:
                for coin1 in new_lst:
                    if coin1.name == coin.name:
                        if coin1.price != coin.price:
                            data = {
                                'name': coin.name,
                                'content': coin.name + " has changed from " + coin.price + " to " + coin1.price + '.'
                            }
                            requests.post(webhook, data=data)
                            print("Webhook sent")
    if type_input == '2':
        choices = user.get_coin_input()
        string = 'You are monitoring for '
        for choice in choices:
            if choices.index(choice) == len(choices) - 1:
                string = string + choice + '.'
            else:
                string = string + choice + ', '
        hook2 = {
            'content': string,
        }
        hook3 = {
            'content': 'Starting Monitor...'
        }
        requests.post(webhook, data=hook2)
        requests.post(webhook, data=hook3)
        while True:
            lst = ci.monitor(choices)
            time.sleep(10)
            new_lst = ci.monitor(choices)
            for coin in lst:
                for coin1 in new_lst:
                    if coin1.name == coin.name:
                        if coin1.price != coin.price:
                            data = {
                                'name': coin.name,
                                'content': coin.name + " has changed from " + coin.price + " to " + coin1.price + '.'
                            }
                            requests.post(webhook, data=data)
                            print("Webhook sent")
    else:
        hook4 = {
            'content': 'Error: Invalid entry.'
        }
        requests.post(webhook, data=hook4)


if __name__ == '__main__':
    main()

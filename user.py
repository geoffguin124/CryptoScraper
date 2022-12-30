# Gets all the necessary data that the user wants and searches for that data in the website

def get_coin_input():
    coin_lst = []
    coin_input = input("Enter coins you would like to monitor for (Hit enter to stop): ")
    while coin_input != '':
        coin_lst.append(coin_input)
        coin_input = input("Enter coins you would like to monitor for (Hit enter to stop): ")
    return coin_lst

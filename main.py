import requests
from bs4 import BeautifulSoup as bs4
import keyboard
from time import sleep
import os
import random


def scrape():
    os.system('cls')

    url = str(input("Website (e.g.: https://google.com):\n"))

    response = requests.get(url)
    
    statCode = response.status_code

    randNum = random.randint(-10000, 100000000)

    text_file = open(f"output{randNum}.txt", "w+")


    if statCode == 200:
        
        soup = bs4(response.content, 'html.parser')
        links = soup.find_all('a')

        for link in links:
            print(link['href'])
            text_file.write(link['href'] + '\n')
        text_file.close()
        menu()
    else:
        print(f'Failed to retrieve the webpage. Status code: {statCode}')
        menu()

def information():
    os.system('cls')
    print('soon..')
    sleep(1)
    menu()

def menu():
    os.system('cls')
    print("[1] Scrape")
    print("[2] Information")
    print("[Q] Quit")

    isPressed = False
    
    while not isPressed:
        if keyboard.is_pressed("1"):
            isPressed = True
            scrape()
        if keyboard.is_pressed("2"):
            isPressed = True
            information()
        if keyboard.is_pressed("q"):
            quit()
menu()
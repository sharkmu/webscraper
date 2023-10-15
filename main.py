import requests
from bs4 import BeautifulSoup as bs4


url = str(input("Website:\n"))

if "http://" or "https://" not in url:
    url = "http://" + url

try: 
    response = requests.get(url)
    statCode = response.status_code

    if statCode == 200:
        soup = bs4(response.content, 'html.parser')
        links = soup.find_all('a')

        for link in links:
            print(link['href'])
    else:
        print(f'Failed to retrieve the webpage. Status code: {statCode}')
except:
    print(f"Failed to request the given URL: {url}")
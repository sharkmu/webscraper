import requests
from bs4 import BeautifulSoup as bs4


url = str(input("Website:\n"))

if "http://" or "https://" not in url:
    url = "http://" + url

try: 
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using Beautiful Soup
        soup = bs4(response.content, 'html.parser')

        # Find all the anchor tags (links)
        links = soup.find_all('a')

        # Print the links
        for link in links:
            print(link['href'])
    else:
        print('Failed to retrieve the webpage.')
except:
    print(f"Failed to request the given URL: {url}")
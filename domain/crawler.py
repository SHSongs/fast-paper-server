import requests
from bs4 import BeautifulSoup

url = 'https://github.com/SHSongs/fast-paper'

response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
else:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    box = soup.find("div", class_="Box mb-3")
    box = box.find("div", role="grid")

    for i in box.find_all("div", role="row"):
        a = i.find("a")
        if a is None:
            continue
        print(a["href"])
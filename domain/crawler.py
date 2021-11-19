import requests
from bs4 import BeautifulSoup

BASE_URL = "https://github.com"


def get_box(prev_url, url):
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
            ref = a["href"]
            if prev_url != BASE_URL + ref and not ref.endswith('.md'):
                print(ref)
                get_box(url, BASE_URL + ref)
            elif ref.endswith('.md'):
                print(ref)


url = 'https://github.com/SHSongs/fast-paper'
get_box(url, url)

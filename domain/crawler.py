import requests
from bs4 import BeautifulSoup
from utils.data_structures import Node
import json

BASE_URL = "https://github.com"


def get_box(prev_url, url, node):
    response = requests.get(BASE_URL + url)

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
            if prev_url != ref and not ref.endswith('.md'):
                print(ref)

                tree[prev_url].append({ref: []})
                child = Node(ref)
                node.children.append(child)
                get_box(url, ref, child)

            elif url != start_url and ref.endswith('.md'):
                child = Node(ref)
                node.children.append(child)

                tree[start_url][-1][url].append(ref)
                print(ref)


start_url = '/SHSongs/fast-paper'
tree = {start_url: []}
root = Node(start_url)

get_box(start_url, start_url, root)
print(tree)

print("\n\n")

j = json.dumps(tree, indent=4, sort_keys=True)
print(j)



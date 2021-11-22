import requests
from bs4 import BeautifulSoup
from utils.data_structures import Node

BASE_URL = "https://github.com"


def make_file_tree(prev_url, url, node):
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
                child = Node(ref)
                node.children.append(child)
                make_file_tree(url, ref, child)

            elif url != start_url and ref.endswith('.md'):
                child = Node(ref)
                node.children.append(child)
                print(ref)


def get_table(url):
    response = requests.get(BASE_URL + url)

    if response.status_code != 200:
        print(response.status_code)
    else:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        try:
            tag_table = soup.find("table")
            return [i.text for i in tag_table.find("tbody").findAll("tr")]
        except:
            print("tag 없음")

        return None


def dfs(node):
    if len(node.children) == 0:
        print(node.data)
        tag = get_table(node.data)
        print(tag)
    for i in node.children:
        dfs(i)


start_url = '/SHSongs/fast-paper'
root = Node(start_url)

make_file_tree(start_url, start_url, root)

print("\n\n")


dfs(root)

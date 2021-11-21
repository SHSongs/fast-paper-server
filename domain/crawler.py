import requests
from bs4 import BeautifulSoup
from utils.data_structures import Node
import json

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

                tree[prev_url].append({ref: []})
                child = Node(ref)
                node.children.append(child)
                make_file_tree(url, ref, child)

            elif url != start_url and ref.endswith('.md'):
                child = Node(ref)
                node.children.append(child)

                tree[start_url][-1][url].append(ref)
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
            print(tag_table.find("thead").find("tr").find("th").text)
            print(tag_table.find("tbody").findAll("tr"))
        except:
            print("tag 없음")
        finally:
            print("\n")


def dfs(node):
    print(node.data)
    if len(node.children) == 0:
        get_table(node.data)
    for i in node.children:
        dfs(i)


start_url = '/SHSongs/fast-paper'
tree = {start_url: []}
root = Node(start_url)

make_file_tree(start_url, start_url, root)
print(tree)

print("\n\n")

j = json.dumps(tree, indent=4, sort_keys=True)
print(j)

dfs(root)

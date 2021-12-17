from typing import List
import requests
from bs4 import BeautifulSoup
from utils.data_structures import Node
import pickle

BASE_URL = "https://github.com"

from dataclasses import dataclass, field
from datetime import date
from typing import List


@dataclass(unsafe_hash=True)
class Board:
    name: str
    category: str
    tags: List[str] = field(default_factory=List)


def make_file_tree(prev_url, url, node, start_url):
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
                make_file_tree(url, ref, child, start_url)

            elif url != start_url and ref.endswith('.md'):
                child = Node(ref)
                node.children.append(child)
                print(ref)


def get_table(url, boards):
    response = requests.get(BASE_URL + url)

    if response.status_code != 200:
        print(response.status_code)
    else:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        try:
            tag_table = soup.find("table")
            return [i.text.strip('\n') for i in tag_table.find("tbody").findAll("tr")]
        except:
            print("tag 없음")

        return []


def dfs(node, boards):
    if len(node.children) == 0:
        tag = get_table(node.data, boards)
        print(tag)
        boards.append(Board(name=node.data, category="", tags=tag))
    for i in node.children:
        dfs(i, boards)


def get_info(dummy_data=False) -> List[Board]:
    if dummy_data:
        print("더미 데이터를 가져옵니다.")
        try:
            with open('boards.pickle', 'rb') as f:
                return pickle.load(f)
        except:
            print("load error 발생, 크롤링을 진행합니다.")

    start_url = '/SHSongs/fast-paper'
    root = Node(start_url)
    make_file_tree(start_url, start_url, root, start_url)

    boards = []
    dfs(root, boards)

    # save
    with open('boards.pickle', 'wb') as f:
        pickle.dump(boards, f, pickle.HIGHEST_PROTOCOL)

    return boards

# b: List[Board] = get_info()

from bs4 import BeautifulSoup
import lxml
import request

with open(r"blank/index.html", encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
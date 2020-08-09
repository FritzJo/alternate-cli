from bs4 import BeautifulSoup
import requests

from data.article import Article


def search(query):
    url = "https://www.alternate.de/html/search.html?query=" + query + "&x=0&y=0"

    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")



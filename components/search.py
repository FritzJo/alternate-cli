from bs4 import BeautifulSoup
import requests
import re

from data.article import Article


def search(query):
    url = "https://www.alternate.de/html/search.html?query=" + query + "&x=0&y=0"

    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    results = soup.findAll("a", {"class": "productLink"})
    for result in results:
        result = result.get("href")
        # Parse article id from href
        articleid = re.findall(r'[0-9]*\?', result)[0][:-1]
        print(articleid)

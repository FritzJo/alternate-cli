from bs4 import BeautifulSoup
import requests


class Article:
    def __init__(self, article_id):
        self.id = article_id
        self.name = ""
        self.price = 0.0
        self.stockStatus = ""
        self.update()

    def update(self):
        url = "https://www.alternate.de/html/product/" + self.id
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        self.name = soup.find("meta", {"property": "og:title"}).get("content")
        self.price = float(soup.find("div", {"class": "price"}).get("data-standard-price"))
        # Status: available_stock, preoder,
        self.stockStatus = soup.find("p", {"class": "stockStatus"}).get("class")[1]

    def is_available(self):
        return self.stockStatus == "available_stock"

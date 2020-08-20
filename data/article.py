from bs4 import BeautifulSoup
import requests

from data.review import Review


class Article:
    def __init__(self, article_id, name="", price=0.0, stockStatus=""):
        self.id = article_id
        self.name = name
        self.price = price
        self.stockStatus = stockStatus
        self.update()

    def update(self):
        url = "https://www.alternate.de/html/product/" + self.get_id()
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        self.name = soup.find("meta", {"property": "og:title"}).get("content")
        self.price = float(soup.find("div", {"class": "price"}).get("data-standard-price"))
        # Status: available_stock, preoder,
        self.stockStatus = soup.find("p", {"class": "stockStatus"}).get("class")[1]

    def get_name(self):
        if self.name == "":
            update()
        return self.name

    def get_price(self):
        if self.price == 0.0:
            update()
        return self.price
        
    def get_id(self):
        return self.id

    def is_available(self):
        if self.stockStatus == "":
            update()
        return self.stockStatus == "available_stock"

    def get_reviews(self, page):
        url = "https://www.alternate.de/html/productRatings/" + self.get_id() + "?page=" + str(page)
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        reviews = []
        for reviewHTML in soup.findAll("div", {"class": "rating"}):
            rating = int(reviewHTML.find("var", {"itemprop": "ratingValue"}).text)
            try:
                user = reviewHTML.find("span", {"itemprop": "name"}).findAll("strong")[1].text[4:]
            except:
                # Some reviews have a slightly different format...
                user = reviewHTML.find("strong", {"itemprop": "name"}).text[14:]
            date = reviewHTML.find("strong", {"itemprop": "dateCreated"}).text
            text = reviewHTML.find("div", {"class": "ratingText"}).text
            reviews.append(Review(text, user, rating, date))
        return reviews

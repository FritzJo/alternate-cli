from bs4 import BeautifulSoup
import requests

from data.article import Article


def get_details(articleIds, campaignId):
    url = "https://www.alternate.de/html/product/information/details/productCampaign.json?"

    for articleId in articleIds:
        url += "&keys=" + articleId + "_" + campaignId
    r = requests.get(url)
    alternate_json = r.json()

    for campaign in alternate_json['campaigns']:
        print(campaign['articleId'])


def get_deals():
    url = "https://www.alternate.de/TagesDeals"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text
    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    deals = []
    #print(soup.findAll("div", {"class": "product"}))
    for link in soup.findAll("div", {"class": "product"}):
        productId = link.find("var").text
        productName = link.find("span", {"class": "productName"}).text
        productPrice = float(link.find("span", {"class": "price"}).text[2:-1].replace(",","."))
        deals.append(Article(productId, productName, productPrice))
    return deals

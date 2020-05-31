import sys

from components.deals import get_deals
from data.article import Article

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Missing args")
        exit(1)

    # Lists current deals
    if sys.argv[1] == "deals":
        for item in get_deals():
            print(item.id + ": " + item.name + " - " + str(item.price) + "€")

    # Lookup products based on their id
    if sys.argv[1] == "lookup":
        item = Article(sys.argv[2])
        print(item.id + ": " + item.name + " - " + str(item.price) + "€")

    # Show reviews for a given article
    if sys.argv[1] == "reviews":
        item = Article(sys.argv[2])
        for r in item.get_reviews(1):
            print(str(r.rating) + " by " + r.user + " (" + r.date + ") : " + r.text[:50])

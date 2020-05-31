import sys

from components.deals import get_deals

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Missing args")
        exit(1)
    if sys.argv[1] == "deals":
        get_deals()

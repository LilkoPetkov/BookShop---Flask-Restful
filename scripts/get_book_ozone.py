import requests
from bs4 import BeautifulSoup


class FindAndAddBook:
    BOOK_INFO = {}
    BOOK_DETAILS = {}

    def __init__(self, url):
        self.result = requests.get(url)
        self.doc = BeautifulSoup(self.result.text, "html.parser")

    def get_book_values(self):
        ul = self.doc.find("ul", {"class": "attribute-list"})
        children = ul.findChildren("li", recurisve=False)

        for li in children:
            category = li.findChildren()[0].string[:-1]
            values = li.findChildren()[1:]

            self.BOOK_INFO[category] = []

            for val in values:
                val = val.string

                if val is not None:
                    if category not in self.BOOK_INFO.keys():
                        self.BOOK_INFO[category] = [val.strip()]
                    else:
                        self.BOOK_INFO[category].append(val.strip())

        main_price = self.doc.find_all("span", {"class": "price"})
        price = main_price[2]
        pr = ""

        for p in price:
            pr += str(p.string.strip())

        pr = pr.replace(",", ".")
        self.BOOK_INFO["price"] = pr
        self.BOOK_INFO["price"] = pr[:-3]
        self.BOOK_INFO["Автор"] = ", ".join(self.BOOK_INFO["Автор"])

        # Get Title
        book_title = self.doc.find("h1", {"itemprop": "name"})
        self.BOOK_INFO["title"] = book_title.string

        # Get Description
        book_desc = self.doc.find("div", {"class": "short-description"}).findChildren()[0]
        self.BOOK_INFO["description"] = book_desc.string

        # Convert / Translate the strings
        self.BOOK_DETAILS["author"] = self.BOOK_INFO["Автор"]
        self.BOOK_DETAILS["price"] = float(self.BOOK_INFO["price"])
        self.BOOK_DETAILS["title"] = self.BOOK_INFO["title"]
        self.BOOK_DETAILS["description"] = self.BOOK_INFO["description"]

        return self.BOOK_DETAILS

    def add_book(self):
        data = self.get_book_values()
        end_point = "http://127.0.0.1:5000/books"
        header = {"Authorization": "Bearer $TOKEN"}
        response = requests.post(end_point, headers=header, json=data)

        return response.text


url = "https://www.ozone.bg/product/taynata-na-patsienta/"
FBook = FindAndAddBook(url)

print(FBook.add_book())

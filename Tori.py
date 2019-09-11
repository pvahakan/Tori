import requests
from bs4 import BeautifulSoup

class Tori:
    def __init__(self, keyword="", category="", location=""):
        self.keyword = keyword
        self.category = category
        self.location = location

    def __str__(self):
        return self.keyword + " " + " " + self.category + " " + " " + self.location


    def find_category_codes(self, PRINT=False):
        """
        Finds category HTML-<option> value by its name.

        Param category: string, name of category.
        Param PRINT: Boolean, handles printing of all gategory names and codes.

        Returns code of category and None if category not found.
        """
        url = "https://www.tori.fi/"
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        category_input = soup.find_all('select', id='catgroup') # kategoria

        for c in category_input:
            for i in c.find_all('option'):
                # Prints all categories and codes
                if PRINT == True:
                    print('{:50} {:>8}'.format(i.get_text(), i['value']))

                elif self.category.upper() == i.get_text().upper():
                    return i['value']

        return None

import unittest
import requests
import bs4
import difflib

class TestBeautifulSoup(unittest.TestCase):
    def test_beautiful_soup(self):
        r = requests.get('http://www.python.org')
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        print(soup.title)
        print(soup.prettify())

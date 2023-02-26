import bs4
import requests


# take html from python website and save it to a file
def create_example_html():
    r = requests.get('http://www.python.org')
    with open('../test/resources/python.html', 'w', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        f.write(soup.prettify())


if __name__ == '__main__':
    create_example_html()



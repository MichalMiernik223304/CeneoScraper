from urllib import response
import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/66893958#tab=reviews"
response = requests.get(url)
page_dom = BeautifulSoup(response.text, 'html.parser')

print(page_dom.prettify())
"""Script to gather recipes from Good and Cheap."""
import sys
import requests
from bs4 import BeautifulSoup
import csv
import json

index_URL = "https://www.leannebrown.com/index/"

index_page = requests.get(index_URL)
index_soup = BeautifulSoup(index_page.content, 'html.parser')

for a in index_soup.find_all('a', href=True):
    if (a['href']).startswith("https://www.leannebrown.com/"):
        print (a['href'])

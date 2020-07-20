import requests
import re
import json
from bs4 import BeautifulSoup

corpus = open("corpus.txt", "w")

with open('stopwords-it.json', 'r') as f:
    stopwords_lst = f.read()
with open('url_lst.json', 'r') as d:
    data = json.load(d)

def print_article(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        article = soup.find('span', {'id':'article-body'}).text
    except AttributeError:
        article = soup.find('article').text
    for word in re.findall(r'\w+', article.lower()):
        if word not in stopwords_lst and len(word) > 3:
            corpus.write(word + ' ')

for url in data:
    print_article(url)

corpus.close()
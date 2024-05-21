# Thanks to https://opensource.com/article/21/9/web-scraping-python-beautiful-soup
import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://cse.hkust.edu.hk/'
data = requests.get(url)

my_data = []

html = BeautifulSoup(data.text, 'html.parser')
articles = html.select('a.post-card')
max_time = 30

i=0

for article in articles:

    title = article.select('.card-title')[0].get_text()
    excerpt = article.select('.card-text')[0].get_text()
    pub_date = article.select('.card-footer small')[0].get_text()

    my_data.append({"title": title, "excerpt": excerpt, "pub_date": pub_date})
    if i >= max_time:
        break
    i+=1

pprint(my_data)
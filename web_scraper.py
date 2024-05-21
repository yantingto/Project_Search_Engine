# Thanks to https://opensource.com/article/21/9/web-scraping-python-beautiful-soup
import requests
from bs4 import BeautifulSoup

url = 'https://cse.hkust.edu.hk/'
data = requests.get(url)
max_number = 30

links = []

html = BeautifulSoup(data.text, 'html.parser')
all_links = html.find_all('a')

i=0
for link in all_links:
    href = link.get('href')
    title = link.get('title') or link.text.strip()
    links.append({"href": href, "title": title})
    if i>=max_number:
        break
    i+=1

print(links)
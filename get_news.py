import re
import requests
from bs4 import BeautifulSoup

def get_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                             'AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/57.0.2987.98 Safari/537.36'}
    res = requests.get(url, headers=headers)
    news_soup = BeautifulSoup(res.text, 'html.parser')
    targets = news_soup.find_all("div", class_="news_title")

    title = []
    for each in targets:
         title.append(each.a.text())

    print(title)
def main():
    url = "https://news.163.com/"
    get_url(url)

if __name__=="__main__":
    main()


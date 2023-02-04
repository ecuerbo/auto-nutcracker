import requests
from bs4 import BeautifulSoup as bs
import random

def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )

    soup = bs(response.content,'html.parser')

    title = soup.find(id='firstHeading')
    print(title.text)

    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        #we are only interested in otehr wiki articles
        if link['href'].find("/wiki/")==-1:
            continue
        #use this link to scrape
        linkToScrape = link
        break

    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")
import requests
from bs4 import BeautifulSoup as bs
import random

response = requests.get(
	url="https://en.wikipedia.org/wiki/Web_scraping",
)
soup = bs(response.content,'html.parser')

title = soup.find(id='firstHeading')
print(title.content)

#get all the links
allLinks = soup.find(id='bodyContent').find_all("a")
random.shuffle(allLinks)
linktoScrape = 0

for link in allLinks:
    #we are only interested in other wiki articles
    if link['href'].find("/wiki/") == -1:
        continue
    #use this link to scrape
    linkToScrape = link
    break
print(linkToScrape)
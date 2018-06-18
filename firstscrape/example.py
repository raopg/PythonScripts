#import requests
#The first scrape is going to be on a downloaded HTML document.
from bs4 import BeautifulSoup

def makeSoup(htmlFile = "BarberShopResults.htm") ->"SoupType":
	markupContents = open(htmlFile,'r')
	soup = BeautifulSoup(markupContents, "html.parser")
	return soup
if __name__ == "__main__":
	madeSoup = makeSoup()
	print(madeSoup.prettify())





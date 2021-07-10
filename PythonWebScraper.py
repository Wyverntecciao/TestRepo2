print ("Starting"); #starting message

#url open library
from urllib.request import urlopen 

#import BeautifulSoup for html parsing
# try: 
#     from BeautifulSoup.request import BeautifulSoup
# except ImportError:
#     from bs4 import BeautifulSoup

#need to install beautifulsoup or another package to parse HTML

#setting how to open page
url = "https://www.kxan.com"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

parsed_html = BeautifulSoup(html)
print(parsed_html)

#tempscrape = html.find("site-header__weather-forecast__text")

#print(tempscrape)

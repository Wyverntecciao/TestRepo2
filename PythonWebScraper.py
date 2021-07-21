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
html = html_bytes.decode("UTF-8")

ATXtempTag = html.find('<span class="site-header__weather-forecast__text">')

ATXtempStartIndex = ATXtempTag + len('<span class="site-header__weather-forecast__text">')
ATXtempEndIndex = ATXtempStartIndex + 10


#ATXtemp= html.find('<span class="site-header__weather-forecast__text">')

weatherregion = html.find('<span class="site-header__weather-region">')

ATXtemp = html[ATXtempStartIndex:ATXtempEndIndex]

print(ATXtemp)
#print(weatherregion)
#print(html)

#tempscrape = html.find("site-header__weather-forecast__text")

#print(tempscrape)

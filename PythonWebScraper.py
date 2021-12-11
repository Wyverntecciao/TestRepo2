print ("Starting"); #starting message

#url open library
from urllib.request import urlopen 


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

tnonly = ATXtemp.split('&')

tempunits = " DEGREES F"

temptext = [tnonly[0],tempunits]

print(''.join(temptext))
#print(tnonly[0].join(tempunits))
#print(weatherregion)
#print(html)

#tempscrape = html.find("site-header__weather-forecast__text")

#print(tempscrape)



import sys
print(sys.version)

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.kxan.com"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.gettext())
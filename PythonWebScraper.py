print ("Starting");
from urllib.request import urlopen
url = "https://www.kxan.com"
page = urlopen(url)

print(page)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

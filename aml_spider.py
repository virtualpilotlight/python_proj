# I want a spider that finds the links keeps them and saves any files it finds in along the path

from bs4 import BeautifulSoup
import requests
url = "http://allmylove.org/audio/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup)
for link in soup.find_all('a'):
	print (url + link.get('href'))


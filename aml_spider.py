# I want a spider that finds the links keeps them and saves any files it finds in along the path

from bs4 import BeautifulSoup
import requests
url = "http://allmylove.org/audio/"


req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup)

urls = {url}

for link in soup.find_all('a'):
	new_url = url + link.get('href')
	print (new_url)
	print(type(new_url))
	urls.add(new_url)
	print(urls)
	print(type(urls))





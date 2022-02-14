# I want a spider that finds the links keeps them and saves any files it finds in along the path

from bs4 import BeautifulSoup
import requests

url = "http://allmylove.org/audio/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup)

urls = {url}

def get_links(soup):
	for link in soup.find_all('a'):
		global urls
		new_url = url + link.get('href')
		urls.add(new_url)

get_links(soup)

print(urls)

def soup_it(urls):
	for val in urls:
		if '.mp3' in val:
			# v2 did not work, this is a good place to start with the saving the files to disk
			print(f"Downloading File {name}")
			            download = req.get(href)
			            if download.status_code == 200:
			                with open(name, 'wb') as f:
			                    f.write(download.content)
			            else:
			                print(f"Download Failed For File {name}")
		req = requests.get(val)
		soup = BeautifulSoup(req.text, "html.parser")
		print("soup")
		get_links(soup)
		print(urls)

soup_it(urls)
print(urls)




# I want a spider that finds the links keeps them and saves any files it finds in along the path

"""
Initial soup # this is a html scrape of the page
Initial link scrape # takes a soup and makes a list_of_links 
# mast list of all links as a CSV

List of links
For each link in list of links
   Soup
   Scrape 

Something with cashing 

If link contains allmylove.org/audio/*.*
   Download
Else add link to list of links
"""

from bs4 import BeautifulSoup
import requests

url = "http://allmylove.org/audio/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

print("soup")

urls = {url}

def get_links(soup):
	for link in soup.find_all('a'):
		global urls
		new_url = url + link.get('href')
		urls.add(new_url)


for val in urls:
	if "allmylove" in val:
		print("no soup")
	else:
		print("soup")

get_links(soup)
print(urls)
 

def soup_it(urls):
	for val in urls:
		req = requests.get(val)
		soup = BeautifulSoup(req.text, "html.parser")
		print("soup")
		get_links(soup)
		print(urls)

soup_it(urls)
print(urls)


"""
if '.mp3' in val:
			# v2 did not work, this is a good place to start with the saving the files to disk
			print(f"Downloading File {name}")
			            download = req.get(href)
			            if download.status_code == 200:
			                with open(name, 'wb') as f:
			                    f.write(download.content)
			            else:
			                print(f"Download Failed For File {name}")
"""

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

def get_links(soup):
	counter = 0
	urls = {counter: url}
	for link in soup.find_all('a'):
		new_url = url + link.get('href')
		if "?" in new_url:
			print("no soup")
		elif new_url == url:
			print("already been souped")
		elif "http://allmylove.org/audio//" in new_url:
			print("no extra slashes")
		else:
			counter += 1
			urls.update({counter: new_url})
	return urls

get_links(soup)
print(urls)
url_list = urls.values()

def soup_it(url_list):
	for val in url_list:
		req = requests.get(val)
		soup = BeautifulSoup(req.text, "html.parser")
		print("soup")
		get_links(soup)
		print(urls)

soup_it(url_list)
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

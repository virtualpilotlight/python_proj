from bs4 import BeautifulSoup
import requests

url = "http://allmylove.org/audio/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

print("soup")

def get_links(soup):
	url_list = {url}
	print(type(url_list))
	for link in soup.find_all('a'):
		new_url = url + link.get('href')
		if "?" in new_url:
			print("no soup")
		elif new_url == url:
			print("already been souped")
		elif "http://allmylove.org/audio//" in new_url:
			print("no extra slashes")
		else:
			url_list.add(new_url)
	return url_list

get_links(soup)
print(url_list)

# wtf is <class 'dict_values'>???


"""
"""
urls.pop(0)
print(urls)
url_list = urls.values()

def soup_it(url_list):
	print("inside soup_it")
	for val in url_list:
		print(val)
		req = requests.get(val)
		print("req successful")
		soup = BeautifulSoup(req.text, "html.parser")
		print("soup")
		get_links(soup)
		print("links gotten")

soup_it(url_list)
print(urls)

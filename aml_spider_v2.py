from bs4 import BeautifulSoup
import requests
   
urls=[]
   
def scrape(site):
	r = requests.get(site)
	s = BeautifulSoup(r.text,"html.parser")   
	for i in s.find_all("a"):
		href = i.attrs['href']
		if href.startswith("/"):
			site = site+href               
			if site not in  urls:
				urls.append(site) 
				print(site)
				scrape(site)


site="http://allmylove.org/audio"
scrape(site)
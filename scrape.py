import urllib.request
from bs4 import BeautifulSoup 
import pandas as pd

def scrape():
	nasa_page = "https://mars.nasa.gov/news/"
	page = urllib.request.urlopen(nasa_page)
	soup = BeautifulSoup(page, "html.parser")

	latest_title = soup.find('div', attrs={'class':'content_title'}).text.strip()
	print(latest_title)
	mars_dict = {"latest_title": latest_title}

	latest_paragraph = soup.find('div', attrs={'class':'rollover_description_inner'}).text.strip()
	print(latest_paragraph)
	mars_dict["latest_paragraph"] = latest_paragraph

	jpl_page = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	page = urllib.request.urlopen(jpl_page)
	soup = BeautifulSoup(page, "html.parser")

	soup_url = soup.find('article', attrs={'class':'carousel_item'})

	isurl = False

	featured_url = str(soup_url)
	featured_image_url = "https://www.jpl.nasa.gov"
	i = 0

	while i < len(featured_url):
		if isurl == True:
			if featured_url [i] == "'":
				break
			else:
				featured_image_url += featured_url [i]
		if featured_url [i] == "u" and featured_url [i + 1] == "r" and featured_url [i + 2] == "l" and featured_url [i + 3] == "(" and featured_url [i + 4] == "'":
			isurl = True 
			i += 4
		i += 1

	print(featured_image_url)
	mars_dict["featured_image_url"] = featured_image_url

	twitter_weather_page = "https://twitter.com/marswxreport?lang=en"
	page = urllib.request.urlopen(twitter_weather_page)
	soup = BeautifulSoup(page, "html.parser")

	isreport = False


	featured_url = str(soup)
	mars_weather = ""
	i = 0

	while i < len(featured_url):
		if isreport == True:
			if featured_url [i] == "<":
				break
			else:
				mars_weather += featured_url [i]
		if featured_url [i] == "S" and featured_url [i + 1] == "o" and featured_url [i + 2] == "l" and featured_url [i + 3] == " " and featured_url [i - 1] == ">":
			isreport = True 
			mars_weather += featured_url [i] 
		i += 1

	print(mars_weather)
	mars_dict["mars_weather"] = mars_weather

	facts_page = ("https://space-facts.com/mars/")
	page = urllib.request.urlopen(facts_page)
	soup = BeautifulSoup(page,'lxml')
	table = soup.find_all('table')[0] 
	mars_facts_df = pd.read_html(str(table))
	print(mars_facts_df)
	mars_dict["mars_facts_df"] = mars_facts_df

	hemisphere_image_urls = [
		{"title": "Valles Marineris Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
		{"title": "Cerberus Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"},
		{"title": "Schiaparelli Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif"},
		{"title": "Syrtis Major Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
	]
	
	mars_dict["mars_hemispheres"] = hemisphere_image_urls
	
	return mars_dict
	
if __name__ == '__main__':
   scrape()
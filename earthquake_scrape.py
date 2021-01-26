'''
Author: Shana Scogin
Date: 1/26/20201
Class: Practicing Programming
Professor: Dr. Keith Davis
Acknowledgements:
-Brendan O'Handley for assistance with html/javascript
-Andrew Decker for general webscraping advice
-Brian Reardon for listening to me talk through soup errors
-Dr. Keith Davis for code pulling out individual hrefs
Sources:
-https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f
-https://able.bio/rhett/web-scraping-with-python-using-beautiful-soup-and-selenium--44jqsra
-https://stackoverflow.com/questions/43814754/python-beautifulsoup-how-to-get-href-attribute-of-a-element/43815538

Aim: This code saves the urls from a Nepali Times search page before looping
through a list of links to save the text from each link. A version of the first
half of this code that uses user input can be found in 'user_input_scrape'
'''

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import requests

url_ = 'https://www.nepalitimes.com/nepali-times-search/?q=earthquake'

# access the url with selenium with wait
browser = webdriver.Chrome('./chromedriver')
browser.get(url_)
time.sleep(5) # let's not overwhelm the site...
# NOTE: I cannot use requests here since the javascript code with the
# urls loads after the html page. Using selenium gets around this.
# See the first link listed under sources above for more.


# create obj from webpage source
page = BeautifulSoup(browser.page_source, 'html.parser')

# beautiful the code to check it out
print(page.prettify()) # this step can help since each website has diff tags

# parse and extract data
links = page.select("a.gs-title")
browser.quit()

# create a loop to save each href
link_list = []
for tag in links:
    link_list.append(tag.get("href"))
len(link_list)

# clean up list
start_letter = 'http'
link_list_clean = [x for x in link_list if x and x.startswith(start_letter)]

# loop through to scrape each pages and save the text
texts = []
for link in link_list_clean:
    url = link
    web_page = requests.get(url) # makes the request to the page
    # coverpage = web_page.content # saves the content into an obj called coverpage
    # web_page = request.get(url)
    soup = BeautifulSoup(web_page.text, 'html.parser') ## alternative way
    text = soup.findAll("p")
    texts.append(text)
    time.sleep(2)
## Problem: I do not know how to get just the text I want - this gets only
## the stuff in the p objects, which is close, but it's still too much

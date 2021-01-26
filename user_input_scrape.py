'''
Author: Shana Scogin
Date: 1/24/20201
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

Aim: This code takes a user-inputed url, provides an option to look at the
prettified html, and creates an object containing information from the page.
Future iterations will save the list of urls to a csv file.

Currently, there are not arguments in the function to change the html tags, so
the code only works for the Nepali Times.
'''

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd #
import requests # not used yet - will use to throw an error if url doesn't work

# create function
def f_scrape(url_, print_pretty): # need to add tag_ref

    # access the url with selenium with wait
    browser = webdriver.Chrome('./chromedriver')
    browser.get(url_)
    time.sleep(5) # let's not overwhelm the site...
    # NOTE: Cannot use requests here since the javascript code with the
    # urls loads after the html page. Using selenium gets around this.
    # See the first link listed under sources above for more.

    # create obj from webpage source
    page = BeautifulSoup(browser.page_source, 'html.parser')

    # beautiful the code to check it out
    if print_pretty == "TRUE":
        print(page.prettify()) # this step can help since each website has diff tags
    if print_pretty == "FALSE":
        pass

    # parse and extract data
    links = page.select("a.gs-title") # TODO: need to add an option for this
    browser.quit()

    # create a loop to save each href
    link_list = []
    for tag in links:
      link_list.append(tag.get("href")) # TODO: need to add an option for this

    # let the user know what's up
    n = str(len(link_list))
    print("Scrape found " + n + " urls")

    # save as text file
    link_list.to_csv('link_list.csv', index=False) ### TODO: need to change list to df

# have user put in the url and other options
print("This code will go to a specifed webpage and return a list of the urls found in the page.")
tag_ = input("First, do you want the prettified html printed back before you choose an html tag? (y/n):")
url_ = input("Great! Now, please enter your url: (Try https://www.nepalitimes.com/nepali-times-search/?q=earthquake) ")

# TODO: add option to change href

if tag_ == "y" or tag_ == "Y" or tag_ == "yes" or tag_ == "Yes" or tag_ == "YES":
    f_scrape(url_ = url_, print_pretty = "TRUE")
elif tag_ == "n" or tag_ == "N" or tag_ == "no" or tag_ == "No" or tag_ == "NO":
    f_scrape(url_ = url_, print_pretty = "FALSE")
else:
    print("Sorry, I do not recognize that input. Try again.")

# TODO: add requests to check if url works and throw error if does not

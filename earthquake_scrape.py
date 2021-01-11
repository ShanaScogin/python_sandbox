'''
Note: An iteration of a project for Dr. Davis's Practice Prgramming class at
Notre Dame, Jan 2021
Sources:
-https://github.com/miguelfzafra/Latest-News-Classifier
-http://theautomatic.net/2020/08/05/how-to-scrape-news-articles-with-python/
-https://pypi.org/project/selenium/
Aim: This code will collect articles with keywords from Nepali news sources and
analyse the text as data
'''

'''
First, collect articles with a keyword using the search bar with selenium
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./chromedriver')
browser.get('https://www.nepalitimes.com/')

elem = browser.find_element_by_class_name('search-input')
elem.send_keys('earthquake' + Keys.RETURN)

browser.quit()
# right now this just opens, searches, and closes the browser.
# next step is to scrape them, push the 'next' button, and then save them
# with beautifulsoup. I might also be able to do all of this with scrapy

'''
Second, use beautifulsoup to scrape articles found with selenium
'''

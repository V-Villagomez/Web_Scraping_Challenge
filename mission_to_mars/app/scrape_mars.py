from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False) 

# Define a function called `scrape` that will execute all of your scraping code from the `mission_to_mars.ipynb` notebook and return one Python dictionary containing all of the scraped data. 

def scrape():
    browser = init_browser()
    listing = {}
    zip_code = 92614
    min_price = 800
    max_price = 2000

    url = f"https://losangeles.craigslist.org/search/hhh?postal={zip_code}&max_price={max_price}&min_price={min_price}&availabilityMode=0"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    listing["headline"] = soup.find("a", class_="result-title").get_text()
    listing["price"] = soup.find("span", class_="result-price").get_text()
    listing["hood"] = soup.find("span", class_="result-hood").get_text()
    listing["url"] = soup.find("a", class_="result-title")["href"]

    # Store data in a dictionary
    costa_data = {"sloth_img": sloth_img, "min_temp": min_temp, "max_temp": max_temp}
    
    # Close the browser after scraping
    browser.quit()

    # Return results
    return costa_data

    return listing



# It will be a good idea to create multiple smaller functions that are called by the `scrape()` function. 
# Remember, each function should have one 'job' (eg. you might have a `mars_news()` function that scrapes the NASA mars news site and returns the content as a list/tuple/dictionary/json)
# HINT: the headers in the notebook can serve as a useful guide to where one 'job' ends and another begins. 
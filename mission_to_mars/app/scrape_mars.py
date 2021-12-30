from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

#def init_browser():
def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False) 

# Define a function called `scrape` that will execute all of your scraping code from the `mission_to_mars.ipynb` notebook and return one Python dictionary containing all of the scraped data. 

    #def scape():
    #browser = init_browser()

    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # latest news as of December 20, 2021
    latest_news = soup.find('li', class_='slide')
    news_title = latest_news.find('div', class_='content_title').text

    # .find() the paragraph text
    nasa_paragraph = latest_news.find('div', class_='article_teaser_body').text

    # mars_news = { 'news_title': news_title, 'nasa_paragraph': nasa_paragraph } 

    # return mars_news

# jpl_images():
    #browser = init_browser()
    
    jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(jpl_url)

    image_btn = browser.links.find_by_partial_text('FULL IMAGE').click()

    html = browser.html
    soup = bs(html, 'html.parser')

    relative_image = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'+relative_image

    # return featured_image_url

# mars_facts():
    #browser = init_browser()

    mars_url = 'https://space-facts.com/mars/'
    browser.visit(mars_url)
    mars_df = pd.read_html(mars_url)[0]
    mars_df.columns=['description', 'value']
    mars_df.set_index('description', inplace=True)
    mars_html_table = mars_df.to_html(justify='left')
    mars_html_table = mars_html_table.replace('\n', '')

    # return mars_html_table

# mars hemispheres():
    #browser = init_browser()

    hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemis_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    mars_data = soup.find_all("div", class_="item")

    hemisphere_image_urls = []

    mars_links = browser.find_by_css('a.prduct-item img')

    for i in range(len(mars_data)):
    
    #python dictionary to store the data
        hemispheres = {}
    
    # We have to find the elements on each loop to avoid a stale element exception
        browser.find_by_css('a.product-item img')[i].click()
    
    # Next, we find the Sample image anchor tag and extract the href
        sample_img = browser.links.find_by_text('Sample').first
        hemispheres['img_url'] = sample_img['href']
    
    #html = browser.html
    #soup = BeautifulSoup(html, 'html.parser')
    
    # Get Hemisphere title
        hemispheres['title'] = browser.find_by_css('h2.title').text
    
    # Append hemisphere object to list
        hemisphere_image_urls.append(hemispheres)
    
    # Finally, we navigate backwards with browser.back()
        browser.back()

    # return hemisphere_image_urls

    # return all results in one dictionary
    mars_dict = {
        'news_title': news_title, 
        'nasa_paragraph': nasa_paragraph,
        'featured_image_url': featured_image_url,
        'mars_html_table': mars_html_table,
        'hemisphere_image_urls': hemisphere_image_urls}
    
    # Close the browser after scraping
    browser.quit()

    # Return results
    return(mars_dict)

# Run your app
if __name__ == "__main__":
    print(scrape())

# It will be a good idea to create multiple smaller functions that are called by the `scrape()` function. 
# Remember, each function should have one 'job' (eg. you might have a `mars_news()` function that scrapes the NASA mars news site and returns the content as a list/tuple/dictionary/json)
# HINT: the headers in the notebook can serve as a useful guide to where one 'job' ends and another begins. 
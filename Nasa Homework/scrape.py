
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)

def scrape ():
    
    browser = init_browser()
    mars_data = {}

    local_nasa_file = "News_Nasa_Mars_Exploration_Program.html"
    nasa_html = open(local_nasa_file, "r").read()
    news_soup = BeautifulSoup(nasa_html, "html.parser")
    news_soup

    news_list = news_soup.find('ul', class_='item_list')
    first_item = news_list.find('li', class_='slide')
    first_title = first_item.find('div', class_='content_title').text
    first_para = first_item.find('div', class_='rollover_description_inner').text
    mars_data['first_title']=first_title
    mars_data['first_para']=first_para

    # # visit the JPL website and scrape the featured image
    # jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # browser.visit(jpl_url)
    # time.sleep(1)
    # browser.click_link_by_partial_text('FULL IMAGE')
    # time.sleep(1)
    # try:
    #     expand = browser.find_by_css('a.fancybox-expand')
    #     expand.click()
    #     time.sleep(1)

    #     jpl_html = browser.html
    #     jpl_soup = BeautifulSoup(jpl_html, 'html.parser')

    #     img_relative = jpl_soup.find('img', class_='fancybox-image')['src']
    #     image_path = f'https://www.jpl.nasa.gov{img_relative}'
    #     mars_data["feature_image_src"] = image_path
    # except ElementNotVisibleException:
    #     image_path = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA22076_hires.jpg'
    #     mars_data["feature_image_src"] = image_path
        
    # # visit the mars weather report twitter and scrape the latest tweet
    # mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
    # browser.visit(mars_weather_url)
    # time.sleep(1)
    # mars_weather_html = browser.html
    # mars_weather_soup = BeautifulSoup(mars_weather_html, 'html.parser')

    # tweets = mars_weather_soup.find('ol', class_='stream-items')
    # mars_weather = tweets.find('p', class_="tweet-text").text
    # mars_data["weather_summary"] = mars_weather

    # # visit space facts and scrap the mars facts table
    # mars_facts_url = 'https://space-facts.com/mars/'
    # browser.visit(mars_facts_url)
    # time.sleep(1)
    # mars_facts_html = browser.html
    # mars_facts_soup = BeautifulSoup(mars_facts_html, 'html.parser')

    # fact_table = mars_facts_soup.find('table', class_='tablepress tablepress-id-mars')
    # column1 = fact_table.find_all('td', class_='column-1')
    # column2 = fact_table.find_all('td', class_='column-2')

    # facets = []
    # values = []

    # for row in column1:
    #     facet = row.text.strip()
    #     facets.append(facet)
        
    # for row in column2:
    #     value = row.text.strip()
    #     values.append(value)
        
    # mars_facts = pd.DataFrame({
    #     "Facet":facets,
    #     "Value":values
    #     })

    # mars_facts_html = mars_facts.to_html(header=False, index=False)
    # mars_data["fact_table"] = mars_facts_html

    # # scrape images of Mars' hemispheres from the USGS site
    # mars_hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # hemi_dicts = []

    # for i in range(1,9,2):
    #     hemi_dict = {}
        
    #     browser.visit(mars_hemisphere_url)
    #     time.sleep(1)
    #     hemispheres_html = browser.html
    #     hemispheres_soup = BeautifulSoup(hemispheres_html, 'html.parser')
    #     hemi_name_links = hemispheres_soup.find_all('a', class_='product-item')
    #     hemi_name = hemi_name_links[i].text.strip('Enhanced')
        
    #     detail_links = browser.find_by_css('a.product-item')
    #     detail_links[i].click()
    #     time.sleep(1)
    #     browser.find_link_by_text('Sample').first.click()
    #     time.sleep(1)
    #     browser.windows.current = browser.windows[-1]
    #     hemi_img_html = browser.html
    #     browser.windows.current = browser.windows[0]
    #     browser.windows[-1].close()
        
    #     hemi_img_soup = BeautifulSoup(hemi_img_html, 'html.parser')
    #     hemi_img_path = hemi_img_soup.find('img')['src']

    #     hemi_dict['title'] = hemi_name.strip()       
    #     hemi_dict['img_url'] = hemi_img_path

    #     hemi_dicts.append(hemi_dict)

    # mars_data["hemisphere_imgs"] = hemi_dicts

    browser.quit()

    return mars_data
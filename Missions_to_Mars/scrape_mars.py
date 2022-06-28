
# Import dependencies
import pandas as pd
import pymongo
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Configure ChromeDriver
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)


# # NASA Mars News

# In[3]:
def mars_news(browser):

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    news_soup = BeautifulSoup(html, "html.parser")
    mars_news = news_soup.select_one("div.list_text")

    mars_news.find("div", class_="content_title")
    news_title = mars_news.find("div", class_="content_title").get_text()
    news_p = mars_news.find("div", class_="article_teaser_body").get_text()

    return news_title, news_p


# In[ ]:

def featured_image(browser):
# Visit the space image Site for featured image 

    url = "https://spaceimages-mars.com/"
    browser.visit(url)


    # In[ ]:


    # <button class
    full_image_button = browser.find_by_id("FULL IMAGE")
    full_image_button.click()
    
    html = browser.html
    image_soup = BeautifulSoup(html, "html.parser")




    img_url = image_soup.select_one('img', class_='fancybox-image').get("src")
    img_url


# Use Base URL to Create Absolute URL
    img_url = f"https://spaceimages-mars.com/{img_url}"
    print(img_url)


def mars_facts(browser):
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    mars_facts_df = pd.read_html(url)
    mars_facts_df = mars_facts_df[0]
    mars_facts_df.columns = ['Description', 'Mars', 'Earth']
    mars_facts_df

    mars_facts_html = mars_facts_df.to_html(classes='table table-striped')
    
    return mars_facts_html

def hemisphere(browser):
    
    url = "https://marshemispheres.com/"
    browser.visit(url+ 'index.html')

# # Visit the Mars Facts Site Using Pandas to Read
#     mars_df = pd.read_html("https://marshemispheres.com/")[0]
#     print(mars_df)
#     mars_df.columns=["Description", "Value"]
#     mars_df.set_index("Description", inplace=True)
#     mars_df

    hemisphere_image_urls = []
    links = browser.find_by_css("a.product-item h3")
    for item in range(len(links)):
        
    # Find Element on Each Loop to Avoid a Stale Element Exception
        browser.find_by_css("a.product-item h3")[item].click()
        hemisphere= hemisphere_scrape(browser.html)
        hemisphere['img_url'] = url + hemisphere['img_url']

        
     # Append Hemisphere Object to List
        hemisphere_image_urls.append(hemisphere)
        
    # Navigate Backwards
        browser.back()
        hemisphere_image_urls

def hemisphere_scrape(html_text):
    hemisphere   =BeautifulSoup(html_text, "html.parser")
    
    # Get Hemisphere Title
    hemisphere["title"] = browser.find_by_css("h2.title").text
    hemisphere['sample'] = browser.find_by_css("a.Sample").get('href')

    hemispheres = {
        "title": hemisphere['title'],
        "img_url": hemisphere['sample']
    }

    # if __name__ == '__main__':
    #     scrape_all()
# %%

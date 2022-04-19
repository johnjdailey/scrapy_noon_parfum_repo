#2get_parfum_info.py



# Downloads a csv file of all of the noon.com parfum info from their own respective webpages including:
# "brand","name","old_price","new_price","ml","concentration","department","scents","base_note","middle_note","item_rating","seller","seller_rating","num_seller_ratings"
# In agreement with the columns of the noon parfum csv data found on kaggle


# Imports

import os
import sys
import csv
import pandas as pd
from tqdm import tqdm
from timeit import default_timer as timer

import scrapy
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
from scrapy import Request
from scrapy.crawler import CrawlerProcess


# Be sure to check your project file structure if there are any import issues

#https://stackoverflow.com/questions/24570960/python-scrapy-does-not-working-importerror-no-module-named-settings/24576949

# Interesting function to get settings ... as opposed to just import Settings

settings = get_project_settings()

# Write all of the terminal output to a file for further analysis later, we may discover we miss some scrapes because the html/css/xpaths can change from page to page

sys.stdout = open("get_parfum_info_output0.txt", "w")


# We want the following attritbutes/column names for each parfum for our new csv

c = ["brand","name","old_price","new_price","ml","concentration","department","scents","base_note","middle_note","item_rating","seller","seller_rating","num_seller_ratings"]

# Import the df that has links scraped from get_parfum_links.py and cleaned by clean_links_df.py

df = pd.read_csv("noon_parfum_links.csv")
links = df["link"].to_list()

# Start timer

start = timer()


# Check if csv file already exists, if so, delete it, else scrape and create a new one

if os.path.exists("noon_parfum_info.csv"):
    os.remove("noon_parfum_info.csv")
else:
    print("noon_parfum_info.csv does not exist, scraping and creating one now.")


# InfoSpider class to use a scrapy spider to scrape all noon.com parfum info from previously scraped links and metadata to create a csv file of all the data

class InfoSpider(scrapy.Spider):

    # Name of scraper

    name = 'infoSpider'

    # This url works for the first page, for testing

#    start_urls = [
#          #'https://www.noon.com/uae-en/qafiya-03-edp-75ml/N18913615A/p?o=c0dae8e3126cee8f' # No Rating
#          "https://www.noon.com/uae-en/fahrenheit-le-parfum-spray-75ml/N11075112A/p?o=ce0613d0b2a77cbd"
#    ]
#    
#
#    # This url for loop works for scraping all of the pages on noon.com, and specifically for the links previously collected in 0get_parfum_links.p

    allowed_domains = ['www.noon.com']
    start_urls = [
                "https://www.noon.com" + \
                f"{link}"
                for link in links
    ]

    # Custom Settings, to feed data in CSV format - also supports JSON and XML

    custom_settings = {
        "FEED_FORMAT": "csv",
        "FEED_URI": 'noon_parfum_info.csv',
        "DOWNLOADER_MIDDLEWARES" : settings.get("DOWNLOADER_MIDDLEWARES"),
        "USER_AGENT" : settings.get("USER_AGENT") 
    }

    # Scrapy parse function to parse all of the required data - think: Extract, Transform, Load

    def parse(self, response):

        # Loop through the responses from noon.com to extract the required data using xpath this time. We could also use .css or even in combination with methods from BS4

        for product in response.xpath('//*[@id="__next"]/div/section'):

            # Some parfum prices are in index 2, and in index on other pages. So, we can try, if there is an error, then pass, then use the other index

            try:
                old_price = product.xpath("//*[@id='__next']/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/text()").extract()[2]
            except:
                pass
                old_price = product.xpath("//*[@id='__next']/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/text()").extract()

            try:
                new_price = product.xpath("//*[@id='__next']/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[4]/text()").extract()[2]
            except:
                pass
                new_price = product.xpath("//*[@id='__next']/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[4]/text()").extract()
            
            try:
                seller_rating = product.xpath("//*[@id='__next']/div/section/div/div[1]/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[2]/text()").extract()[1]
            except:
                pass
                seller_rating = product.xpath("//*[@id='__next']/div/section/div/div[1]/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[2]/text()").extract()[0]

            yield {

                "brand": product.xpath("//*[@id='__next']/div/section/div/div[1]/div/div[2]/div[1]/div[2]/a/div/text()").get(),
                "name": product.xpath("//*[@id='__next']/div/section/div/div[1]/div/div[2]/div[1]/div[2]/h1/text()").get(),            
                "old_price": old_price,
                "new_price": new_price,
                "ml": "wrangle from name",
                "concentration": "wrangle from name",
                # Just use pandas read_html to scrape these tables and then merge, was not able to scrape these with this method for some reason
#                "department": product.xpath("//*[@id='__next']/div/section/div/div[2]/div/div/div[2]/div/div/div[1]/table/tbody/tr[3]/td[2]/text()") ? 
#                "scents":
#                "base_note": product.xpath("//*[@id='__next']/div/section/div/div[2]/div/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[2]/text()"),
#                "middle_note":
                "item_rating": product.xpath("//*[@id='__next']/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/a/div/div[1]/text()").get(),
                "seller": product.xpath("//*[@id='__next']/div/section/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/span/a/text()").get(),
                "seller_rating": seller_rating,
                "num_seller_ratings": product.xpath("//*[@id='__next']/div/section/div/div[1]/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/div[3]/div/div/text()").get()
                   }

    # This will make the requests from the list of start_urls, we can add a header here to look like a normal broswer, a proxy, and other Requests parameters - see the docs: https://docs.scrapy.org/en/latest/topics/request-response.html#module-scrapy.http

    handle_httpstatus_list = [403, 404] # https://stackoverflow.com/questions/50786931/error-403-in-scrapy-while-crawling
    # Output
    #'bans/status/403': 2495,
    #'bans/status/404': 4,

    def start_requests(self): #https://stackoverflow.com/questions/14075941/how-to-access-scrapy-settings-from-item-pipeline
        #headers= ({"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}) # This is a trivial solution for solving a 403 response (website blocking the scraper)
        for url in tqdm(self.start_urls):          # /\ However, this is not enough for this scraping job of 10500 URLs, and the scraper gets a "INFO: Ignoring response <403 https://www.noon.com/uae-en/sloane-rose-edp-100ml/N11074680A/p?o=ac27cff4f6539cee>: HTTP status code is not handled or not allowed" message at around 2500 scrapes, so we try the solution found here: https://stackoverflow.com/questions/50786931/error-403-in-scrapy-while-crawling      
            #yield scrapy.Request(url, headers=headers, meta=...) # meta is another possible argument here with allows for proxies, ie: # https://stackoverflow.com/questions/4710483/scrapy-and-proxies ....... http://free-proxy.cz/en/
            request = Request(url, headers = settings.get("DEFAULT_REQUEST_HEADERS"))
            #request.meta["proxy"] = "https://3.130.124.100:8080" #"https://51.223.252.49:8080" - set more proxies in settings.py
            yield request


# Stop timer

Runtime = timer() - start # in seconds

print("Runtime:", Runtime)

# 'elapsed_time_seconds':


# Run spider (runs by running script instead of having to use: scrapy runspider get_parfum_info.py)

process = CrawlerProcess()
process.crawl(InfoSpider)
process.start()


# Close the file writing terminal output 

sys.stdout.close()

#0get_parfum_links.py

# Downloads a csv file of all of the noon.com parfum names, currency, prices and links



# Imports

import os
import csv
from timeit import default_timer as timer

import scrapy
from scrapy.crawler import CrawlerProcess


# Start timer

start = timer()


# Check if csv file already exists, if so, delete it, else scrape and create a new one

if os.path.exists("noon_parfum_links.csv"):
    os.remove("noon_parfum_links.csv")
else:
    print("noon_parfum_links.csv does not exist, scraping and creating one now.")


# LinksSpider class to use a scrapy spider to scrape all noon.com parfum links and metadata to create a csv file of all the data

class LinksSpider(scrapy.Spider):

    # Name of scraper

    name = 'linksSpider'

#    # This url works for the first page, for testing
#
#    start_urls = [
#          'https://www.noon.com/uae-en/search?q=parfum'
#    ]
    

     # This url for loop works for scraping all of the pages with pdf files of forms on the IRS website

    start_urls = [
                "https://www.noon.com/uae-en/search?limit=150" + \
                f"&page={page}&q=parfume"
                for page in range(0, 70, 1)
    ]

    # Custom Settings, to feed data in JSON format - also supports CSV and XML

    custom_settings = {
        "FEED_FORMAT": "csv",
        "FEED_URI": 'noon_parfum_links.csv'
    }

    # Scrapy parse function to parse all of the IRS form product numbers, pdf download urls, titles, and revision dates

    def parse(self, response):

        # Loop through the tables on the IRS websites to extract the form numbers, pdf download links, form title, and revision dates

        for products in response.css('div.productContainer'): # table css

            name = products.css("span:nth-child(2)").get()
            name = name.replace("<span>","")
            name = name.replace("<!-- -->","")
            name = name.replace("</span>","")

            yield {
                "name": name, # we could also try using BS4's match.unwrap() https://stackoverflow.com/questions/22496822/removing-span-tags-from-soup-beautifulsoup-python
                "currency": products.css("span.currency::text").get(),
                "price": products.css("strong::text").get(),
                "link": products.css("a::attr(href)").extract_first(),
            }

    # This will make the requests from the list of start_urls, we can add a header here to look like a normal broswer, a proxy, and other Requests parameters - see the docs: https://docs.scrapy.org/en/latest/topics/request-response.html#module-scrapy.http

    def start_requests(self):
        headers= ({"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"})
        for url in self.start_urls:                         # https://stackoverflow.com/questions/4710483/scrapy-and-proxies
            yield scrapy.Request(url, headers=headers)


# Stop timer

Runtime = timer() - start # in seconds

print("Runtime:", Runtime)


# Run spider (runs by running script instead of having to use: scrapy runspider get_parfum_links.py)

process = CrawlerProcess()
process.crawl(LinksSpider)
process.start()

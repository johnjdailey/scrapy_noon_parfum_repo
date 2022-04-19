# Scrapy settings for scrapy_noon_parfum project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_noon_parfum'

SPIDER_MODULES = ['scrapy_noon_parfum.spiders']
NEWSPIDER_MODULE = 'scrapy_noon_parfum.spiders'

# Write output to a text file

LOG_STDOUT = True
LOG_FILE = "get_parfum_info_output.txt"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'scrapy_noon_parfum (+http://www.noon.com)'

# Obey robots.txt rules - https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware
#ROBOTSTXT_OBEY = True
#ROBOTSTXT_PARSER = "scrapy.robotstxt.PythonRobotParser"

# To solve this error: scrapy.core.engine] DEBUG: Crawled (403) <GET https://www.noon.com/robots.txt> (referer: None)

from scrapy_noon_parfum.utils import get_random_agent

#USER_AGENT = get_random_agent()
#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'

# This could be even better for getting passed 403 - https://github.com/alecxe/scrapy-fake-useragent

#FAKEUSERAGENT_PROVIDERS = [
#    'scrapy_fake_useragent.providers.FakeUserAgentProvider',  # this is the first provider we'll try
#    'scrapy_fake_useragent.providers.FakerProvider',  # if FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
#    'scrapy_fake_useragent.providers.FixedUserAgentProvider',  # fall back to USER_AGENT value
#]
#USER_AGENT = get_random_agent() #'<your user agent string which you will fall back to if all other providers fail>'

#USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
#CONCURRENT_REQUESTS = 1
#DOWNLOAD_DELAY = 5

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 1 # default:  3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
    'authority': 'noon.com', # https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    #'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'user-agent':  USER_AGENT, # FAKEUSERAGENT_PROVIDERS,
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip, deflate',
    #'Accept-Language': 'en-US,*',
}
# Previous noobie solutions which did not work for this high volume of scraping ~ 10500 urls
#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"


# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_noon_parfum.middlewares.scrapy_noon_parfumSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None, # This can be used to override deault user agent https://docs.scrapy.org/en/latest/topics/downloader-middleware.html?highlight=UserAgentMiddleWare#scrapy.downloadermiddlewares.useragent.UserAgentMiddleware
#    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1 # https://stackoverflow.com/questions/4710483/scrapy-and-proxies
#}

ROTATING_PROXY_LIST = [ # http://free-proxy.cz/en/proxylist/country/US/https/uptime/level1
    'https://68.183.221.156:42048', # USA
    'https://20.97.28.47:8080', # USA
    'https://23.107.176.84:32180', # USA
    'https://47.242.200.148:80', # USA
    'https://150.136.5.47:80', # USA
    'https://150.136.72.180:80', # USA
    'https://178.32.41.167:8080', # Belgium
    'http://92.204.129.161:80', # Germany
    'https://14.207.120.81:8080', # Thailand
    'http://82.223.108.75:80', # Spain
    'http://52.209.100.128:80', # Ireland
    "HTTPS://35.244.81.72:80",
    "HTTPS://78.101.64.35:8080",
    "HTTPS://54.74.172.252:80",
    "HTTPS://172.107.193.236:443",
    "HTTPS://23.107.176.84:32180",
    "HTTPS://160.16.71.130:80",
    "HTTPS://186.0.176.147:8080",
    "HTTPS://185.60.25.51:80",
    "HTTPS://197.255.52.214:8081",
    "HTTPS://47.242.200.148:80",
    "HTTPS://130.61.22.238:80",
    "HTTPS://167.172.184.166:40065",
    "HTTPS://176.56.107.234:33911",
    "HTTPS://92.207.253.226:38157",
    "HTTPS://35.222.148.80:80",
    "HTTPS://213.230.97.10:3128",
    "HTTPS://118.99.100.33:8080",
    "HTTPS://23.254.161.181:80",
    "HTTPS://154.66.245.47:46611",
    "HTTPS://103.224.136.237:80",
    "HTTPS://168.138.211.5:8080",
    "HTTPS://128.199.20.88:8080",
    "HTTPS://189.112.111.194:80",
    "HTTPS://23.94.143.167:80",
    "HTTPS://46.246.6.2:3128",
    "HTTPS://185.220.175.233:80",
    "HTTPS://109.86.219.179:53438",
    "HTTPS://3.22.72.241:80",
    "HTTPS://150.136.37.217:80",
    "HTTPS://112.133.200.131:81",
    "HTTPS://103.68.60.115:80",
    "HTTPS://103.93.248.73:80",
    "HTTPS://130.61.155.13:80",
    "HTTPS://18.221.9.126:80",
    "HTTPS://134.19.254.2:21231",
    "HTTPS://51.222.21.93:32768",
    "HTTPS://178.32.41.167:8080",
    "HTTPS://137.74.245.212:43567",
    "HTTPS://23.107.176.87:32180",
    "HTTPS://51.38.82.244:443",
    "HTTPS://2.104.55.144:80",
    "HTTPS://147.135.255.62:8241",
    "HTTPS://84.54.82.234:3128",
    "HTTPS://157.230.103.91:36635",
    "HTTPS://103.240.77.98:30093",
    "HTTPS://109.172.57.250:23500",
    "HTTPS://46.61.194.166:8080",
    "HTTPS://152.179.12.86:3128",
    "HTTPS://20.97.28.47:8080",
    "HTTPS://117.121.202.62:8080",
    "HTTPS://157.230.103.189:40251",
    "HTTPS://160.16.226.31:3128",
    "HTTPS://146.59.199.43:80",
    "HTTPS://14.207.120.81:8080",
    "HTTPS://43.224.10.36:6666",
    "HTTPS://130.61.236.104:80",
    "HTTPS://115.124.115.26:80",
    "HTTPS://68.183.230.116:33061",
    "HTTPS://202.40.188.94:40486",
    "HTTPS://103.231.80.146:55443",
    "HTTPS://202.51.86.91:8080",
    "HTTPS://150.136.5.47:80",
    "HTTPS://51.210.151.72:443",
    "HTTPS://68.183.221.156:42048",
    "HTTPS://165.227.173.87:41302",
    "HTTPS://83.111.183.37:80",
    "HTTPS://177.223.16.110:8080",
    "HTTPS://150.136.72.180:80",
    "HTTPS://172.107.159.194:443",
    "HTTPS://51.222.21.94:32768",
    "HTTPS://86.29.163.97:49787",
    "HTTPS://65.2.86.118:80",
    "HTTPS://192.166.144.250:80",
    "HTTPS://128.240.212.61:80",
    "HTTPS://172.106.12.19:443",
    "HTTPS://3.234.61.191:80",
    "HTTPS://177.37.161.4:41819",
    "HTTPS://191.252.38.6:80",
    "HTTPS://103.9.191.174:56765",
    "HTTPS://190.61.63.83:999",
    "HTTPS://192.153.57.250:80",
    "HTTPS://43.225.23.131:80",
    "HTTPS://201.49.58.234:80",
    "HTTPS://103.246.225.34:80",
    "HTTPS://164.163.12.50:8080",
    "HTTPS://176.63.205.248:54621",
    "HTTPS://168.119.248.202:6000",
    "HTTPS://14.99.187.7:80",
    "HTTPS://45.112.124.133:8080",
    "HTTPS://36.94.35.217:55418",
    "HTTPS://154.66.241.27:52004",
    "HTTPS://13.232.80.159:80",
    "HTTPS://192.99.239.215:8080",
    "HTTPS://46.101.173.102:8080",
    "HTTPS://82.165.117.135:80",
    "HTTPS://138.197.142.249:80",
    "HTTPS://201.132.155.198:8080",
    "HTTPS://47.88.17.124:1157",
    "HTTPS://177.124.63.140:80",
    "HTTPS://150.129.148.88:35101",
    "HTTPS://23.107.176.12:32180",
    "HTTPS://157.90.162.222:3129",
    "HTTPS://34.245.170.188:80",
    "HTTPS://195.78.112.235:42549",
    "HTTPS://142.93.208.14:80",
    "HTTPS://86.29.163.97:49787",
    "HTTPS://65.2.86.118:80",
    "HTTPS://192.166.144.250:80",
    "HTTPS://128.240.212.61:80",
    "HTTPS://172.106.12.19:443",
    "HTTPS://3.234.61.191:80",
    "HTTPS://177.37.161.4:41819",
    "HTTPS://191.252.38.6:80",
    "HTTPS://103.9.191.174:56765",
    "HTTPS://190.61.63.83:999",
    "HTTPS://192.153.57.250:80",
    "HTTPS://43.225.23.131:80",
    "HTTPS://201.49.58.234:80",
    "HTTPS://103.246.225.34:80",
    "HTTPS://164.163.12.50:8080",
    "HTTPS://176.63.205.248:54621",
    "HTTPS://168.119.248.202:6000",
    "HTTPS://14.99.187.7:80",
    "HTTPS://45.112.124.133:8080",
    "HTTPS://36.94.35.217:55418",
    "HTTPS://154.66.241.27:52004",
    "HTTPS://13.232.80.159:80",
    "HTTPS://192.99.239.215:8080",
    "HTTPS://46.101.173.102:8080",
    "HTTPS://82.165.117.135:80",
    "HTTPS://138.197.142.249:80",
    "HTTPS://201.132.155.198:8080",
    "HTTPS://47.88.17.124:1157",
    "HTTPS://177.124.63.140:80",
    "HTTPS://150.129.148.88:35101",
    "HTTPS://23.107.176.12:32180",
    "HTTPS://157.90.162.222:3129",
    "HTTPS://34.245.170.188:80",
    "HTTPS://195.78.112.235:42549",
    "HTTPS://142.93.208.14:80",
    "HTTPS://46.101.173.102:8080",
    "HTTPS://82.165.117.135:80",
    "HTTPS://138.197.142.249:80",
    "HTTPS://201.132.155.198:8080",
    "HTTPS://47.88.17.124:1157",
    "HTTPS://177.124.63.140:80",
    "HTTPS://150.129.148.88:35101",
    "HTTPS://23.107.176.12:32180",
    "HTTPS://157.90.162.222:3129",
    "HTTPS://34.245.170.188:80",
    "HTTPS://195.78.112.235:42549",
    "HTTPS://142.93.208.14:80",
    "HTTPS://193.122.144.192:80",
    "HTTPS://186.194.120.72:8080",
    "HTTPS://190.186.1.46:55830",
    "HTTPS://36.67.57.45:30066",
    "HTTPS://172.107.159.202:443",
    "HTTPS://129.213.69.94:80",
    "HTTPS://41.87.29.130:8080",
    "HTTPS://36.66.242.146:43936",
    "HTTPS://34.94.158.4:80",
    "HTTPS://130.61.227.199:80",
    # ...
]

DOWNLOADER_MIDDLEWARES = { # https://medium.com/@TeraCrawler.io/how-to-rotate-proxies-in-scrapy-2bccf38439f7
    # ...
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 800,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 800,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1
    # ...
}   

# TODO READ THESE FOR BETTER SCRAPING RESULTS 
# GREAT RESOURCE FOR ADVANCED TECHNIQUES: http://sangaline.com/post/advanced-web-scraping-tutorial/
# INFORMATIVE BEST PRACTICES: https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scrapy_noon_parfum.pipelines.scrapy_noon_parfumPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

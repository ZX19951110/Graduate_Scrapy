# -*- coding: utf-8 -*-

# Scrapy settings for graduate_scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'graduate_scrapy'

SPIDER_MODULES = ['graduate_scrapy.spiders']
NEWSPIDER_MODULE = 'graduate_scrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'graduate_scrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 15
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Host': 'www.lagou.com',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=ABAAABAAAGGABCB9DB06594E35E7110DEE2C284A2B7F0AA; user_trace_token=20180210191157-9d456791-e83b-4c95-ad98-c12b15308bd2; LGUID=20180210191158-36324b21-0e53-11e8-afce-5254005c3644; _gid=GA1.2.2011062565.1518261119; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1518261119; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1518265140; _ga=GA1.2.2020632721.1518261118; LGSID=20180210201900-937b7428-0e5c-11e8-826b-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_web%25E5%2589%258D%25E7%25AB%25AF; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_web%25E5%2589%258D%25E7%25AB%25AF%3Fpx%3Ddefault%26city%3D%25E6%2588%2590%25E9%2583%25BD; LGRID=20180210201900-937b75b9-0e5c-11e8-826b-525400f775ce; SEARCH_ID=e924f127ba3e432ab3a824507b1ba770',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_web%E5%89%8D%E7%AB%AF?px=default&gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B,3-5%E5%B9%B4&xl=%E6%9C%AC%E7%A7%91&city=%E6%88%90%E9%83%BD'
    }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'graduate_scrapy.middlewares.GraduateScrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
 #    'graduate_scrapy.middlewares.proxy_middlewares': 20
      'graduate_scrapy.middlewares.user_agent_middlewares': 20
  }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'graduate_scrapy.pipelines.GraduateScrapyPipeline': 300,
    #'graduate_scrapy.pipelines.JsonWithEncodingPipeline': 2,
    'graduate_scrapy.pipelines.SaveInMysql': 301
}
#Mysql Connection Settings
MYSQL_SETTING ={
    'host': '127.0.0.1',
    'user': 'root',
    'db': 'graduate',
    'password': '123456',
    'port': '3306'
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
PROXIES_HTTP = [
    {'ip_port': '110.73.0.26:8123'},
    {'ip_port': '111.155.116.215:8123'},
    {'ip_port': '111.11.228.75:80'},
    {'ip_port': '110.73.0.26:8123'},
    {'ip_port': '122.96.59.104:80'},
]
PROXIES_HTTPS = [
    {'ip_port': '120.77.254.116:3128'},
    {'ip_port': '119.28.138.104:3128'},
    {'ip_port': '111.230.165.16:3128'},
]
PROXIES_FOREIGN = [
    {'ip_port': '192.155.185.201:80'},
    {'ip_port': '192.155.185.78:80'},
    {'ip_port': '192.155.185.8:80'},
]
USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
]
JOB_MAPPING_TABLE= {
    "数据挖掘": 'data_mining',
    "大数据": 'big_data',
    "机器学习": 'm_l',
    "产品经理": 'program_manager',
    "c++": 'c_plus'
}

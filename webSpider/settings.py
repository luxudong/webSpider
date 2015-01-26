# -*- coding: utf-8 -*-

# Scrapy settings for webSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'webSpider'

SPIDER_MODULES = ['webSpider.spiders']
NEWSPIDER_MODULE = 'webSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'webSpider (+http://www.yourdomain.com)'

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'webspider'
MONGODB_CRAWLER_SITE = 'website'
MONGODB_ARTICLES_LIST = 'articles_list'
MONGODB_ARTICLES_CONTENT = 'articles_content'
MONGODB_ARTICLES_SITE = 'articles_site'
MONGODB_ARTICLES_LIST_URL_MD5 = 'articles_list_url_md5'
MONGODB_SAFE = True

ITEM_PIPELINES = {
    'webSpider.pipelines.JsonWithEncodingBdhubPipeline': 300,
}

LOG_LEVEL = 'INFO'
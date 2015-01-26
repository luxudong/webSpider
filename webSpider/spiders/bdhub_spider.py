import scrapy
import datetime
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from webSpider.items import *
from webSpider.misc.log import *

class ClassName(CrawlSpider):
	"""docstring for ClassName"""
	name = "bdhub"
	allowed_domains = ["ibmbigdatahub.com"]
	start_urls = [
		"http://www.ibmbigdatahub.com/blogs"
	]
	rules = [
		Rule(sle(allow=("/blogs\?page=\d{,4}")),follow=True, callback='parse_item')
	]
	def isempty(self,var):
		if len(var):
			return var[0]
		else:
			return None
	def parse_item(self, response):
		items = []
		sel = Selector(response)
		base_url = get_base_url(response)
		siteviews = sel.css('div.view-content div.views-row')
		for view in siteviews:
			item = DbhubItem()
			view = view.css('div.node__teaser')
			item['author'] = self.isempty(view.css('div.node__attributes span.blogger__name').xpath('a/text()').extract())
			item['authorTitle'] = self.isempty(view.css('div.node__attributes span.blogger__title-and-company').xpath('text()').extract())
			item['imageUrl'] = self.isempty(view.css('div.blog__image a').xpath('img/@src').extract())
			item['title'] = self.isempty(view.css('h2').xpath('a/text()').extract())
			item['date'] = self.isempty(view.css('div.node__attributes span.blog__created-date').xpath('text()').extract())
			item['summery'] = self.isempty(view.css('div.blog__summary').xpath('text()').extract())
			relative_url = self.isempty(view.css('h2').xpath('a/@href').extract())
			item['link'] = urljoin_rfc(base_url, relative_url)
			item['baseUrl'] = response.url
			items.append(item)
		info("parsed " + str(response))
		return items

	def parse_start_url(self,response):
		return self.parse_item(response)

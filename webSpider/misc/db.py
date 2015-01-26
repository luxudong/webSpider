from pymongo import MongoClient
import redis
from scrapy.conf import settings
from utils import Utils

class Mongodb:
	"""docstring for Mongodb"""
	def __init__(self, col):
		self.server = settings['MONGODB_SERVER']
		self.port = settings['MONGODB_PORT']
		self.db = settings['MONGODB_DB']
		self.col = col
		connection = MongoClient(self.server,self.port)
		db = connection[self.db]
		self.collection = db[self.col]

	def save(self, obj):
		if self.col == settings['MONGODB_ARTICLES_LIST']:
			self.collection.insert({
				'author' : obj.author,
				'authorTitle' : obj.authorTitle,
				'imageUrl' : obj.imageUrl,
				'title' : obj.title,
				'date' : self.date,
				'summery' : self.summery,
				'link' : self.link,
				'baseUrl' : self.baseUrl
			})
		elif self.col == settings['MONGODB_ARTICLES_SITE']:
			self.collection.insert({
				'site' : obj.site,
				'source' : obj.source,
				'updated' : obj.updated
			})
		elif self.col == settings['MONGODB_ARTICLES_CONTENT']:
			self.collection.insert({
				'url' : obj.link,
				'source' : obj.source,
				'isParse' : obj.isParse 
			})
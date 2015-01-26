# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import json
import codecs
import pymongo
import datetime
from pymongo import MongoClient
from webSpider.misc.utils import Utils

class JsonWithEncodingBdhubPipeline(object):

    def __init__(self):
        self.file = codecs.open('bdhub.json', 'w', encoding='utf-8')
        self.client = MongoClient("localhost",27017)
        self.db = self.client.bdhub
        self.collection = self.db.first

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        dbdict = dict(item)
        dbdict['date'] = Utils.timestamp_to_datetime_by_format(Utils.str_to_timestamp_by_format(dbdict['date']))
        
        dbdict['createdate'] = datetime.datetime.utcnow()
        if dbdict['authorTitle']:
            dbdict['authorTitle'] = str(dbdict['authorTitle'].encode("utf-8")).strip()
        self.collection.insert(dbdict)
        return item

    def spider_closed(self, spider):
        self.file.close()

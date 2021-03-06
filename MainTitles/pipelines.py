# -*- coding: utf-8 -*-

import pymongo
import scrapy
from scrapy.conf import settings


class MaintitlesPipeline(object):
    
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_SERVER'],settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

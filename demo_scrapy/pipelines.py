# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


CONNECTION_STRING = "mongodb+srv://DucKhoan:Khoan25032001@cluster.lr6v6.mongodb.net/test"

class DemoScrapyPipeline:
    def process_item(self, item, spider):
        return item

class ProductPipeline:
    def __init__(self):
        self.client = MongoClient(CONNECTION_STRING)
        self.db_name = self.client["Products"]
    def process_item(self, item, spider):
        collection_name = self.db_name["Product"]
        collection_name.insert_one(dict(item))
        return item

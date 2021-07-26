# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    price_sale =scrapy.Field()
    price = scrapy.Field()
    rate_average = scrapy.Field()


class ProductItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    price_sale = scrapy.Field()
    sold = scrapy.Field()
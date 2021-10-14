# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MonstiesprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class mon_stats(scrapy.Item):
    # ... other item fields ...
    image_urls = scrapy.Field()
    images = scrapy.Field()


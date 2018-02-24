# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    # 问题
    headline = scrapy.Field()
    # 编号
    number = scrapy.Field()
    # 处理状态
    state = scrapy.Field()
    # 提问时间
    questiontime = scrapy.Field()
    # 问题详情
    info = scrapy.Field()
    # 链接
    sourcelink = scrapy.Field()




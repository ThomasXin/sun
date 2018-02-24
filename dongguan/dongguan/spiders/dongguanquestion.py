# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem

class DongguanquestionSpider(CrawlSpider):
    name = 'dongguanquestion'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=0']
    pagelinks = LinkExtractor(allow='page=\d+')
    questionlinks = LinkExtractor(allow='/question/\d+/\d+.shtml')
    rules = (
        Rule(pagelinks),
        Rule(questionlinks, callback='parse_item'),
    )

    def parse_item(self, response):
        item = DongguanItem()

        item['headline'] = response.xpath('//div[contains(@class,"pagecenter p3")]//strong/text()').extract()[0]

        item['number'] = item['headline'].split(' ')[-1].split(':')[-1]

        item['state'] = response.xpath('//span[@class="qgrn"]/text() | //span[@class="qblue"]/text() | //span[@class="qred"]/text() ').extract()[0]

        item['questiontime'] = response.xpath('//p[@class="te12h"]/text()').extract()[0].split('：')[-1]

        info = response.xpath('//div[contains(@class,"pagecenter p3")]//div[@class="contentext"]/text()').extract()

        if len(info) == 0:
            content = response.xpath('//div[contains(@class,"pagecenter p3")]//div[@class="c1 text14_2"]/text()').extract()
            item['info'] = "".join(content)
        else:
            item['info'] = "".join(info)
        item['sourcelink'] = response.url

        yield item

        # print response.url
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i

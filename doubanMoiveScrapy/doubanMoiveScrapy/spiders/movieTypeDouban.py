# -*- coding: utf-8 -*-
import scrapy
from doubanMoiveScrapy.items import movieType


class MovietypedoubanSpider(scrapy.Spider):
    name = 'movieTypeDouban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/tag/#']

    def parse(self, response):
        print('===================================')
        print(response)
        print('===================================')
        tst = 0
        tst = response.xpath('/html/body/div[3]/div[1]/div/div[1]/div/div/div[1]/div[1]/ul[2]/li[18]/span/text()').get()
        item = movieType()
        mType = 0
        for i in range(2,24):
            mType = response.xpath('//*[@id="app"]/div/div[1]/div[1]/ul[2]/li['+str(i)+']/span/text()').extract_first()
            print(mType)
            item['type'] = mType
            yield item



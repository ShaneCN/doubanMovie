# -*- coding: utf-8 -*-
import scrapy
from doubanMoiveScrapy.items import DoubanmoivescrapyItem
from doubanMoiveScrapy.items import Doubanlink

class Doubantop250scrapySpider(scrapy.Spider):
    name = 'doubanTop250Scrapy'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']
    base_url = 'http://movie.douban.com/top250'
    nRound = 0
    #解析
    def parse(self, response):
        item = Doubanlink()
        i = 1
        for i in range(1,26):

            item['link'] = 0
            link = response.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li['+str(i)+']/div/div[2]/div[1]/a/@href').get()
            item['link'] = link
            print(link)
            yield item

        if self.nRound < 10:
            num = 25*self.nRound
            self.nRound = self.nRound+1
            tailer = '?start='+str(num)+'&filter='
            url = self.base_url+tailer
            yield scrapy.Request(url, callback=self.parse)
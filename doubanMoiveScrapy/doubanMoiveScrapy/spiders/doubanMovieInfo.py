# -*- coding: utf-8 -*-
import scrapy
from doubanMoiveScrapy.items import DoubanmoivescrapyItem

class DoubanmovieinfoSpider(scrapy.Spider):
    contents = []
    nRound = 187
    with open('/Users/shane/PycharmProjects/doubanMovie/doubanMoiveScrapy/doubanMoiveScrapy/spiders/spiderdata.json') as fileObj:
        contents = fileObj.readlines(25000)

    name = 'doubanMovieInfo'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/1292052/']
    print('--------------------------------------------')

    def parse(self, response):
        print('---------------------------------------------------------------')
        item = DoubanmoivescrapyItem()
        name = response.xpath('/html/body/div[3]/div[1]/h1/span[1]/text()').extract_first()
       # name.replace("/",'')
        star = response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong/text()').get()
        actor = response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span[3]/span[2]//text()').extract()
        actor = actor.replace("'",'')
        director = response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/span[2]/a/text()').extract_first()
        writer = response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span[2]/span[2]//text()').extract()

        theme = []
        theme.append(response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span[5]/text()').extract_first())
        n = 6
        while response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span['+str(n)+']/text()').extract_first()!='制片国家/地区:': #and response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span['+str(n)+']/text()').extract_first()!='官方网站:':
            theme.append(response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span['+str(n)+']/text()').extract_first())
            n = n + 1
        country = response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span['+str(n)+']/following::text()[1]').extract_first()
        n = n + 3
        time = response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span['+str(n)+']//text()').extract()
        n = n + 1
        while response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span['+str(n)+']/text()').extract_first()!='片长:':
            time.append(response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/span['+str(n)+']//text()').extract())
            n = n + 1
        comments=[]
        comments.append(response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[10]/div[2]/div[2]/div[1]/div[1]/div/p/span/text()').extract())
        comments.append(response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[10]/div[2]/div[2]/div[1]/div[2]/div/p/span/text()').extract())
        comments.append(response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[10]/div[2]/div[2]/div[1]/div[3]/div/p/span/text()').extract())
        comments.append(response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[10]/div[2]/div[2]/div[1]/div[4]/div/p/span/text()').extract())
        comments.append(response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[10]/div[2]/div[2]/div[1]/div[5]/div/p/span/text()').extract())

        print('name',name)
        print('star',star)
        print('actors',actor)
        print('director',director)
        print('writer',writer)
        print('theme',theme)
        print('country',country)
        print('time',time)
        item['movieName'] = name
        item['movieStar'] = star
        item['movieMainActor'] = actor
        item['movieDirector'] = director
        item['movieWriter'] = writer
        item['movieTheme'] = theme
        item['movieCountry'] = country
        item['moviePlayTime'] = time
        item['movieComments'] = comments
        yield item

        if self.nRound < 249:
            self.nRound += 1
            url = self.contents[self.nRound][10:-3]
            print(url)
       #     yield scrapy.Request(url, callback=self.parse)

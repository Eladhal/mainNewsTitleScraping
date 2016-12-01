# -*- coding: utf-8 -*-
import scrapy
import time
from MainTitles.items import MaintitlesItem

class MaintitleSpider(scrapy.Spider):
    name = "mainTitle"
    allowed_domains = ["news.sky.com","www.foxnews.com","www.bbc.com","www.wsj.com","www.nytimes.com"]
    start_urls = (
        "http://news.sky.com/","http://www.foxnews.com/","http://www.bbc.com/news","http://www.wsj.com/europe","http://www.nytimes.com/"
    )

    def parse(self, response):
        mainTitle = MaintitlesItem()
        if response.url.split('.')[-2] == 'sky':
            mainTitle['name']=response.url.split('.')[-2]
            mainTitle['mainTitle']=response.xpath('.//*[@class="sky-component-story-grid__link"]/text()').extract_first()
            mainTitle['DateTime'] = time.strftime("%d/%m/%Y")+" , "+time.strftime("%H:%M")
        
        elif response.url.split('.')[-2] == 'foxnews':
            mainTitle['name']=response.url.split('.')[-2]
            mainTitle['mainTitle']=response.xpath('//*[@class="primary"]/h1/a/text()').extract_first()
            mainTitle['DateTime'] = time.strftime("%d/%m/%Y")+" , "+time.strftime("%H:%M")
        
        elif response.url.split('.')[-2] == 'bbc':
            mainTitle['name']=response.url.split('.')[-2]
            mainTitle['mainTitle']=str(response.xpath('.//*[@class="title-link__title-text"]/text()').extract_first()).strip()
            mainTitle['DateTime'] = time.strftime("%d/%m/%Y")+" , "+time.strftime("%H:%M")
       
        elif response.url.split('.')[-2] == 'wsj':
            mainTitle['name']=response.url.split('.')[-2]
            mainTitle['mainTitle']=response.xpath('.//*[@class="wsj-headline-link"]/text()').extract_first()
            mainTitle['DateTime'] = time.strftime("%d/%m/%Y")+" , "+time.strftime("%H:%M")
        
        elif response.url.split('.')[-2] == 'nytimes':
            mainTitle['name']=response.url.split('.')[-2]
            mainTitle['mainTitle']=response.xpath('.//*[@class="story-heading"]/a/text()').extract_first()
            mainTitle['DateTime'] = time.strftime("%d/%m/%Y")+" , "+time.strftime("%H:%M")
        
        
        yield mainTitle


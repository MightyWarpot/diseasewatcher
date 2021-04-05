import scrapy
from datetime import datetime, timedelta

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    
    start_urls = [
        'http://outbreaknewstoday.com/brazil-tocantins-records-a-87-drop-in-dengue-in-2020/',
        
    ]
        
    def parse(self, response):
        date = datetime.strptime( response.css('div.datsingle::text').get(), '%B %d, %Y' )
        date2 = datetime.now() - timedelta(days =390)
        print(date)
        print(date2)
        if date > date2:
            yield {
                'title': response.css('div.posttitle').css('h1::text').get(),
                'date': response.css('div.datsingle::text').get(),
                'body': response.css('div.postcontent').css('p::text').getall(),
                'url': response.request.url,
                'region': response.css('div.catsing').css('a::text').get(),
            } 
            nexturls = response.css('div.postcontent').css('ul').getall()
            print(nexturls)
            for href in response.css('div.postcontent').css('ul a::attr(href)'):
                yield response.follow(href, callback=self.parse)
            yield from response.follow_all(css='div.postcontent.ul a', callback=self.parse)
        
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    
    start_urls = [
        'http://outbreaknewstoday.com/china-reports-3-human-h9n2-avian-influenza-cases-68463/',
        
    ]
        
    def parse(self, response):
        
        yield {
            'title': response.css('div.posttitle').css('h1::text').get(),
            'date': response.css('div.datsingle::text').get(),
            'body': response.css('div.postcontent').css('p::text').getall(),
            'url': response.request.url,
        } 
        nexturls = response.css('div.postcontent').css('ul').getall()
        print(nexturls)
        for href in response.css('div.postcontent').css('ul a::attr(href)'):
            yield response.follow(href, callback=self.parse)
        yield from response.follow_all(css='div.postcontent.ul a', callback=self.parse)
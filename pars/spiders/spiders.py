from scrapy.spiders import CrawlSpider
import scrapy
import os

class TitleSpider(CrawlSpider):
    name = u"title"

    def start_requests(self):
        urls = ['http://books.toscrape.com']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        name_book = response.xpath('//li//article//h3//a//@title').extract()
        save_data(name_book)

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def save_data(data):
        filename = 'books_title.txt'
        if os.path.exists('books_title.txt'):
            f = open(filename, 'a')
        else:
            f = open(filename, 'x')
        f.write(data)
        f.close()

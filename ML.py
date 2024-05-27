import scrapy


class MlSpider(scrapy.Spider):
    name = "ML"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/smatphonnes#D[A:smatphonnes]"]

    def parse(self, response):
        pass

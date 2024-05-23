import scrapy


class MlSpider(scrapy.Spider):
    name = "ML"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/smatphonnes#D[A:smatphonnes]"]

    def parse(self, response):
        products = response.css("div.ui-search-result__content-wrapper")

        for product in products:
            yield {
                'loja': product.css('p.ui-search-official-store-label.ui-search-item__group__element.ui-search-color--GRAY::text').get()
            }

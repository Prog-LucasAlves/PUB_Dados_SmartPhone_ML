import scrapy


class MlSpider(scrapy.Spider):
    name = "ML"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/smatphonnes#D[A:smatphonnes]"]
    PAGE_COUNT = 1
    MAX_PAGES = 2

    def parse(self, response):
        products = response.css("div.ui-search-result__content-wrapper")

        for product in products:

            preco_reais = product.css('span.andes-money-amount__fraction::text').getall()

            yield {
                'loja': product.css('p.ui-search-official-store-label.ui-search-item__group__element.ui-search-color--GRAY::text').get(),
                'descricao': product.css('h2.ui-search-item__title::text').get(),
                'old_preco_reais': preco_reais[0] if len(preco_reais) > 0 else None,
            }

        if self.PAGE_COUNT < self.MAX_PAGES:
            next_page = response.css("li.andes-pagination__button.andes-pagination__button--next::attr(href)").get()
            if next_page is not None:
                self.PAGE_COUNT += 1
                yield scrapy.Request(url=next_page, callback=self.parse)

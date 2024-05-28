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
            preco_cents = product.css('andes-money-amount__cents andes-money-amount__cents--superscript-24::text').getall()

            yield {
                'loja': product.css('p.ui-search-official-store-label.ui-search-item__group__element.ui-search-color--GRAY::text').get(),
                'descricao': product.css('h2.ui-search-item__title::text').get(),
                'old_preco_reais': preco_reais[0] if len(preco_reais) > 0 else None,
                'new_price_reais': preco_reais[1] if len(preco_reais) > 1 else None,
                'reviews_rating_number': product.css('span.ui-search-reviews__rating-number::text').get(),
                'reviews_amount': product.css('span.ui-search-reviews__amount::text').get()
            }

        if self.PAGE_COUNT < self.MAX_PAGES:
            next_page = response.css("li.andes-pagination__button.andes-pagination__button--next::attr(href)").get()
            if next_page is not None:
                self.PAGE_COUNT += 1
                yield scrapy.Request(url=next_page, callback=self.parse)

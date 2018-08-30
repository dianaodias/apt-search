import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.vivareal.com.br/imovel/apartamento-3-quartos-botafogo-zona-sul-rio-de-janeiro-com-garagem-94m2-aluguel-RS2600-id-95334649/?__vt=ranking:visit'
            # 'https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/botafogo/apartamento_residencial/?gclid=CjwKCAjwq57cBRBYEiwAdpx0vY_NsDz1kMoxZlxYPsNOsng9qaTQGktpiDt1TwqSDY0TKBvfWj1PdRoCmZcQAvD_BwE&__vt=ranking:visit',
            # 'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_price(self, price_string):
        return int(price_string[3:].replace('.',''))

    def parse(self, response):
        
        rent = response.css('span.js-detail-rent-price::text').extract_first()
        rent = self.parse_price(rent)
        self.log(rent)

        condo_fee = response.css('span.js-detail-condo-price::text').extract_first()
        condo_fee = self.parse_price(condo_fee)
        self.log(condo_fee)


        iptu = response.css('span.js-detail-iptu-price::text').extract_first()
        iptu = self.parse_price(iptu)
        self.log(iptu) 

        rooms = response.css('li.js-detail-rooms span.dc::text').extract_first()
        rooms = int(rooms)
        self.log(rooms)

        # bathrooms = 

        # area = 

        # garage = 

        # description = 

        # street = 

        # street_number =

        # neighborhood =









        # page = response.url.split("/")[-2]
        # filename = 'vivareal.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        # class="dc js-detail-rent-price"
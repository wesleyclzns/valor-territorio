import scrapy

class LoftSpider(scrapy.Spider):
    name = 'QuintoSpider'
    start_urls = ['https://www.quintoandar.com.br/comprar/imovel/sao-paulo-sp-brasil']

    def parse(self, response):
        imovel = response.xpath("*//div[@class='MuiPaper-root MuiCard-root sc-jNMcJZ iCPDBK sc-abggw7-0 iemxZf MuiPaper-elevation1 MuiPaper-rounded']")
        for apto in aptos:
            {
                'link': ("//a[class='sc-15oj7uq-0 iOyGjI']/@href"),
                'tipo-imovel':("//div[@data-testid='house-card-details']/@class='sc-hhh4j4-0 jcHGdu'/span[class='sc-bdfBQB giyFJX sc-hhh4j4-2 dIkUna']/text"),
                'endereço':('data-testid="house-card-address"::text'),
                'endereço-2':('data-testid="house-card-region"::text'),
                'metragem':('data-testid="house-card-area"::text'),
                'quartos':('data-testid="house-card-area"::text'),
                'vagas':('data-testid="house-card-area"::text'),
                'condominio-iptu':('data-testid="house-card-rent"::text'),
                'preço':("//div[@class='sc-m82tat-1 SRBQz']/p[@class=sc-'bdfBQB dxrUpR']/strong/text"),
                
            }


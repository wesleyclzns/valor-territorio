import scrapy

loft = https://loft.com.br/venda/apartamentos/sao-paulo_sp


class LoftSpider(scrapy.Spider):
    name = 'LoftSpider'
    start_urls = ['https://loft.com.br/venda/apartamentos/sao-paulo_sp']

    def parse(self, response):
        imovel = response.xpath("*//div[@class='MuiPaper-root MuiCard-root jss488 MuiPaper-elevation0 MuiPaper-rounded']")
        for apto in aptos:
            {
                'link': apto.xpath("@href").get
                'valor':
                'endereço':
                'metragem':
                'quartos':
                'vagas':
                'propriedade_loft':
            }
imovel.xpath("*//p[@class='MuiTypography-root jss280 jss257 jss269 jss551 jss552 MuiTypography-body1 MuiTypography-noWrap']/text")


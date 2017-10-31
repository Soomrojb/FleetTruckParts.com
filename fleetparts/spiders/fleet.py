# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.utils.response import open_in_browser

BaseURL = "http://www.fleettruckparts.com"

class FleetSpider(scrapy.Spider):
    name = 'fleetp'
    allowed_domains = ['fleettruckparts.com']
    start_urls = [BaseURL]

    def parse(self, response):
        for Category in response.xpath("//td[@class='textboldnolink']/../../tr"):
            Category_Title = Category.xpath("./td[2]/a/text()")[0].extract()
            Category_Href = BaseURL + Category.xpath("./td[2]/a/@href")[0].extract()
            MetaData = {
                "Category_Title"   : Category_Title,
                "Category_Href"    : Category_Href
            }
            yield scrapy.Request(Category_Href, dont_filter=True, meta=MetaData, callback=self.screenpg)
    
    def screenpg(self, response):
        for Product in response.xpath("//div[@class='item-list-home']"):
            Price = Product.xpath("./div[@class='item-price']").extract()
            NextLink = BaseURL + Product.xpath("./div[@class='item-name']/a/@href")[0].extract()
            MetaData = {
                "Category_Title"   : response.meta['Category_Title'], 
                "Category_Href"    : response.meta['Category_Href']
            }
            if Price:
                yield scrapy.Request(NextLink, dont_filter=True, meta=MetaData, callback=self.detailpg)
            else:
                yield scrapy.Request(NextLink, dont_filter=True, meta=MetaData, callback=self.screenpg)
        try:
            CurrentPg = response.xpath("//td[@class='bglt medtextbold']/text()")[0].extract()
        except:
            CurrentPg = 0
        if CurrentPg != 0:
            TestElement = response.xpath("//td[@class='medtext']/text()").extract()
            if TestElement:
                NextpgNum = response.xpath("//td[@class='medtext']/following-sibling::td[2]/text()").extract()
                if NextpgNum:
                    NextpgHref = BaseURL + response.xpath("//td[@class='medtext']/following-sibling::td/a/@href")[0].extract()
                    yield scrapy.Request(NextpgHref, dont_filter=True, meta=response.meta, callback=self.screenpg)
        
    def detailpg(self, response):
        Title = response.xpath("//div[@class='it-name']/text()")[0].extract()
        Price = response.xpath("//input[@id='amount']/@value").extract()
        PartNum = response.xpath("//div[@class='it-dsc-tit' and text()='Part #:']/../div[@class='it-dsc-txt']/text()").extract()
        Make = response.xpath("//div[@class='it-dsc-tit' and text()='Make:']/../div[@class='it-dsc-txt']/text()").extract()
        Model = response.xpath("//div[@class='it-dsc-tit' and text()='Model:']/../div[@class='it-dsc-txt']/text()").extract()
        Fits = response.xpath("//div[@class='it-dsc-tit' and text()='Fits:']/../div[@class='it-dsc-txt']/text()").extract()
        OEM = response.xpath("//div[@class='it-dsc-tit' and text()='OEM Cross Part #:']/../div[@class='it-dsc-txt']/text()").extract()
        AfterMarket = response.xpath("//div[@class='it-dsc-tit' and text()='Aftermarket Cross Part #:']/../div[@class='it-dsc-txt']/text()").extract()
        Addionalinfo = response.xpath("//div[@class='it-dsc-tit' and text()='Additional Info:']/../div[@class='it-dsc-txt']/text()").extract()
        Alert = response.xpath("//div[@class='it-dsc-tit' and text()='Alert!']/../div[@class='it-dsc-txt']/text()").extract()
        Material = response.xpath("//div[@class='it-dsc-tit' and text()='Material:']/../div[@class='it-dsc-txt']/text()").extract()
        Condition = response.xpath("//div[@class='it-dsc-tit' and text()='Condition:']/../div[@class='it-dsc-txt']/text()").extract()
        Manufacturer = response.xpath("//div[@class='it-dsc-tit' and text()='Manufacturer:']/../div[@class='it-dsc-txt']/text()").extract()
        MadeIN = response.xpath("//div[@class='it-dsc-tit' and text()='Made in:']/../div[@class='it-dsc-txt']/text()").extract()
        StockStatus = response.xpath("//div[@class='it-dsc-tit' and text()='Stock Status:']/../div[@class='it-dsc-txt']/text()").extract()
        ProductLength = response.xpath("//div[@class='it-dsc-tit' and text()='Product Length:']/../div[@class='it-dsc-txt']/text()").extract()
        ProductHeight = response.xpath("//div[@class='it-dsc-tit' and text()='Product Height:']/../div[@class='it-dsc-txt']/text()").extract()
        ProductWidth = response.xpath("//div[@class='it-dsc-tit' and text()='Product Width:']/../div[@class='it-dsc-txt']/text()").extract()
        ProductDiameter = response.xpath("//div[@class='it-dsc-tit' and text()='Product Diameter:']/../div[@class='it-dsc-txt']/text()").extract()
        ProductWeight = response.xpath("//div[@class='it-dsc-tit' and text()='Product Weight:']/../div[@class='it-dsc-txt']/text()").extract()
        ShipsVia = response.xpath("//div[@class='it-dsc-tit' and text()='Ships via:']/../div[@class='it-dsc-txt']/text()").extract()
        ShipsClass = response.xpath("//div[@class='it-dsc-tit' and text()='Ship Class:']/../div[@class='it-dsc-txt']/text()").extract()
        ShippingWeight = response.xpath("//div[@class='it-dsc-tit' and text()='Shipping Weight:']/../div[@class='it-dsc-txt']/text()").extract()
        ShippingLength = response.xpath("//div[@class='it-dsc-tit' and text()='Shipping Length:']/../div[@class='it-dsc-txt']/text()").extract()
        ShippingHeight = response.xpath("//div[@class='it-dsc-tit' and text()='Shipping Height:']/../div[@class='it-dsc-txt']/text()").extract()
        ShippingWidht = response.xpath("//div[@class='it-dsc-tit' and text()='Shipping Widht:']/../div[@class='it-dsc-txt']/text()").extract()
        ImageURL = response.xpath("//div[@id='custimg1']/a/img/@src").extract()
        yield {
            "URL" : response.url,
            "Category Title" : response.meta['Category_Title'],
            "Category Href" : response.meta['Category_Href'],
            "Price" : Price,
            "Title" : Title,
            "Part Number" : PartNum,
            "Make" : Make,
            "Model" : Model,
            "Fits" : Fits,
            "OEM" : OEM,
            "After Market" : AfterMarket,
            "Addional info" : Addionalinfo,
            "Alert" : Alert,
            "Material" : Material,
            "Condition" : Condition,
            "Manufacturer" : Manufacturer,
            "Made In" : MadeIN,
            "Stock Status" : StockStatus,
            "Product Length" : ProductLength,
            "Product Height" : ProductHeight,
            "Product Width" : ProductWidth,
            "Product Diameter" : ProductDiameter,
            "Product Weight" : ProductWeight,
            "Ships Via" : ShipsVia,
            "Ships Class" : ShipsClass,
            "Shipping Weight" : ShippingWeight,
            "Shipping Length" : ShippingLength,
            "Shipping Height" : ShippingHeight,
            "Shipping Widht" : ShippingWidht,
            "Image URL" : ImageURL
        }


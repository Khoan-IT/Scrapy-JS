import scrapy
from scrapy_splash import SplashRequest
from demo_scrapy.items import ProductItem
 
class ShopeeCrawlSpider(scrapy.Spider):
    name = 'shopee_crawl'
    allowed_domains = ['shopee.vn']
    start_urls = ['https://shopee.vn/shop/88201679/search']
    
    render_script = """
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(5))
 
            return {
                html = splash:html(),
                url = splash:url(),
            }
        end
        """ 
 
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url,
                self.parse, 
                endpoint='render.html',
                args={
                    'wait': 5,
                    'lua_source': self.render_script,
                }
            )
    
    def parse(self, response):
        item = ProductItem()
        
        for product in response.css("div.shop-search-result-view__item"):
            item["name"] = product.css("div._36CEnF ::text").extract_first()
            item["price"] = product.css("div._3_-SiN ::text").extract_first()
            item["price_sale"] = product.css("span._29R_un ::text").extract_first()
            item["sold"] = product.css("div.go5yPW ::text").extract_first()
            
            yield item 
import scrapy
from scrapy_splash import SplashRequest
from demo_scrapy.items import PItem

class CrawlMaccareSpider(scrapy.Spider):
    name = 'Crawl_MacCare'
    allowed_domains = ['giayla.com']
    start_urls = ['https://giayla.com/collections/giay-the-thao-nam/']

    render_script = """
            function main(splash)
                local url = splash.args.url

                assert(splash:go(url))
                assert(splash:wait(5))

                local scroll_screen = splash:jsfunc([[
                  function () {
                      return document.body.scrollHeight
                  }
                ]])
                local last_scroll_height = 0
                local scroll_height = scroll_screen()
                assert(splash:wait(3))
                while last_scroll_height < scroll_height do
                    last_scroll_height = scroll_height
    								splash.scroll_position = {y = scroll_height}
                    scroll_height = scroll_screen()
                    assert(splash:wait(3))
                end
                
                return {
                    html = splash:html(),
                }
            end
    """

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url,
                self.parse, 
                endpoint='execute',
                args={
                    'lua_source': self.render_script,
                }
            )

    def parse(self, response):
        f = open("Source.html",'w')
        f.write(response.text)
        item  = PItem()

        for P in response.css("div.col-lg-3.col-md-3.col-sm-4.col-xs-6.product-wrapper.product-resize.animated.zoomIn.fixheight"):
            item['name'] = P.css("div.product-info > a > h2 ::text").extract_first().replace("\t", "").replace("\n","")
            item['price'] = P.css("div.price-new-old span ::text").extract_first()

            yield item

            

            



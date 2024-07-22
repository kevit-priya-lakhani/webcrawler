
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from scrapy.crawler import CrawlerProcess



class LinkItem(scrapy.Item):
    link = scrapy.Field()


class ExampleSpider(CrawlSpider):
    name = "my crawler"

    #only scrape on pages within the example.co.uk domain
    allowed_domains = ["ranveerbrar.com"]

    #start scraping on the site homepage once credentials have been authenticated
    start_urls=["https://ranveerbrar.com/"]

    seen_urls = set()
    #rules for recursively scraping the URLS found
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True,
                deny=('comment','respond','jpg'),
                allow_domains=('ranveerbrar.com')
            ),
            follow=True,
            callback="parse_url"
        )
    ]

    #method to identify hyperlinks by xpath and extract hyperlinks as scrapy items
    def parse_url(self, response):
        for element in response.xpath('//a'):
            oglink = element.xpath('@href').get()
            #need to add on prefix as some hrefs are not full https URLs and thus cannot be followed for scraping
            if "http" not in str(oglink):
                full_url = "https://ranveerbrar.com/" + oglink
            else:
                full_url = oglink

            disallow_urls=['comment','respond','#','jpg','pdf','post','page','jpeg','png']

            for word in disallow_urls:
                if word in full_url:
                    full_url=None
                    break

            if full_url:
                if full_url not in self.seen_urls and 'https://ranveerbrar.com/' in full_url:
                    self.seen_urls.add(full_url)
                    
                    item = LinkItem()

                    item['link']=full_url
                    
                    yield item

if __name__=='__main__':
    process= CrawlerProcess()
    process.crawl(ExampleSpider)
    process.start()
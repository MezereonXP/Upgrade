import scrapy
import time
import Upgrade.items as items
from scrapy.contrib.spiders import CrawlSpider, Rule
class csdnSpider(CrawlSpider):

    name = "csdn"
    start_urls = ['https://blog.csdn.net/qq_34206952']
    url = 'https://blog.csdn.net/qq_34206952'

    def parse(self, response):
        item = items.UpgradeItem()
        for temp in response.css('.grade-box dl:nth-child(2) dd'):
            jobMessage = temp.css('::attr(title)').extract()
            item['visit'] = jobMessage
        for temp in response.css('.grade-box dl:nth-child(4)'):
            jobMessage = temp.css('::attr(title)').extract()
            item['rank'] = jobMessage
            import time

        f = open('./history' + time.strftime("%Y-%m", time.localtime()), 'a+')
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ';' + item['visit'][0])
        f.write(';')
        f.write(item['rank'][0])
        f.write('\n')
        f.close()
        return item

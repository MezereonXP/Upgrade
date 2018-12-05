import scrapy
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
        f = open('./history', 'a+')
        f.write(item['visit'][0])
        f.write(';')
        f.write(item['rank'][0])
        f.write('\n')
        f.close()
        return item
        # selector = Selector(response)
        # ....
        # response就是返回的网页数据
        # 处理好的数据放在items中，在items.py设置好你要处理哪些数据字段，这里我们抓取文章标题，url，作者，阅读数，喜欢，打赏数
        ## 解析处理数据的地方，用xpath解析处理数据
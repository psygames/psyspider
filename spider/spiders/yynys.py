# -*- coding: utf-8 -*-
from spider.items import *
from spider import db
from spider import tools
from datetime import datetime


# 悠悠鸟影视
def find(node, xpath, split=None):
    res = node.xpath(xpath).extract()
    if split is not None:
        if len(res) == 0:
            return []
        return res[0].strip().split(split)
    if len(res) == 0:
        return None
    return res[0].strip()


class YynysSpider(scrapy.Spider):
    name = "yynys"
    allowed_domains = ["csdn.net"]
    start_urls = []
    for i in range(16000, 70000):
        start_urls.append(f'http://yynys.com/vod-detail-id-{i}.html')

    # new
    printer = tools.Printer()
    crawl_count = 0
    hit_count = 0

    def parse(self, response):
        self.crawl_count += 1
        if response.text.find('获取数据失败，请勿非法传递参数') != -1:
            self.print_status()
            return
        self.hit_count += 1
        info = response.xpath('//div[@class="info"]')
        _id = response.url[response.url.rfind('-') + 1:-5]
        title = find(info, 'h1/text()')
        year = int(find(info, 'ul/li[1]/text()[1]'))
        state = find(info, 'ul/li[1]/text()[2]')
        tags = find(info, 'ul/li[1]/text()[3]', '，')
        cast = find(info, 'ul/li[2]/text()', ',')
        category = find(info, 'ul/li[3]/a/text()')
        area = find(info, 'ul/li[4]/text()')
        update_date = datetime.strptime(find(info, 'ul/li[5]/div/text()[1]'), '%Y-%m-%d').date()
        alias = find(info, 'ul/li[2]/text()[2]', ',')
        hot = find(info, '//em[@id="hits"]')
        story = find(info, '//div[@class="endtext"]/div/text()')

        mox = response.xpath('//table[@style="border-bottom: 1px solid #f2f2f2;"]')
        _mox_len = len(mox.extract())
        for
        mox = mox.xpath('tbody/tr/td[1]/table/tbody/tr/td/div/ul')
'//table/tbody/tr/td[1]/table/tbody/tr/td/div/ul'
'//*[@id="main"]/div[2]/div[6]/div[2]/div/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/div/input'
        self.print_status()

    def print_status(self):
        tags = ['Crawl', 'Hit']
        vals = [self.crawl_count, self.hit_count]
        self.printer.print(tags, vals)

import os
import re
import scrapy
import shutil
import scrapy
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess

try:
    shutil.rmtree("html")
except:
    pass
os.mkdir("html")

class CJSpider(scrapy.Spider):
    name = "cj"
    start_urls = ['https://jobs.cj.com/jobs/city/santa-barbara#/']

    def parse(self, response):
        next_pages = response.css('#conversant-table a::attr(href)').getall()
        next_pages = ["https://jobs.cj.com" + x for x in next_pages if "/jobs/category/" not in x]
        next_pages = list(set(next_pages))
        for href in next_pages:
            yield response.follow(href, self.parse_new_page)

    def parse_new_page(self, response):
        page = response.url.split("/")[-2]
        filename = 'html/{}_{}.html'.format(self.name, page)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}_{}.html".format(self.name, page, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class RaytheonSpider(scrapy.Spider):
    name = "raytheon"
    start_urls = ['https://jobs.raytheon.com/search-jobs/United%20States?orgIds=4679&ac=22812&alp=6252001&alt=2&p=1',
                  'https://jobs.raytheon.com/search-jobs/United%20States?orgIds=4679&ac=22812&alp=6252001&alt=2&p=2',
                  'https://jobs.raytheon.com/search-jobs/United%20States?orgIds=4679&ac=22812&alp=6252001&alt=2&p=3',
                  'https://jobs.raytheon.com/search-jobs/United%20States?orgIds=4679&ac=22812&alp=6252001&alt=2&p=4',
                  'https://jobs.raytheon.com/search-jobs/United%20States?orgIds=4679&ac=22812&alp=6252001&alt=2&p=5',
                  'https://jobs.raytheon.com/search-jobs/United%20States?orgIds=4679&ac=22812&alp=6252001&alt=2&p=6',
                  'https://jobs.raytheon.com/search-jobs/United%20States?orgIds=4679&ac=22812&alp=6252001&alt=2&p=7',
                  'https://jobs.raytheon.com/search-jobs/United%20States?orgIds=4679&ac=22812&alp=6252001&alt=2&p=8',
                  'https://jobs.raytheon.com/search-jobs/United%20States?orgIds=4679&ac=22812&alp=6252001&alt=2&p=9']

    def parse(self, response):
        next_pages = response.css('#search-results-list a::attr(href)').getall()
        next_pages = ["https://jobs.raytheon.com" + x for x in next_pages if x != "#"]
        next_pages = list(set(next_pages))
        for href in next_pages:
            yield response.follow(href, self.parse_new_page)

    def parse_new_page(self, response):
        page = response.url.split("/")[-2]
        if "search-jobs" in page:
            return
        filename = 'html/{}_{}.html'.format(self.name, page)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}_{}.html".format(self.name, page, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class InogenSpider(scrapy.Spider):
    name = "inogen"
    start_urls = ['https://inogen.applicantpro.com/jobs/']

    def parse(self, response):
        next_pages = response.css('.job-listings a::attr(href)').getall()
        next_pages = list(set(next_pages))
        for href in next_pages:
            yield response.follow(href, self.parse_new_page)

    def parse_new_page(self, response):
        page = response.url.split("/")[-2]
        filename = 'html/{}_{}.html'.format(self.name, page)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}_{}.html".format(self.name, page, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class SonosSpider(scrapy.Spider):
    name = "sonos"
    start_urls = ['https://careers.sonos.com/jobs/SearchJobs/?3_72_3=%5B%2215814%22%5D']

    def parse(self, response):
        next_pages = response.css('.group a::attr(href)').getall()
        next_pages = [x for x in next_pages if x != "#" and "facebook" not in x and "share" not in x]
        next_pages = list(set(next_pages))
        for href in next_pages:
            yield response.follow(href, self.parse_new_page)

    def parse_new_page(self, response):
        page = response.url.split("/")[-2]
        if page == "en":
            return
        filename = 'html/{}_{}.html'.format(self.name, page)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}_{}.html".format(self.name, page, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class D2TechSpider(scrapy.Spider):
    name = "d2tech"
    start_urls = ['https://www.d2tech.com/careers']

    def parse(self, response):
        filename = 'html/{}.html'.format(self.name)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}.html".format(self.name, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class YardiSpider(scrapy.Spider):
    name = "yardi"
    start_urls = ['https://careers.yardi.com/openings/?loc=1157']

    def parse(self, response):
        next_pages = response.css('#resultsList a::attr(href)').getall()
        next_pages = list(set(next_pages))
        for href in next_pages:
            yield response.follow(href, self.parse_new_page)

    def parse_new_page(self, response):
        page = response.url.split("/")[-2]
        if page == "en":
            return
        filename = 'html/{}_{}.html'.format(self.name, page)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}_{}.html".format(self.name, page, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class ImpactSpider(scrapy.Spider):
    name = "impact"
    start_urls = ['https://talent.impact.com/jobs/santa-barbara/#']

    def parse(self, response):
        filename = 'html/{}.html'.format(self.name)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}.html".format(self.name, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class GHSSpider(scrapy.Spider):
    name = "ghs"
    start_urls = ['https://www.ghs.com/jobs_usa.html']

    def parse(self, response):
        filename = 'html/{}.html'.format(self.name)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}.html".format(self.name, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class OntraPortSpider(scrapy.Spider):
    name = "ontraport"
    start_urls = ['https://ontraport.com/careers/jobs/engineering']

    def parse(self, response):
        filename = 'html/{}.html'.format(self.name)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}.html".format(self.name, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class RipTideSpider(scrapy.Spider):
    name = "riptide"
    start_urls = ['https://riptideio.com/careers-join-us/']

    def parse(self, response):
        filename = 'html/{}.html'.format(self.name)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}.html".format(self.name, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

# Launch spiders
process = CrawlerProcess()
process.crawl(CJSpider)
process.crawl(RaytheonSpider)
process.crawl(InogenSpider)
process.crawl(SonosSpider)
process.crawl(D2TechSpider)
process.crawl(YardiSpider)
process.crawl(ImpactSpider)
process.crawl(GHSSpider)
process.crawl(OntraPortSpider)
process.crawl(RipTideSpider)
process.start()

# Extracting Text
text = []
for filename in os.listdir("html"):
    html = open("html/{}".format(filename)).read()
    soup = BeautifulSoup(html)
    for script in soup(["script", "style"]):
        script.decompose()
    text.append(soup.get_text())
with open('../../data/processed/text.txt', 'w') as file:
    file.write(" ".join(text))

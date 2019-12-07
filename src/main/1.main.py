import os
import re
import scrapy
import shutil
import scrapy
from scrapy.crawler import CrawlerProcess

try:
    shutil.rmtree("html")
except:
    pass
os.mkdir("html")

# start_urls = [
#     'https://curvature.wd5.myworkdayjobs.com/External/1/refreshFacet/318c8bb6f553100021d223d9780d30be',
#     'https://inogen.applicantpro.com/jobs/', # goleta only
#     'https://careers.sonos.com/jobs/SearchJobs/?3_72_3=%5B%2215814%22%5D',
#     'https://flexerasoftware.wd1.myworkdayjobs.com/FlexeraSoftware/1/refreshFacet/318c8bb6f553100021d223d9780d30be',
#     'https://www.transphormusa.com/en/company/#careers',
#     'https://www.d2tech.com/careers',
#     'https://www.appfolioinc.com/jobs-openings', # santa barbara only
#     'https://careers.yardi.com/openings/?loc=1157',
#     'https://www.invoca.com/company/careers/#job_listing', # santa barbara only
#     'https://talent.impact.com/jobs/santa-barbara/#',
#     'https://www.logicmonitor.com/careers/',
#     'https://www.ghs.com/jobs_usa.html',
#     'https://ontraport.com/careers/jobs/engineering',
#     'https://riptideio.com/careers-join-us/',
#     'https://hginsights.com/careers/',
#     'https://novacoast.com/jobs/', # SB only
# ]



class CJSpider(scrapy.Spider):
    name = "job_listings"
    start_urls = ['https://jobs.cj.com/jobs/city/santa-barbara#/']

    def parse(self, response):
        next_pages = response.css('#conversant-table a::attr(href)').getall()
        next_pages = ["https://jobs.cj.com" + x for x in next_pages if "/jobs/category/" not in x]
        for href in next_pages:
            yield response.follow(href, self.parse_listing)

    def parse_listing(self, response):
        page = response.url.split("/")[-2]
        filename = 'html/cj_{}.html'.format(page)
        i = 2
        while os.path.exists(filename):
            filename = "html/cj_{}_{}.html".format(page, i)
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class RaytheonSpider(scrapy.Spider):
    name = "job_listings"
    start_urls = ['https://jobs.raytheon.com/search-jobs/United%20States?orgIds=4679&ac=22812&alp=6252001&alt=2']

    def parse(self, response):
        next_pages = response.css('#search-results-list a::attr(href)').getall()
        next_pages = ["https://jobs.raytheon.com" + x for x in next_pages if x != "#"]
        for href in next_pages:
            yield response.follow(href, self.parse_listing)

    def parse_listing(self, response):
        page = response.url.split("/")[-2]
        filename = 'html/{}.html'.format(page)
        i = 2
        while os.path.exists(filename):
            filename = "html/raytheon_{}_{}.html".format(page, i)
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))



process = CrawlerProcess()
process.crawl(CJSpider)
process.crawl(RaytheonSpider)
process.start() # the script will block here until all crawling jobs are finished

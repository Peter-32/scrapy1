import scrapy


class JobListingsSpider(scrapy.Spider):
    name = "job_listings"

    def start_requests(self):
        urls = [
            'https://www.qad.com/about/careers/job-search',
            'https://jobs.cj.com/jobs/city/santa-barbara#/',
            'https://jobs.raytheon.com/search-jobs/United%20States?orgIds=4679&ac=22812&alp=6252001&alt=2',
            'https://curvature.wd5.myworkdayjobs.com/External/1/refreshFacet/318c8bb6f553100021d223d9780d30be',
            'https://inogen.applicantpro.com/jobs/', # goleta only
            'https://careers.sonos.com/jobs/SearchJobs/?3_72_3=%5B%2215814%22%5D',
            'https://flexerasoftware.wd1.myworkdayjobs.com/FlexeraSoftware/1/refreshFacet/318c8bb6f553100021d223d9780d30be',
            'https://www.transphormusa.com/en/company/#careers',
            'https://www.d2tech.com/careers',
            'https://www.appfolioinc.com/jobs-openings', # santa barbara only
            'https://careers.yardi.com/openings/?loc=1157',
            'https://www.invoca.com/company/careers/#job_listing', # santa barbara only
            'https://talent.impact.com/jobs/santa-barbara/#',
            'https://www.logicmonitor.com/careers/',
            'https://www.ghs.com/jobs_usa.html',
            'https://ontraport.com/careers/jobs/engineering',
            'https://riptideio.com/careers-join-us/',
            'https://hginsights.com/careers/',
            'https://novacoast.com/jobs/', # SB only


        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


# https://www.naukri.com/job-listings

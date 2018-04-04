import scrapy
import json
import random
from graduate_scrapy.items import Lagou
import graduate_scrapy.settings
import pymysql
from twisted.enterprise import adbapi
class lagouSpider(scrapy.Spider):
    name = 'lagou'
    def __init__(self,job = None, *args, **kwargs):
        self.job = job
        self.url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0"
        self.page = 30
        settings = graduate_scrapy.settings.MYSQL_SETTING
        dbparams = dict(
            host=settings['host'],
            db=settings['db'],
            user=settings['user'],
            passwd=settings['password'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        self.mysqlConnection = adbapi.ConnectionPool('pymysql', **dbparams)

    def _conditional_delete(self, tx):
        table = self.job
        for title in graduate_scrapy.settings.JOB_MAPPING_TABLE.keys():
            if self.job == title:
                table = graduate_scrapy.settings.JOB_MAPPING_TABLE[title]
        sql = "delete from %s"%table
        tx.execute(sql)
    def start_requests(self):
        self.mysqlConnection.runInteraction(self._conditional_delete)
        for i in range(self.page+1):
            if (i == 0):
                continue
            formdata = {'first': 'true', 'pn': str(i), 'kd': self.job}
            if (i  > 1):
                formdata = {'first': 'false', 'pn': str(i), 'kd': self.job}
            yield scrapy.FormRequest(self.url, callback=self.parseJson, formdata=formdata)
    def parseJson(self, response):
         self.jsonresponse = json.loads(response.body_as_unicode())['content']['positionResult']['result']
         for item in self.jsonresponse:
             job = Lagou()
             job['title'] = self.job
             job['city'] = item['city']
             job['salary'] = item['salary']
             job['shortName'] = item['companyShortName']
             job['positionName'] = item['positionName']
             job['workYear'] = item['workYear']
             job['education'] = item['education']
             job['companyLabelList'] = str(item['companyLabelList'])[1:-1].replace('\'','')
             yield job

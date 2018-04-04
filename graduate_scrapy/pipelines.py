# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import graduate_scrapy.settings
import pymysql
from twisted.enterprise import adbapi
class GraduateScrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('jobs.json', 'w', encoding="utf-8")
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False, )
        self.file.write(lines)
        return item
    def spider_closed(self, spider):
        self.file.close()

class SaveInMysql(object):
    def __init__(self):
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
        self.mysqlConnection = adbapi.ConnectionPool('pymysql',**dbparams)

    def process_item(self, item, spider):
        query = self.mysqlConnection.runInteraction(self._conditional_insert, item)
        return item
    def _conditional_insert(self, tx, item):
        for title in graduate_scrapy.settings.JOB_MAPPING_TABLE.keys():
            if (item['title'] == title):
                item['title'] = graduate_scrapy.settings.JOB_MAPPING_TABLE[title]
        sql = "insert into %s (city,salary,shortName,positionName,workYear,education,companyLabelList) " \
              "values ('%s','%s','%s','%s','%s','%s','%s')" % (item['title'],item['city'], item['salary'], item['shortName'],
                                                               item['positionName'], item['workYear'],
                                                               item['education'],
                                                               item['companyLabelList'])
        tx.execute(sql)

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs,json
import pymysql

mhost='cdb-mzvws756.cd.tencentcdb.com'
muser='spider'
mpassword='zxc123!@#'
mport=10143
mdb = 'spider_data'

class DoubanmoivescrapyPipeline(object):
    def __init__(self):
        print('------------------init-------------------')
        self.connect = pymysql.connect(host=mhost, user=muser, password=mpassword, db=mdb, port=mport)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        print('------------------procesing-------------------')
        insert_sql = """
        insert into movie_type (movie_type_name) VALUES(%s)
        """
        self.cursor.execute(insert_sql, (item['type']))
        self.connect.commit()

    def spider_closed(self, spider):
        print('----------------closed---------------')
        self.cursor.close()
        self.connect.close()
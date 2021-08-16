# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class OnePipeline:
    def process_item(self, item, spider):
        return item
    # conn = None
    # cursor=None
    #
    # def open_spider(self,spider):
    #     self.conn=pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='123456',db='wangyi',charset='utf8')
    # def process_item(self, item, spider):
    #     self.cursor=self.conn.cursor()
    #     try:
    #         # self.cursor.execute('insert into db(tt,aa) values("%s","%s")' % (item['title'],item['content']))
    #         self.cursor.execute('insert into wang(title,content) values("%s","%s")'%(item['title'],item['content']))
    #         self.conn.commit()
    #     except Exception as e:
    #         print(e)
    #         self.conn.rollback()
    #     return item
    # def close_spider(self,spider):
    #     self.conn.close()
    #     self.cursor.close()

class MysqlPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='wangyi',
                                    charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            # self.cursor.execute('insert into db(tt,aa) values("%s","%s")' % (item['title'],item['content']))
            self.cursor.execute('insert into wang(title,content) values("%s","%s")' % (item['title'], item['content']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.conn.close()
        self.cursor.close()
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
class ThreePipeline:
    def process_item(self, item, spider):
        return item   # 传递给下一个即将被执行的管道类
class MysqlPipeline:
    conn=None
    cursor=None
    def open_spider(self,spider):
        self.conn=pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='123456',db='db')
        # 创建链接对象
    def process_item(self,item,spider):
        self.cursor=self.conn.cursor()   # 创建游标对象
        try:
            self.cursor.execute()  #加上sql语句
            self.conn.commit()  #数据提交
        except Exception as a:
            print(a)
            self.conn.rollback()   #有异常数据回滚
        return item  # 传递给下一个即将被执行的管道类
    def close_spider(self,spider):
        self.conn.close()
        self.cursor.close()

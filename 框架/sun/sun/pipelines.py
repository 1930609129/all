# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SunPipeline:
    def process_item(self, item, spider):
        if item.__class__.__name__ == 'DetailItem':
            content = item['content']
            id = item['id']
            print(content,id)
        else:
            title = item['title']
            id = item['id']
            print(title,id)
        return item

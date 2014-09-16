# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from models import Ads, db_connect, create_ads_table


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BlocketPipeline(object):
    
    def __init__(self):
        """Initialize database connection and sessionmaker, create ads table."""
        engine = db_connect()
        create_ads_table(engine)
        self.Session = sessionmaker(bind=engine)
        
    def process_item(self, item, spider):
        """ Save ads in the database """
        session = self.Session()
        ad = Ads(**item)
        try:
            session.add(ad)
            session.commit()
        except:
            session.rollback()      
            raise 
        finally:
            session.close()

        return item


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.engine.url import URL 

import settings


DeclarativeBase = declarative_base()



def db_connect():
	"""
	Performs database connection using database settings from settings.py
	Returns sqlalchemy engine instance
	"""
	return create_engine(URL(**settings.DATABASE))


def create_ads_table(engine):
	""""""
	DeclarativeBase.metadata.create_all(engine)

def Ads(DeclarativeBase):
	"""Sqlalchemy ads model"""
	__tablename__ = "ads"

	id = Column(Integer, primary_key=True)
	name = Column('name', String, nullable=True)
	link = Column('link', String, nullable=True)
	price = Column('price', String, nullable=True)
	area = Column('area', String, nullable=True)
	date = Column('date', String, nullable=True)
	time = Column('time', String, nullable=True)
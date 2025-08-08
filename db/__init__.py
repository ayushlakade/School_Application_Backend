import os.path

from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import pymysql

from config_parser import parse_file

file_path=os.path.dirname(__file__)
print(file_path)
config_details=parse_file(os.path.join(file_path,'../db_connection.json'))

if not config_details:
    raise RuntimeError('Unable to open db_connection file')

DB_USER=config_details['DB_USER']
DB_PASSWORD=config_details['DB_PASSWORD']
DB_IP=config_details['DB_IP']  #localhost or 127.0.0.1
DB_PORT=3306
DB_NAME=config_details['DB_NAME']


#Initial Engine (Database Exists)
base_engine=create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_IP}:{DB_PORT}/{DB_NAME}",echo=True)
Session=sessionmaker(bind=base_engine)

#Define ORM Base & Table
Base=declarative_base()

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()


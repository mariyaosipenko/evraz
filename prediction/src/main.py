import time
import random

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, MetaData, Time

db_name = 'goland'
db_user = 'goland'
db_pass = 'goland'
db_host = '127.0.0.1'
db_port = '5432'

# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
engine = create_engine(db_string)
connection = engine.connect()
meta = MetaData()


def add_new_table():
    new_table = Table(
        'predict', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('prediction_data', Time),
    )
    meta.create_all(engine)


# def get_last_row():
# pass


if __name__ == '__main__':
    print('Application started')

    # while True:
    add_new_table()
        # time.sleep(5)
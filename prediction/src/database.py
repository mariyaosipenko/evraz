from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, Time
import pandas as pd
import os


class DataBase:
    def __init__(self):
        db_name = 'goland'
        db_user = 'goland'
        db_pass = 'goland'
        db_host = os.getenv("DD_DB_HOST")
        if db_host == '':
            db_host = '127.0.0.1'

        db_port = '5432'

        db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
        self.engine = create_engine(db_string)
        # connection = self.engine.connect()
        self.meta = MetaData()
        self.info_table = Table('info', self.meta, autoload_with=self.engine)
        self.last_date_load = '2023-02-19'  # дата последней выгрузки данных, нужно для загрузки только новых строк

    def add_new_table(self):
        new_table = Table(
            'prediction', self.meta,
            Column('exgauster', Integer, primary_key=True),
            Column('time', Time),
            Column('prediction_data', Time),
        )
        self.meta.create_all(self.engine)

    def get_last_rows(self):
        with self.engine.connect().execution_options(autocommit=True) as conn:

            # df = pd.read_sql(f"""SELECT * FROM info WHERE typename_id=1 and podtype_id=1 or podtype_id=0""", con=conn)
            df = pd.read_sql(f"""SELECT * FROM kafkainfo INNER JOIN info ON kafkainfo.code_id = info.id 
            WHERE kafkainfo.time > '{self.last_date_load}' 
            and info.typename_id = 2 
            and info.podtype_id = ANY(ARRAY[4, 5])""", con=conn, parse_dates=['time'])

            if len(df) > 0:
                self.last_date_load = df['time'].max()
        return df

    def add_new_rows(self, df):
        with self.engine.connect().execution_options(autocommit=True) as conn:
            df.to_sql('prediction', con=conn, index=False, if_exists='append')

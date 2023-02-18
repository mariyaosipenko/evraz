from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, Time
import pandas as pd


class DataBase:
    def __init__(self, docker=1):
        db_name = 'goland'
        db_user = 'goland'
        db_pass = 'goland'
        if docker:
            db_host = 'db'
        else:
            db_host = '127.0.0.1'

        db_port = '5432'

        db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
        self.engine = create_engine(db_string)
        # connection = self.engine.connect()
        self.meta = MetaData()
        self.info_table = Table('info', self.meta, autoload_with=self.engine)

    def add_new_table(self):
        new_table = Table(
            'prediction', self.meta,
            Column('code_id', Integer, primary_key=True),
            Column('time', Time),
            Column('prediction_data', Time),
        )
        self.meta.create_all(self.engine)

    def get_last_rows(self):
        with self.engine.connect().execution_options(autocommit=True) as conn:

            df = pd.read_sql(f"""SELECT * FROM info WHERE typename_id=1 and podtype_id=1 or podtype_id=0""", con=conn)
        print(df)
        return df

    def add_new_rows(self, df):
        with self.engine.connect().execution_options(autocommit=True) as conn:
            df.to_sql('prediction', con=conn, index=False, if_exists='append')

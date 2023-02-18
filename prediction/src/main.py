import datetime
import time
import random
import pandas as pd
from model import Model
from database import DataBase


if __name__ == '__main__':
    print('Application started')
    db = DataBase()
    # db.get_last_rows()

    model = Model()
    df = pd.read_csv('../data/raw_data2.csv', parse_dates=['moment'])
    column_name = ['SM_Exgauster\[0:6]', 'SM_Exgauster\[0:7]', 'SM_Exgauster\[0:9]', 'SM_Exgauster\[0:10]']
    df = df[column_name]
    df = df.rename({'SM_Exgauster\[0:6]': 'bearing7_hor',
                    'SM_Exgauster\[0:7]': 'bearing7_vert',
                    'SM_Exgauster\[0:9]': 'bearing8_hor',
                    'SM_Exgauster\[0:10]': 'bearing8_vert'}, axis=1)
    date_predict = model.predict(df[0: 100])

    df = pd.DataFrame({'code_id': 2, 'time': datetime.datetime.now(), 'prediction_data': date_predict}, index=[0])
    db.add_new_rows(df)

    # while True:
    # time.sleep(5)
    # add_new_table()
    # get_last_rows()
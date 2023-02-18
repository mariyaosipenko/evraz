import datetime
import pandas as pd
from model import Model
from database import DataBase
import time


if __name__ == '__main__':
    print('Application started')
    db = DataBase(docker=0)
    db.get_last_rows()

    # df = db.get_last_rows()  # будут данные по всем 6 экзгаустерам
    # for exgauster_id, df_exgauster in df.groupby('algoa'):
    #     df_exgauster.podtype_id == 4  # горизонтальная
    #     df_exgauster.podtype_id == 5  # вертикальная
    #     df_exgauster.melt(id_vars=['time'], var_name=)


    date_calc = datetime.datetime.now()

    model = Model()
    # df = pd.read_csv('../data/raw_data2.csv', parse_dates=['moment'])
    # column_name = ['SM_Exgauster\[0:6]', 'SM_Exgauster\[0:7]', 'SM_Exgauster\[0:9]', 'SM_Exgauster\[0:10]']
    # df = df[column_name]
    # df = df.rename({'SM_Exgauster\[0:6]': 'bearing7_hor',
    #                 'SM_Exgauster\[0:7]': 'bearing7_vert',
    #                 'SM_Exgauster\[0:9]': 'bearing8_hor',
    #                 'SM_Exgauster\[0:10]': 'bearing8_vert'}, axis=1)
    # date_predict = model.predict(df[0: 100])

    df = pd.DataFrame({'code_id': 2, 'time': date_calc, 'prediction_data': date_calc}, index=[0])
    db.add_new_rows(df)

    while True:
      time.sleep(20)
      print(10)
      # get_last_rows()
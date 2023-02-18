import datetime
import pandas as pd
from model import Model
from database import DataBase
import time
from utils import renaming

if __name__ == '__main__':
    print('Application started')
    db = DataBase(docker=1)
    models = [Model()] * 6
    df = pd.DataFrame(columns=['code_id', 'algotype', 'algoa',
                       'algob', 'value', 'time', 'id',
                       'code_id', 'name', 'typename_id',
                       'podtype_id', 'signal_id', 'analog',
                       'activity'])

    while True:
        date_calc = datetime.datetime.now()
        df_input = db.get_last_rows()  # будут данные по всем 6 экзгаустерам

        if len(df_input) < 40:
            df = pd.concat([df, df_input])
            continue
        else:
            df = df_input

        df['bearing_type'] = df.apply(renaming, axis=1)
        df_output = pd.DataFrame(columns=['exgauster', 'time', 'prediction_data'])

        for exgauster_id, df_exgauster in df.groupby('exgauster'):
            """
            цикл по экзгаустерам
            """
            df_exgauster.melt(id_vars=['time'], var_name='bearing_type', value_name='value')
            df_exgauster = df_exgauster.sort_values(by=['time'])

            model = models[exgauster_id]
            prediction_data = model.predict(df_exgauster)

            df_output_one = pd.DataFrame({'exgauster': exgauster_id,
                                        'time': date_calc,
                                        'prediction_data': prediction_data}, index=[0])

            df_output = pd.concat([df_output, df_output_one])

        # запись в БД
        db.add_new_rows(df_output)
        time.sleep(10 * 60)  # раз в 10 минут

    # model = Model()
    # df = pd.read_csv('../data/raw_data2.csv', parse_dates=['moment'])
    # column_name = ['SM_Exgauster\[0:6]', 'SM_Exgauster\[0:7]', 'SM_Exgauster\[0:9]', 'SM_Exgauster\[0:10]']
    # df = df[column_name]
    # df = df.rename({'SM_Exgauster\[0:6]': 'bearing7_hor',
    #                 'SM_Exgauster\[0:7]': 'bearing7_vert',
    #                 'SM_Exgauster\[0:9]': 'bearing8_hor',
    #                 'SM_Exgauster\[0:10]': 'bearing8_vert'}, axis=1)
    # date_predict = model.predict(df[0: 100])

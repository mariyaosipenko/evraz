import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet, Lasso, LinearRegression
import datetime


class Model:
    def __init__(self):
        self.count_samples = 10  # минут
        self.history_data = pd.DataFrame(columns=['bearing7_hor', 'bearing7_vert',
                                                 'bearing8_hor', 'bearing8_vert'])  # историческое значение амплитуды
        self.df_train = self.history_data

        # здесь нужно сохранять исторические данные

        self.data_start = None

        self.count_predict = 2000

    def get_linear_approx(self, x, y):

        model = LinearRegression()
        model.fit(x, y)

        return model

    def calc_break(self, coeff):
        """
        через сколько шагов прогнозируется поломка
        :param coeff:
        :return:
        """
        x = 0.4 / coeff
        x = x - len(self.df_train)
        return x

    def predict(self, df):
        # df = self.add_new_data(df)
        self.df_train = df
        model = self.get_linear_approx(np.array(df.index).reshape(-1, 1), df['bearing7_hor'].values)
        step_break = self.calc_break(np.squeeze(model.coef_))
        print(step_break)
        data_predict = datetime.datetime.now() + datetime.timedelta(minutes=step_break*10)
        print(data_predict)
        return data_predict

    def add_new_data(self, df):
        print(df, self.history_data)
        df = pd.concat(self.history_data, df)
        return df




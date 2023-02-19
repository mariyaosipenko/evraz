import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet, Lasso, LinearRegression
import datetime
from utils import get_amplitude


class Model:
    def __init__(self):
        self.count_samples = 10  # минут
        self.history_data = pd.DataFrame(columns=['bearing7_hor', 'bearing7_vert',
                                                  'bearing8_hor', 'bearing8_vert'])  # историческое значение амплитуды
        self.amplitude_data = pd.DataFrame(columns=['bearing7_hor', 'bearing7_vert',
                                                  'bearing8_hor', 'bearing8_vert'])  # историческое значение амплитуды
        self.df_train = self.history_data

        # здесь нужно сохранять исторические данные

        self.data_start = None
        self.count_predict = 2000
        self.dangerous_amplitude = {'bearing7_hor': 2.4, 'bearing7_vert': 2.4,
                                    'bearing8_hor': 2.4, 'bearing8_vert': 2.4}

    def get_linear_approx(self, x, y):

        model = LinearRegression()
        model.fit(x, y)

        return model

    def calc_break(self, coeff, name_feature, len_vector):
        """
        через сколько шагов прогнозируется поломка
        :param coeff:
        :return:
        """
        x = self.dangerous_amplitude[name_feature] / coeff
        x = x - len_vector
        return x

    def get_amplitude_df(self, df):
        result = []
        v = []
        for i in df:
            v.append(i)
            if len(v) >= 10:
                result.append(get_amplitude(v))
                v = []
        return result

    def predict(self, df):
        # if len(df) < 10:
        #     df = self.add_new_data(df)
        # df = df.apply(get_amplitude, axis=1)
        # print(df)
        self.df_train = df

        step_break = []

        for i in df.columns:
            k = self.get_amplitude_df(df[i].values)
            model = self.get_linear_approx(np.array(range(0, len(k))).reshape(-1, 1), k)
            step_break.append(self.calc_break(np.squeeze(model.coef_), name_feature=i, len_vector=len(k)))

        step_break = np.mean(step_break)

        data_predict = datetime.datetime.now() + datetime.timedelta(minutes=step_break*10)

        return data_predict

    def add_new_data(self, df):
        print(df, self.history_data)
        df = pd.concat(self.history_data, df)
        return df




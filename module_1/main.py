import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv('data/movie_bd_v5.csv')
data_desc = data.runtime.describe().reset_index()
data['profit'] = data.revenue - data.budget
data['genres'] = data.genres.apply(lambda s: s.split('|'))
data.explode('genres')
print(data)


# import pandas as pd
# import os
#
# def clean_time(t):
#     if str(t)[0:1] == '[':
#         return t[1:]
#     else:
#         return t
#
# # users = pd.read_csv('users.xls', encoding='koi8_r', delimiter='\t')
# # users.columns = ['user_id', 'email', 'geo']
#
# # sample = pd.read_csv('sample.xls')
# # sample2 = sample[sample['Age'] < 30]
# # sample2 = sample.copy()
# # sample2 = sample.City.apply(lambda s: str(s).lower())
# # print(sample2)
#
# # sample['Age_category'] = sample.Age.apply(lambda age: age_category(age))
#
# log = pd.read_csv("log.xls", header=None)
# log.columns = ['user_id', 'time', 'bet', 'win']
# log = log[log.user_id != '#error']
# print(log)
# log.time = log.time.apply(lambda t: clean_time(t))
#
# # print(log.win.nunique())
# # log_win = log[(log.win>0) & (log.bet>0)]
# # win_bet = len(log_win)
# # new_log = log[~log.user_id.str.match('#error', na=False)]
# # print(sample)
# # print(log)
# # print(win_bet)
# # print(log.value_counts())
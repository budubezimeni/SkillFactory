import pandas as pd
import numpy as np

us = pd.read_csv('users.xls', encoding='koi8_r', delimiter='\t')
us.columns = ['user_id', 'email', 'geo']


def clean_time(t):
    if str(t)[0:1] == '[':
        return t[1:]
    else:
        return t


def clean_user(name):
    splitted = str(name).split(' - ')
    print(splitted)
    if len(splitted) > 1:
        return splitted[1]
    else:
        return ''

def makeDayTime(t):
    if 0 <= t <= 5:
        return 'night'
    elif 6 <= t <= 11:
        return 'morning'
    elif 12 <= t <= 17:
        return 'day'
    elif 18 <= t <= 23:
        return 'evening'
    else:
        return 'none'


log = pd.read_csv('log.xls', header=None)
log.columns = ['user_id', 'time', 'bet', 'win']
# print(log[log.bet == log.bet.min()].reset_index()['bet'].count())
# log.drop_duplicates(subset=['user_id', 'time'], inplace=True)
# log.dropna(inplace=True)
log.time = log.time.apply(lambda t: clean_time(t))
log.time = pd.to_datetime(log.time)
# log['daypart'] = log.time.dt.hour.apply(lambda t: makeDayTime(t))
# log['time'] = log['time'].apply(lambda x: x.minute)
# log['hour'] = log.time.dt.hour
log['bet'].fillna(0, inplace=True)
log['win'].fillna(0, inplace=True)


def fillna_win(row):
    if not pd.isnull(row.win):
        return row
    elif pd.isnull(row.win) and pd.isnull(row.bet):
        row.win = 0
        return row
    elif (pd.isnull(row.win) and (not pd.isnull(row.bet))):
        row.win = row.bet * -1
        return row

# Применяем функцию
new_win = log.apply(lambda row: fillna_win(row), axis=1)

# Заменяем старый столбец с пропусками на новый без пропусков
log['win'] = new_win['win']
log['net'] = log['win'] - log['bet']
# wins = log[log.win > 0].reset_index()
# print(log[log.net>0].mean())
# print(log[log.net>0].median())
# print(log.shape[0])
# print(log[log.bet > 0].shape[0])
# Приведем признак user_id к одному формату в обоих датасетах
us.user_id = us.user_id.apply(lambda x: x.lower())
# Избавимся от ошибок в user_id
log = log[log.user_id != '#error']
log.user_id = log.user_id.str.split(' - ').apply(lambda x: x[1])
merged = pd.merge(log, us, on='user_id')

# print(merged.info())
# print(merged.groupby(merged['user_id']).net.sum().median())
# group = merged[merged.bet == 0].groupby(['user_id']).bet.count()
# group_not_null = merged[merged.bet > 0].groupby(['user_id']).bet.count()
# merged_null = pd.merge(group, group_not_null, on='user_id')
# merged_null = merged_null[merged_null['bet_y']>0]
# print(merged_null['bet_x'].sum()/len(merged_null))
# print(merged.groupby(merged['user_id']).bet.value_counts())

# group = merged[merged.bet == 0].groupby(['user_id']).time.min()
# group_not_null = merged[merged.bet > 0].groupby(['user_id']).time.min()
# merged_null = pd.merge(group, group_not_null, on='user_id')
# merged_null['time_diff'] = merged_null['time_y'] - merged_null['time_x']
# print(merged_null.time_diff.mean())

print(merged.groupby(merged['geo']).win.sum().reset_index().sort_values('win'))
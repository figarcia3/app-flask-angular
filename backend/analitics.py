import pandas as pd
import numpy as np


def get_time_spent_by_day(df):

    '''
    Retorna el tiempo promedio por dia de la semana
    '''
    
    df_time = df[['date_closed','date_opened']].apply(lambda x: pd.to_datetime(x))

    df_time['day'] = df_time['date_closed'].dt.day_name()

    df_time['time_spent'] = df_time['date_closed'] - df_time['date_opened']
    df_time['time_spent_sec'] = df_time['time_spent'].dt.total_seconds()

    time_by_day = df_time.groupby('day').mean()
    time_by_day = pd.to_datetime(time_by_day['time_spent_sec'], unit='s').dt.strftime('%H:%M')

    result = time_by_day.to_json()

    return result

def get_money_spent_by_day():

    '''
    Retorna el gasto promedio de una cena por dia de la semana
    '''

    df = pd.read_json('ventas.json')

    df_total = df[['date_closed']].apply(lambda x: pd.to_datetime(x))
    df_total['total'] = df['total']

    df_total['day'] = df_total['date_closed'].dt.day_name()

    money_by_day = df_total.groupby('day')['total'].mean().astype(int)

    result = money_by_day.to_json()

    return result


def get_total_dinners_by_day():

    '''
    Retorna el el total de comensales por dia de la semana
    '''

    df = pd.read_json('ventas.json')
    
    df_total = df[['date_closed']].apply(lambda x: pd.to_datetime(x))
    df_total['diners'] = df['diners']

    df_total['day'] = df_total['date_closed'].dt.day_name()

    money_by_day = df_total.groupby('day')['diners'].sum()

    result = money_by_day.to_json()

    return result


def get_effective_work_by_waiter():

    '''
    Tiempo de trabajo efectivo por mesero
    '''

    df = pd.read_json('ventas.json')

    df_time = df[['date_closed','date_opened']].apply(lambda x: pd.to_datetime(x))

    df_time['waiter'] = df['waiter']

    df_time['time_spent'] = df_time['date_closed'] - df_time['date_opened']
    df_time['time_spent_sec'] = df_time['time_spent'].dt.total_seconds()

    time_by_waiter = df_time.groupby('waiter').sum()
    time_by_waiter = pd.to_datetime(time_by_waiter['time_spent_sec'], unit='s').dt.strftime('%H:%M')

    result = time_by_waiter.to_json()

    return result

def get_effective_work_by_cashier():

    '''
    Tiempo de trabajo efectivo por mesero
    '''

    df = pd.read_json('ventas.json')

    df_time = df[['date_closed','date_opened']].apply(lambda x: pd.to_datetime(x))

    df_time['cashier'] = df['cashier']

    df_time['time_spent'] = df_time['date_closed'] - df_time['date_opened']
    df_time['time_spent_sec'] = df_time['time_spent'].dt.total_seconds()

    time_by_waiter = df_time.groupby('cashier').sum()
    time_by_waiter = pd.to_datetime(time_by_waiter['time_spent_sec'], unit='s').dt.strftime('%H:%M')

    result = time_by_waiter.to_json()

    return result
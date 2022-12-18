from datetime import timedelta,date
import holidays
import pandas as pd

# Calendar Dataframe

def calendar(year,country='ES',subdiv=None):
    """
    returns a dataframe with three columns:
    dates: with format [YYYY-MM-DD], ascending
    weekend: with value 1 if it's Saturday or Sunday, otherwise it returns 0.
    holidays: with value 1 if it's public holidays, otherwise it returns 0.
    """
    calendar=pd.DataFrame()

    def daterange(year):
        calendar = pd.DataFrame()
        calendar['Dates']=pd.date_range(f'{year}-01-01', f'{year}-12-31', freq='D')
        return calendar

    calendario = daterange(year)

    def weekends(calendar):
        calendar['weekday']= calendar['Dates'].apply(lambda x: x.weekday())
        weekend = {0:0,1:0,2:0,3:0,4:0,5:1,6:1}
        calendar['Weekend'] = calendar['weekday'].map(weekend)
        calendar.drop(columns='weekday',inplace=True)
        return calendar

    calendario = weekends(calendario)

    def public_holidays(calendar):
        es_cl_holidays = holidays.country_holidays(country,subdiv)
        calendar['Holidays']=calendar['Dates'].apply(lambda x: x in es_cl_holidays).map(int)
        return calendar
    calendario = public_holidays(calendario)

    def times(calendario):
        times=['Morning','Evening','Night']
        for i in times:
            calendario[i] = pd.Series(0)
        return calendario
    calendario = times(calendario)
    calendario['Month'] = calendario['Dates'].apply(lambda x: x.strftime('%b'))
    calendario['Week Number'] = calendario['Dates'].dt.isocalendar().week
    return calendario

def accounting(workers_df,calendar_df):
    workers=list(workers_df['name'])
    for i in workers:
        calendar_df[f'{i} T.C.']=0
        calendar_df[f'{i} W.C.']=0
        calendar_df[f'{i} M.C.']=0
    return calendar_df

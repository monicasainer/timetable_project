from datetime import timedelta,date
import holidays
import pandas as pd


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
        calendar['dates']=pd.date_range(f'{year}-01-01', f'{year}-12-31', freq='D')
        return calendar

    calendario = daterange(year)

    def weekends(calendar):
        calendar['weekday']= calendar['dates'].apply(lambda x: x.weekday())
        weekend = {0:0,1:0,2:0,3:0,4:0,5:1,6:1}
        calendar['weekend'] = calendar['weekday'].map(weekend)
        calendar.drop(columns='weekday',inplace=True)
        return calendar

    calendario = weekends(calendario)

    def public_holidays(calendar):
        es_cl_holidays = holidays.country_holidays(country,subdiv)
        calendar['holidays']=calendar['dates'].apply(lambda x: x in es_cl_holidays).map(int)
        return calendar
    calendario = public_holidays(calendario)
    return calendario

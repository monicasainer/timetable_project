from datetime import timedelta,date
import holidays
import pandas as pd

# Calendar Dataframe

def calendar(year,country='ES',subdiv=None):
    """
    Returns a dictionary. Each month is a key and the values are Dataframes with
    the following columns:
    ['Dates', 'Weekend', 'Holidays', 'Morning_1', 'Morning_2', 'Morning_3',
       'Evening_1', 'Evening_2', 'Night_1', 'Night_2', 'Month', 'Week Number']
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
        times=['Evening','Night']
        for i in range(1,4):  #3 people working during Morning
            calendario[f'Morning_{i}']=pd.Series(0)
        for t in times:
            for n in range(1,3): #2 people working during Evening and Night.
                calendario[f'{t}_{n}'] = pd.Series(0)
        return calendario
    calendario = times(calendario)
    calendario['Month'] = calendario['Dates'].apply(lambda x: x.strftime('%b'))
    calendario['Week Number'] = calendario['Dates'].dt.isocalendar().week
    month = calendario['Month'].unique()
    calendarios={}
    for i in month:
        calendarios[i]= calendario[calendario['Month']==i]
    calendarios['All']= calendario   # It will be needed to assign nights.
    return calendarios

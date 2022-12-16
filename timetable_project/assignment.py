
import random

def holiday_assignment(workers_df,calendar_df):
    def split(a, n):
        k, m = divmod(len(a), n)
        return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
    worker_holidays = list(workers_df[workers_df['holiday']==1]['name'])*(len(workers_df[workers_df['holiday']==1]['name'])-1)
    public_holidays=list(calendar_df[calendar_df['Holidays']==1].index)
    random.shuffle(public_holidays)
    split_index = list(split(public_holidays,len(list(workers_df[workers_df['holiday']==1]['name']))))
    for i in range(len(split_index)):
        indexes = split_index[i]
        names_selected = random.sample(worker_holidays,2)
        while names_selected[0]==names_selected[1]:
            names_selected = random.sample(worker_holidays,2)
        for x in indexes:
            calendar_df['Morning'].iloc[x]=names_selected[0]
            calendar_df['Evening'].iloc[x]=names_selected[1]
        worker_holidays.remove(names_selected[0])
        worker_holidays.remove(names_selected[1])
    workers=list(workers_df[workers_df['holiday']==1]['name'])
    for x in workers:
        count = 0
        for i in range(len(calendar_df.index)):
            if (calendar_df['Morning'].iloc[i] == x or calendar_df['Evening'].iloc[i]== x or calendar_df['Night'].iloc[i] == x):
                count += 1
                calendar_df[f'{x} T.C.'][i] = count
    return calendar_df


import random

def nights_assignment(workers_df,calendar_df):
    def assignment():
        worker_nights=workers_df[workers_df['schedule']==2]['name']
        total_hours={}
        total_days = 0
        for x in worker_nights:
            percentage = float(workers_df[workers_df['name']==x]['percentage'])
            initial_days=round(len(calendar_df['Night'])/len(worker_nights))
            total_hours[x]=round(initial_days*percentage)
            total_days +=total_hours[x]
        diff_days=len(calendar_df['Night'])-total_days
        while (diff_days >= len(worker_nights)) & (total_days >= len(calendar_df['Night'])) :
            for i in worker_nights:
                percentage = float(data[data['name']==i]['percentage'])
                initial_days=round(diff_days/len(worker_nights))
                total_hours[i]+=round(initial_days*percentage)
                total_days += round(initial_days*percentage)
            diff_days=len(calendar_df['Night'])-total_days
        quotient,remainder = divmod(diff_days,len(worker_nights))
        for t in worker_nights:
            total_hours[t]+=quotient
            total_days += quotient
        names = random.sample(list(worker_nights),remainder)
        for p in names:
            total_hours[p]+=1
        return total_hours

    def setting_nights():
        total_hours =assignment()
        worker_nights=workers_df[workers_df['schedule']==2]['name']
        indexes = list(range(len(calendar_df['Night'])))
        random.shuffle(indexes)

        for i in worker_nights:
            index = indexes[:total_hours[i]]
            indexes = indexes[total_hours[i]:]
            for x in index:
                calendar_df['Night'].iloc[x]= i
        return calendar_df
    calendar_df = setting_nights()
    return calendar_df










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

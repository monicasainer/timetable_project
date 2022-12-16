from datetime import timedelta,date
import holidays
import pandas as pd

def number_workers():
    worker= input("how many workers do you have? >>")
    try:
        worker = int(worker)
        return worker
    except ValueError:
        print("That's not a number!")

# Employees Dataframe

def df_workers(number_of_workers):

    def name_workers():
        name = input('How is your worker called >>')
        if name.strip().isdigit():
            print("That's not a name!")
        else:
            name=name.capitalize()
            return name

    def age_workers():
        age= input("How old is your worker? >>")
        try:
            age = int(age)
            return age
        except ValueError:
            print("That's not a number!")

    def experience_workers():
        experience= input("How many years of experience this person has? >>")
        try:
            experience = int(experience)
            return experience
        except ValueError:
            print("That's not a number!")

    def salary_workers():
        salary = input("What's the annual salary of your worker? (In €) >>")
        try:
            salary = float(salary)
            return salary
        except ValueError:
            print("That's not a number!")

    def times_workers():
        timer =[1,2,3,4,5,6]
        time = input("When does your worker works? >>\n"
                "1 for Morning and Evening\n"
                "2 for Night\n"
                "3 for Everything\n")
        try:
            time = int(time)
            if time in timer:
                return time
            else: print('Select a correct value')
        except ValueError:
            print("That's not a number!")

    def gender_workers():
        genders ={1:'Female',2:'Male',3:'Non-binary'}
        gender = input("What's the gender of your worker? >>\n"
                    "1 for Female\n"
                    "2 for Male\n"
                    "3 for Non-binary\n")
        try:
            gender = int(gender)
            if gender in genders:
                return genders[gender]
            else: print('Select a correct value')
        except ValueError:
            print("That's not a number!")

    def weekend_workers():
        weekends ={1:'No',2:'Yes'}
        weekend = input("Does your worker work during weekends? >>\n"
                    "1 for No\n"
                    "2 for Yes\n")
        try:
            weekend = int(weekend)
            if weekend in weekends:
                return weekend-1
            else: print('Select a correct value')
        except ValueError:
            print("That's not a number!")

    def holiday_workers():
        holidays ={1:'No',2:'Yes'}
        holiday = input("Does your worker work during public holidays? >>\n"
                    "1 for No\n"
                    "2 for Yes\n")
        try:
            holiday = int(holiday)
            if holiday in holidays:
                return holiday - 1
            else: print('Select a correct value')
        except ValueError:
            print("That's not a number!")
    def percentage_work():
        percentage = input("What's is the percentage your employee works? >>\n"
                    "Add it in decimals, for example:\n"
                    "20% = 0.2\n"
                    "65% = 0.65\n"
                    "100% = 1.0\n")
        try:
            percentages = float(percentage)
            return percentages
        except ValueError:
            print("That's not a valid number!")

    def data_workers(number_of_workers):
        data={}
        for i in range(number_of_workers):
            name = name_workers()
            age = age_workers()
            experience = experience_workers()
            salary = salary_workers()
            schedule = times_workers()
            gender = gender_workers()
            weekend = weekend_workers()
            holiday = holiday_workers()
            percentage = percentage_work()
            data[i] = {'name': name,'age': age,'experience':experience,'salary':salary,'schedule':schedule,'gender':gender,'weekend':weekend,'holiday':holiday,'percentage':percentage}
        return data

    df = data_workers(number_of_workers)
    df = pd.DataFrame.from_dict(df,orient='index')
    return df

# Automatic Hospital timetable 


## 😲 **What**

This data product is aimed to return a personnalized annual timeframe and an analysis of the time distribution based on workers profile.

> ➡️Input: 
> - Calendar: Year, country and region (optional).
> - HR information: The following data of employees ➡️ `name`	,`age` ,`experience` , `salary` , `schedule` , `gender` , `weekend` , `month of holidays` , `work percentage` , and `vacation`.

> ⬅️Output:
> - Calendar: Timetable where one row will correspond one day. Three columns will have assigned the employees who work during the morning of that day, two columns will contain the name of employees who work during the evening, and other two columns will gather the night workers names.


## ⁇ **Why**

For many years, the HR (human resource) coordinator has been in charge of distributing the timetable equally among different workers. The existence of many constraints such as the work percentage (full-time, part-time, etc) or the availability of each employee (morning, evening, night), hinders this task, and automating the process is now deemed necessary.


## 🤓 **How**

> Input: 
> - Calendar: Year, country and region (optional).
> - HR information: There are two options:
>   - Option 1: The user will provide a .csv file containing the following data of employees: `name`	,`age` ,`experience` , `salary` , `schedule` , `gender` , `weekend` , `month of holidays` , `work percentage` , and `vacation`.
>   - Option 2: The user will introduce the data manually. The first question they will need to reply is how many employees the company has. Once this value is selected, questions to query the points of information of option 1, will be repeated as many times as workers.
>
> - Constraints:
>   - Full-time employees have one specific month (30 days) of holidays per year.
>   - Night employees work 5 days one week, and 2 day next week, except in their vacation month.
>   - Night workers do not differenciate between public holidays, weekends and weekdays.








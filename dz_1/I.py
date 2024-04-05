file1 = open("input.txt", "r")
data=[]
lines = file1.readlines()
for line in lines:
    data.append(line.strip())
file1.close()
n = int(data[0])
year = int(data[1])
day = data[-1]
def vis(x):
    if x%400==0:
        return True
    elif x%100==0:
        return False
    elif x%4==0:
        return True
    else:
        return False
days = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}
number_day = days.get(day)
slovar={
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0
}
def gl_1(x):
    months = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    day, month_name = x.split()
    day = int(day)
    day_of_year = day
    for m, days_in_month in months.items():
        if m == month_name:
            break
        day_of_year += days_in_month
    return day_of_year
def gl_2(x):
    months = {
        "January": 31,
        "February": 29,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    day, month_name = x.split()
    day = int(day)
    day_of_year = day
    for m, days_in_month in months.items():
        if m == month_name:
            break
        day_of_year += days_in_month
    return day_of_year
if vis(year)==False:
    slovar[number_day] = -1
    for i in range (2,len(data)-1):
        if (gl_1(data[i])%7+number_day-1)%7 != 0:
            slovar[(gl_1(data[i])%7+number_day-1)%7]+=1
        else:
            slovar[7]+=1
else:
    slovar[number_day] = -1
    slovar[number_day+1] = -1
    for i in range (2,len(data)-1):
        if (gl_2(data[i]) % 7 + number_day - 1) % 7 != 0:
            slovar[(gl_2(data[i]) % 7 + number_day - 1) % 7] += 1
        else:
            slovar[7] += 1
max_d = max(slovar.values())
min_d = min(slovar.values())
flag_1=0
flag_2=0
mas=[0]*2
for i in range (1,8):
    if slovar[i]==max_d and flag_1==0:
        flag_1=1
        for key, value in days.items():
            if value == i:
                mas[1]=key
                break
    elif slovar[i]==min_d and flag_2==0:
        flag_2=1
        for key2, value2 in days.items():
            if value2 == i:
                mas[0]=key2
                break
print(mas[0],mas[1])
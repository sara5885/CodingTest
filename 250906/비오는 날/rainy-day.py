n = int(input())
date = []
day = []
weather = []

class today():
    def __init__(self,date,day,weather):
        self.date=date 
        self.day=day 
        self.weather=weather
n_day=[]
for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)
    if w=='Rain':
        n_day.append(today(d,dy,w))

earliest_rain_today=n_day[0]
for i in range(1,len(n_day)):
    ori_year=earliest_rain_today.date[0:4]
    ori_month=earliest_rain_today.date[4:6]
    ori_date=earliest_rain_today.date[6:8]
    new_year=n_day[i].date[0:4]
    new_month=n_day[i].date[4:6]
    new_date=n_day[i].date[6:8]
    
    # change min 
    if ori_year>new_year or (ori_year==new_year and ori_month>new_month) or(ori_year==new_year and ori_month==new_month and ori_date>new_date):
        earliest_rain_today=n_day[i]


print(f"{earliest_rain_today.date} {earliest_rain_today.day} {earliest_rain_today.weather}")

# Please write your code here.
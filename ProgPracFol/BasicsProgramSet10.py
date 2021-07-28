"""
Date-Time Programs
"""
import datetime as dt
import pytz, time , calendar

"""
1) Program to get Current Time
"""
#Method 1
x = dt.datetime.now()
print(x.strftime("%H:%M:%S"))
#Time taken:  0.0010151863098144531

#Method 2
india = pytz.timezone('Asia/Kolkata')
dt_india = dt.datetime.now(india)
print("India Time: ",dt_india.strftime("%H:%M:%S"))
#Time taken:  0.12403178215026855

#Method 3
timeIndia = dt.datetime.now().time()
print("Current Time: ",timeIndia)
#Time taken:  0.0009982585906982422

"""
2) Get Current Date and Time using Python
"""
#Method 1
x = dt.datetime.now()
print(x)
#Time taken:  0.0010151863098144531

#Method 2
x = dt.datetime.now()
print("Year: ",x.year)
print("Month: ",x.month)
print("Date: ",x.day)
print("Hour: ",x.hour)
print("Minute: ",x.minute)
print("Second: ",x.second)
print("Microsecond: ",x.microsecond)
#Time taken:  0.0019898414611816406

"""
3) Program to Find yesterday’s, today’s and tomorrow’s date
"""
presentday = dt.datetime.now()
yesterday = presentday - dt.timedelta(1)
future = presentday + dt.timedelta(1)
print("Present Day: ",presentday.strftime("%D-%M-%Y"))
print("Yesterday Day: ",yesterday.strftime("%D-%M-%Y"))
print("Future Day: ",future.strftime("%D-%M-%Y"))
#Time taken:  0.003993511199951172

"""
4) Program to convert time from 12 hour to 24 hour format
"""
def convert24(x):
    if x[-2:] == "AM" and x[:2] == "12":
        return "00" + x[2:-2]
    elif x[-2:] == "AM":
        return x[:-2]
    elif x[-2:] == "PM" and x[:2] == "12":
        return x[:-2]
    else:
        return str(int(x[:2]) + 12) + x[2:8]
print(convert24("07:05:45 PM"))
#Time taken:  0.003992557525634766

"""
5) Program to find difference between current time and given time
"""
def difference(h1,m1,h2,m2):
    t1 = h1*60 + m1
    t2 = h2*60 + m2
    if(t1 == t2):
        return "Both are same times"
    else:
        diff = t2 - t1
    h = (int(diff/60))%24
    m = diff%60
    return h," : ",m
print(difference(7, 20, 9, 45))
print(difference(15, 23, 18, 54))
print(difference(16, 20, 16, 20))
#Time taken:  0.0040013790130615234

"""
6) How to convert timestamp string to datetime object
"""
def daycount(year):
    days = [ "Monday", "Tuesday", "Wednesday", 
           "Thursday",  "Friday", "Saturday",
           "Sunday" ]
    L = [52 for i in range(7)]
    pos = -1
    day = dt.datetime(year,month = 1,day =1).strftime("%A")
    for i in range(7):
        if day == days[i]:
            pos = i
    if calendar.isleap(year):
        L[pos] += 1
        L[(pos+1)%7] += 1
    else:
        L[pos] += 1
    for i in range(7):
        print(days[i],L[i])
year = 2021
daycount(year)
#Time taken:  0.011987924575805664
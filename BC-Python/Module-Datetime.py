from datetime import datetime,timedelta,date,time


print(datetime.now())
print(date.today())
print(type(datetime.today()))


today = datetime.now()
future_date = today + timedelta(days=7)

print('Today:',today)
print('After 1 week:',future_date)

print('-'*50)

#converting datetime object into string
print(today.strftime("%Y-%m-%d"))
print(type(today.strftime("%Y-%m-%d")))
print(datetime.today().strftime("%d-%m-%Y"))  #another method


#converting string to datetime object.
parsed_date = datetime.strptime("2023-09-26", "%Y-%m-%d")
print(parsed_date)


print('-'*50)
day_of_week = today.strftime("%A")
print(day_of_week)

#Comparision:
today = datetime.now()
future_date = today + timedelta(days=7)
print(today>future_date)
import datetime


today = datetime.datetime.now()
print(today)


# Date in string (yera-month-day)
today_str = datetime.datetime.now().strftime('%Y-%m-%d')
print(today_str)

# Substraction e.g how to get yesterday's day
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
yesterday = yesterday.strftime('%Y-%m-%d')
print(yesterday)
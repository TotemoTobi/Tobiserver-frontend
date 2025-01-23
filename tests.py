import datetime
from datetime import date
from datetime import timedelta
yesterday =  date.today() - timedelta(days = 1)
print(yesterday.strftime("%m")+"/"+ yesterday.strftime("%d"))
import datetime as dt   

today = dt.datetime.now()
date = str(today).split("")[0]
delta = date.time
print(date)
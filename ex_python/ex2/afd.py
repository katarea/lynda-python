from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
today=date.today()
afd=date(today.year,4,1)
if afd<today:
    t = (today-afd).days
    print('april fools day went by', t ,'days')
    afd=afd.replace(year=today.year+1)
time_to_afd=afd-today
print("its just",time_to_afd.days,"days until afd")
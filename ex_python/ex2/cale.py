import calendar
c = calendar.TextCalendar(calendar.SUNDAY)
#st=t.formatmonth(2017, 1)
#print(st)
for i in c.itermonthdays(2018,8):
    print (i)
for name in calendar.month_name:
    print(name)
for name in calendar.day_name:
    print(name)   
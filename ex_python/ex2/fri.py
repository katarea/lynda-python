import calendar
c = calendar.TextCalendar(calendar.SUNDAY)
print("team meetings will be on:")
for m in range(1,13):
    cal=calendar.monthcalendar(2018,m)
    weekone=cal[0]
    weektwo=cal[1]
    if weekone[calendar.FRIDAY] !=0:
        meetday=weekone[calendar.FRIDAY]
    else:
        meetday=weektwo[calendar.FRIDAY] 
    print("%s%d"%(calendar.month_name,meetday))
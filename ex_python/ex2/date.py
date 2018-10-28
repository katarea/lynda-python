from datetime import date
from datetime import time
from datetime import datetime
def main():
    today=date.today()
    print("today's date is: ",today)
    print("data components:",today.day , today.month, today.year)
    print("today's weekday is:" ,today.weekday())
    days=["mon","tue","wed","thu","fri","sat","sun"]
    print("which is a :",days[today.weekday()])  

if __name__=="__main__":
 main()   
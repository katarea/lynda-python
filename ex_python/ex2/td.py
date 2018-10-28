from datetime import datetime
from datetime import timedelta
#print(timedelta(days=365, hours=5,minutes=1))
n=datetime.now()
#print("today is:"+str(n))
#print("one year from now it will be:"+str(n+timedelta(days=365)))
print("after two weeks and three days:"+str(n+timedelta(weeks=2,days=3)))
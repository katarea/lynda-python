import os
from os import path
import datetime
from datetime import time,date,timedelta
import time
def main():
   # t=time.ctime(path.getmtime("textfile.txt"))
    #print(t)
    #print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
    td=datetime.datetime.now()-datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("its been"+str(td)+"since file was modified")
    print("or"+str(td.total_seconds())+"seconds")
main()
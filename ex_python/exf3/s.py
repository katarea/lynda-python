import os
from os import path
import datetime
from datetime import time,date,timedelta
import time
def main():
   # print(os.name)
  # print("item exists:"+str(path.exists("textfile.txt")))
   #print("item is file:"+str(path.isfile("textfile.txt")))
   #print("item is direc(tory:"+str(path.isdir("textfile.txt")))
   print("item path"+str(path.realpath("textfile.txt")))
   print("itempath and name"+str(path.split(path.realpath("textfile.txt"))))
main()    
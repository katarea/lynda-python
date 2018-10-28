from datetime import datetime
def main():
    now=datetime.now()

    print(now.strftime(" current year is %Y"))
    print(now.strftime("%a,%d,%B,%y"))
    #print(now.strftime("local date and time:%c")
    print(now.strftime("24 hour time:%H,%M,%s,%p"))
main()
def main():
    f=open("textfile.txt","r")
    if f.mode=="r":
       # contents=f.read()
        #print (contents)
        fl=f.readlines()
        for x in fl:
            print(x)
    
main()    

    
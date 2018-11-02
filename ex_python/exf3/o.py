def main():
    file_my=open("textfile.txt","w")
    for i in range(10):
        file_my.write("this is ash" +i+  "\n")
    file_my.close()
main()
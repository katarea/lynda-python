import urllib
import sockets
# from urllib import request
def main():
    webUrl = urllib.urlopen("http://wwww.usgs.gov")
    print("result code:" +str(webUrl.getcode()))
    data=webUrl.read()
    print(data)
main()
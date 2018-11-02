import urllib
import json
def printResults(data):
    _theJSON=json.loads(data)
    if "title" in _theJSON["metadata"]:
     print(_theJSON["metadata"]["title"])
    count=_theJSON["metadata"]["count"]
    print(str(count)+"events recorded")
    print("events that were felt:")
    for i in _theJSON["features"]:
        feltReports=i["properties"]["felt"]
        if feltReports !=None:
            if feltReports>0:
        #if i["properties"]["mag"]>=4.0:

             print("%2.1f" %i["properties"]["mag"],i["properties"]["place"],"reported"+str(feltReports)+"times")
        
def main():
    urlData="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webUrl=urllib.urlopen(urlData)
    print("result code:"+str(webUrl.getcode()))
    if (webUrl.getcode()==200):
        data=webUrl.read()
        printResults(data)
    else:
        print("received error,cannot parse reasults")
main()        

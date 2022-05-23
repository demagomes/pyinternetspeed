import speedtest
import time
import csv
import datetime
import os
from time import gmtime, strftime


s = speedtest.Speedtest()

# s.get_servers(servers)
s.get_best_server()
dmbps = s.download() / 1000000
umbps = s.upload() / 1000000

results = s.results.dict()
starttime = time.time()


def getfilename():
    today = datetime.date.today().strftime("%d-%m-%Y")
    return today + '_internetspeedtestresults.csv'

file =getfilename()
#print(file)

def saveresults(download,upload,ping):    
    filename = getfilename()
    fileexists = os.path.exists(filename)
  

def testspeed():
    s=speedtest.Speedtest

printResults = 'Date: ' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + '|' + 'Download Speed (mbps): ' + str(round(dmbps)) + '|' + 'Upload Speed (mbps): ' + str(round(umbps)) + '|' + 'Ping: ' + str(results["ping"])


if not os.path.exists(file):
    with open(file,"w", newline='') as speedResults:   
        write = csv.DictWriter(speedResults,fieldnames=['Time','Download Speed (mbps)','Upload Speed (mbps)','Ping'])   
        write.writeheader()  
        while True:            
            write.writerow({'Time': str(time.asctime()),'Download Speed (mbps)': str(round(dmbps)),'Upload Speed (mbps)': str(round(umbps)),'Ping': str(results["ping"])})
            print(printResults)
            time.sleep(300)
else:
    with open(file,"a", newline='') as saveresults:   
        write = csv.DictWriter(saveresults,fieldnames=['Time','Download Speed (mbps)','Upload Speed (mbps)','Ping'])   
         
        while True:            
            write.writerow({'Time': str(time.asctime()),'Download Speed (mbps)': str(round(dmbps)),'Upload Speed (mbps)': str(round(umbps)),'Ping': str(results["ping"])})
            print(printResults)
            time.sleep(300)
      



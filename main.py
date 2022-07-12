import speedtest
import time
import csv
import datetime
import os
from time import gmtime, strftime

def getfilename():
    today = datetime.date.today().strftime("%d-%m-%Y")
    return today + '_internetspeedtestresults.csv'

def saveresultstocsv(download,upload,ping):
    filename = getfilename()
    fileexists = os.path.exists(filename)
    fieldnames = ['timestamp','download', 'upload','ping']

    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['timestamp','download', 'upload','ping']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not fileexists:
            writer.writeheader()
        
        writer.writerow({'timestamp':strftime("%Y-%m-%d %H:%M:%S", gmtime()),'download': download, 'upload': upload, 'ping': ping})   
 
def speedTest():
    print('Testing Internet Speeed...', end='\r')
    s = speedtest.Speedtest()
    servers = []
    print('Getting Best Server.......', end='\r')
    s.get_servers(servers)
    print('Running Speed Test........', end='\r')
    s.get_best_server()
    dmbps = s.download() / 1000000
    umbps = s.upload() / 1000000
    print('Working  on results.......', end='\r')
    results_dict = s.results.dict()   
    printResults = 'Date: ' + time.asctime() + '|' + 'Download Speed (mbps): ' + str(round(dmbps)) + '|' + 'Upload Speed (mbps): ' + str(round(umbps)) + '|' + 'Ping: ' + str(results_dict["ping"])
    print(printResults)
    saveresultstocsv(str(round(dmbps)),str(round(umbps)),str(results_dict["ping"])) 
    print('Waiting for next run......', end='\r') 
   
def printheader():
    print('Python Internet Speed Test')
    print('https://github.com/demagomes/pyinternetspeed')

# Main Execution block
printheader()
while True:
    speedTest()
    time.sleep(300)





      





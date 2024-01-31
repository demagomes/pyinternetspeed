import speedtest
import time
import csv
import datetime
import os
from time import gmtime, strftime

class TerminalColours:
    HEADER = '\033[95m'
    INFO = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'

def getfilename():
    today = datetime.date.today().strftime("%d-%m-%Y")
    return today + '_internetspeedtestresults.csv'

def saveresultstocsv(filename,download,upload,ping):
    fileexists = os.path.exists(filename)
    fieldnames = ['timestamp','download', 'upload','ping']

    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['timestamp','download', 'upload','ping']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not fileexists:
            writer.writeheader()
        
        writer.writerow({'timestamp':strftime("%Y-%m-%d %H:%M:%S", gmtime()),'download': download, 'upload': upload, 'ping': ping})   
 
def speed_test():
    print('Testing Internet Speeed...', end='\r')

    try:
        s = speedtest.Speedtest()
    except speedtest.ConfigRetrievalError as err:
        cprint('Date: ' + time.asctime() + '|' + 'Error while running speed test: {0}'.format(err),'ERROR')
        return

    servers = []
    print('Getting Best Server.......', end='\r')
    s.get_servers(servers)
    print('Running Speed Test........', end='\r')

    try:
        s.get_best_server()
    except speedtest.SpeedtestBestServerFailure as err:
        cprint('Date: ' + time.asctime() + '|' + 'Error while getting best server: {0}'.format(err),'ERROR')
        return


    dmbps = s.download() / 1000000
    umbps = s.upload() / 1000000
    print('Working  on results.......', end='\r')
    results_dict = s.results.dict()   
    printResults = 'Date: ' + time.asctime() + '|' + 'Download Speed (mbps): ' + str(round(dmbps)) + '|' + 'Upload Speed (mbps): ' + str(round(umbps)) + '|' + 'Ping: ' + str(results_dict["ping"])
    print(printResults)
    saveresultstocsv(getfilename(),str(round(dmbps)),str(round(umbps)),str(results_dict["ping"])) 
   
def printheader():
    cprint('Python Internet Speed Test','HEADER')
    cprint('https://github.com/demagomes/pyinternetspeed','INFO')
    cprint('Please press Control+C to end the program','INFO')

def cprint(message, type):
    if type == 'HEADER':
        print(f"{TerminalColours.HEADER}{message}{TerminalColours.ENDC}")
    elif type == 'INFO':
        print(f"{TerminalColours.INFO}{message}{TerminalColours.ENDC}")
    elif type == 'WARNING':
        print(f"{TerminalColours.WARNING}{message}{TerminalColours.ENDC}")
    elif type == 'ERROR':
        print(f"{TerminalColours.ERROR}{message}{TerminalColours.ENDC}")

      





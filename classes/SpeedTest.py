import speedtest
import time
import csv
import datetime
import os
from classes.TerminalColours import TerminalColours as tc
from time import gmtime, strftime

class SpeedTest:

    def cprint(self, message, type):
        if type == 'HEADER':
            print(f"{tc.HEADER}{message}{tc.ENDC}")
        elif type == 'INFO':
            print(f"{tc.INFO}{message}{tc.ENDC}")
        elif type == 'WARNING':
            print(f"{tc.WARNING}{message}{tc.ENDC}")
        elif type == 'ERROR':
            print(f"{tc.ERROR}{message}{tc.ENDC}")
        elif type == 'OKBLUE':
            print(f"{tc.OKBLUE}{message}{tc.ENDC}")
        elif type == 'OKCYAN':
            print(f"{tc.OKCYAN}{message}{tc.ENDC}")
        elif type == 'WHITE':
            print(f"{tc.WHITE}{message}{tc.ENDC}")

    def getfilename(self):
        today = datetime.date.today().strftime("%d-%m-%Y")
        return today + '_internetspeedtestresults.csv'

    def saveresultstocsv(self,filename,download,upload,ping):
        fileexists = os.path.exists(filename)
        fieldnames = ['timestamp','download', 'upload','ping']

        with open(filename, 'a', newline='') as csvfile:
            fieldnames = ['timestamp','download', 'upload','ping']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not fileexists:
                writer.writeheader()
            
            writer.writerow({'timestamp':strftime("%Y-%m-%d %H:%M:%S", gmtime()),'download': download, 'upload': upload, 'ping': ping})   
    
    def speed_test(self):
        print('Testing Internet Speeed...', end='\r')

        try:
            s = speedtest.Speedtest()
        except speedtest.ConfigRetrievalError as err:
            self.cprint('Date: ' + time.asctime() + '|' + 'Error while running speed test: {0}'.format(err),'ERROR')
            return

        servers = []
        print('Getting Best Server.......', end='\r')
        s.get_servers(servers)
        print('Running Speed Test........', end='\r')

        try:
            s.get_best_server()
        except speedtest.SpeedtestBestServerFailure as err:
            self.cprint('Date: ' + time.asctime() + '|' + 'Error while getting best server: {0}'.format(err),'ERROR')
            return


        dmbps = s.download() / 1000000
        umbps = s.upload() / 1000000
        print('Working  on results.......', end='\r')
        results_dict = s.results.dict()   
        printResults = 'Date: ' + time.asctime() + '|' + 'Download Speed (mbps): ' + str(round(dmbps)) + '|' + 'Upload Speed (mbps): ' + str(round(umbps)) + '|' + 'Ping: ' + str(results_dict["ping"])
        self.cprint(printResults,'INFO')
        self.saveresultstocsv(self.getfilename(),str(round(dmbps)),str(round(umbps)),str(results_dict["ping"])) 
    
    def printheader(self):
        self.cprint('Python Internet Speed Test','HEADER')
        self.cprint('https://github.com/demagomes/pyinternetspeed','WHITE')
        self.cprint('Please press Control+C to end the program','WHITE')



        





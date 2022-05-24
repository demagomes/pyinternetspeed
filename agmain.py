# This is the speedtest library that we need to install
# refer to readme for info on how to do so
import csv
import datetime
import os
import speedtest
import time

# The inspect module provides several useful functions to help get information about live objects such as
# modules, classes, methods, functions, tracebacks, frame objects, and code objects. 
# For example, it can help you examine the contents of a class, retrieve the source code of a method, 
# extract and format the argument list for a function, 
# or get all the information you need to display a detailed traceback.
# import inspect

# save results to csv
# {Download Speed, Upload Speed, Ping}
def getfilename():
    today = datetime.date.today().strftime("%d-%m-%Y")
    return today + '_internetspeedtestresults.csv'

def saveresultstocsv(download,upload,ping):
    filename = getfilename()
    fileexists = os.path.exists(filename)

    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['timestamp','download', 'upload','ping']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not fileexists:
            writer.writeheader()
        
        writer.writerow({'timestamp':time.asctime(),'download': download, 'upload': upload, 'ping': ping})

# Instantiate an object from class speedtest
def testspeed():
    s = speedtest.Speedtest()
    # print('Running speed tests....')

    servers = []
    s.get_servers(servers)
    s.get_best_server()
    dmbps = s.download() / 1000000
    umbps = s.upload() / 1000000
    # s.results.share # This doesnt seem to work
    # print(s.results.share)
    results_dict = s.results.dict()
    # print(results_dict)
    # uncomment this for checking available info in the dic
    # for key, value in results_dict.items():
    #     print(key, ' : ', value)

    # print a little message on screen
    print(time.asctime() + '|' + 'Download Speed (mbps): ' + str(round(dmbps)) + '|' + 'Upload Speed (mbps): ' + str(round(umbps)) + '|' + 'Ping: ' + str(results_dict["ping"]))

    # record in csv
    saveresultstocsv(str(round(dmbps)),str(round(umbps)),str(results_dict["ping"]))

starttime = time.time()
while True:
    testspeed()
    time.sleep(900.0 - ((time.time() - starttime) % 900.0))

# print all methods available in the class speedtest
# for method in inspect.getmembers(s, predicate=inspect.ismethod):
#     print(method[0])


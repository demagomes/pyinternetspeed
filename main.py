import speedtest
import time
import csv

s = speedtest.Speedtest()

# s.get_servers(servers)
s.get_best_server()
dmbps = s.download() / 1000000
umbps = s.upload() / 1000000

results = s.results.dict()
starttime = time.time()


with open('speed_results.csv',"w", newline='') as speedList:
    write = csv.DictWriter(speedList,fieldnames=['Time','Download Speed (mbps)','Upload Speed (mbps)','Ping'])   
    write.writeheader()   
    while True:             
        write.writerow({'Time': str(time.asctime()),'Download Speed (mbps)': str(round(dmbps)),'Upload Speed (mbps)': str(round(umbps)),'Ping': str(results["ping"])})
        time.sleep(30) 
        break 

    #print('Time: ' + str(time.asctime())  + '|' + 'Download Speed (mbps): ' + str(round(dmbps)) + '|' + 'Upload Speed (mbps): ' + str(round(umbps)) + '|' + 'Ping: ' + str(results["ping"]))
    
#print('Download Speed (mbps): ' + str(round(dmbps)) + '|' + 'Upload Speed (mbps): ' + str(round(umbps)) + '|' + 'Ping: ' + str(results["ping"]))



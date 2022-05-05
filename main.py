import speedtest

s = speedtest.Speedtest()

# s.get_servers(servers)
s.get_best_server()
dmbps = s.download() / 1000000
umbps = s.upload() / 1000000

results = s.results.dict()

print('Download Speed (mbps): ' + str(round(dmbps)) + '|' + 'Upload Speed (mbps): ' + str(round(umbps)) + '|' + 'Ping: ' + str(results["ping"]))
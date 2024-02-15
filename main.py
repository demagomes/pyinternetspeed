import time
from classes.SpeedTest import SpeedTest

# Main Execution block
# It prevents from running if imported.
if __name__ == '__main__':
    # instantiate speedtest class.
    sp = SpeedTest()
    sp.printheader()
    try:
        while True:
            sp.speed_test()
            print('Waiting for next run......', end='\r') 
            time.sleep(900)
    except KeyboardInterrupt:
        # remove the C^ output from console.
        print('', end='\r')
        sp.cprint('Thanks for using Python Internet Speed Test','HEADER')
        pass



      





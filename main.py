import time
import classes.SpeedTest as sp

# Main Execution block
# It also prevents from running if imported.
if __name__ == "__main__":
    sp.printheader()
    try:
        while True:
            sp.speed_test()
            print('Waiting for next run......', end='\r') 
            time.sleep(900)
    except KeyboardInterrupt:
        # remove the C^ output from console.
        print('', end='\r')
        print('Thanks for using Python Internet Speed Test')
        pass



      





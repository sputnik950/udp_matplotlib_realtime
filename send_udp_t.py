import socket
import time 
from contextlib import closing
 
import datetime
import numpy as np
import matplotlib.dates as mdates

def main():
    host = '127.0.0.1'
    port = 4000
    count = 0
    dat   = 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    n_cnt =400

    time_range = n_cnt# 24 * 30
    dates = [datetime.datetime(2017,1,1) + datetime.timedelta(hours=i) for i in range(time_range)]
    vals = [np.sin(2 * np.pi * i / 240) for i in range(time_range)]

    with closing(sock):
     
        while True:
            #message = "fgwrp"
            message = 'AT1 ' +str(dates[count]) + ' ' +str(vals[count])
            print(message)
            sock.sendto(message, (host, port))
            count += 1
            dat *=-0.98
            if count > n_cnt -1:
                count = 0
                dat = 1
            time.sleep(0.1)
    return

if __name__ == '__main__':
    main()

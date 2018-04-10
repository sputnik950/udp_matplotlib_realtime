from __future__ import print_function
from contextlib import closing
import math
#from pylab import *
import numpy as np
import datetime
import threading
import sys
from udp_read import *
from graph import *
import signal
import time
from threading import Timer,Thread,Event

plot_flg = 0

class InfiniteTimer():
    """A Timer class that does not stop, unless you want it to."""

    def __init__(self, seconds, target):
        self._should_continue = False
        self.is_running = False
        self.seconds = seconds
        self.target = target
        self.thread = None

    def _handle_target(self):
        self.is_running = True
        self.target()
        self.is_running = False
        self._start_timer()

    def _start_timer(self):
        if self._should_continue: # Code could have been running when cancel was called.
            self.thread = Timer(self.seconds, self._handle_target)
            self.thread.start()

    def start(self):
        if not self._should_continue and not self.is_running:
            self._should_continue = True
            self._start_timer()
        else:
            print("Timer already started or running, please wait if you're restarting.")

    def cancel(self):
        if self.thread is not None:
            self._should_continue = False # Just in case thread is running and cancel fails.
            self.thread.cancel()
        else:
            print("Timer never started or failed to initialize.")


def tick():
    global plot_flg
#    print('ipsem lorem')
    plot_flg = 1

def task(arg1, arg2):
  global  plot_flg
  print ( plot_flg)
  plot_flg = 1
    

def main():
  global plot_flg
  args = sys.argv
  lcnt = 0
  cnt = 0
  cnt_old = 0
 # udp = Udp_read(args[1])
  g = Graph (args[2])
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind(('', 4000))
  s.setblocking(0)
  data=''
  address=''

  t = InfiniteTimer(0.5, tick)
  t.start()
  while True:

   # print ( plot_flg)
    try:
        data,address = s.recvfrom(1024)
    except socket.error:
        pass
    else:
       # print( "", data)
        g.input_data( data )
        cnt +=1
   #
   
    if plot_flg==1:
      
      print("C ", lcnt, cnt-cnt_old, g.return_n_sum_data())
      cnt_old = cnt
      plot_flg = 0
      lcnt +=1
      g.exec_plot()

      
    #cnt +=1
    #if(cnt%20==19):

      #p.set()
      #p.plot(d.t, d.y)
      #return
    
if __name__ == '__main__':
  main()

  

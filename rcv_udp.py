from __future__ import print_function
import socket
from contextlib import closing
import math
#from pylab import *
import numpy as np
import threading
import matplotlib.pyplot as plt

  
class Data2d():
  def __init__(self, index_in):
    self.index = index_in
    self.n=0
    self.x=list()
    self.y=list()
  def add_data_2d(self, xin, yin):
    self.x.append(xin)
    self.y.append(yin)
    self.n+=1
  def min_x(self):
    return min(self.x)
  def max_x(self):
    return max(self.x)
  def min_y(self):
    return min(self.y)
  def max_y(self):
    return max(self.y)
  def new_x(self):
    return self.x[len(self.x)-1]
  def new_y(self):
    return self.y[len(self.y)-1]
  
def cal_tics(min, max, div):

#  dif = max-min
#  tics = (int(dif/div)+1)*div
#  tmin = (int(min/tics)-1)*tics
#  tmax = (int(max/tics)+1)*tics
  tmin = div*(math.floor( min/div))
  tmax = div*(math.ceil(  max/div))
  tics = math.floor( (tmax-tmin)/10)
  print (min, max, div, tics, tmin, tmax, tics)
  return np.arange( tmin, tmax, tics)
  
  
def main():
  port = 4000
  bufsize = 4096
  d = Data2d(0)
  plt.ion()
  cnt = 0
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  #nlx = [0,2,4,6,7,8] 
  #nly = [2,4,7,9,4,2]
  #nlx = np.arange(0, 10, 0.01) 
  #nly = np.sin(nlx)
  with closing(sock):
    sock.bind(("", port))
    while True:
      buf = sock.recv(bufsize)
      if(buf.find('AT1')!=-1):
        bufs = buf.split()
        d.add_data_2d(float(bufs[1]), float(bufs[2]))
        #lx.append(bufs[1])
        #ly.append(bufs[2])
        cnt +=1
        #print ("%lf %G\n" % (d.new_x(), d.new_y()) )
        #print (d.new_x(), d.new_y() )
        #print (bufs[0],bufs[1],bufs[2])
        
        if(cnt%20==19):
#
#          print( d.min_x(), d.max_x())
          xl = cal_tics( int(d.min_x()), int(d.max_x()), 10)
         # plt.xticks(np.arange( d.min_x(), d.max_x(), 5))
        #  plt.xlim(0, 400)
#          plt.xlim( d.min_x(),d.max_x() )
         # plt.ylim( d.min_y(),d.max_y() )
          #plt.ylim([min(d.y), max(d.y)])
          #plt.xlim([0,400])
        
          plt.plot(d.x, d.y)
          plt.xticks(xl, xl)
          plt.draw()
          plt.pause(0.1)
          #return
  return

if __name__ == '__main__':
  main()

  

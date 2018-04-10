from figure_setting import *
from data_container import *
from plotif import *
import re

import pandas as pd

def is_float_expression(s):

  if re.match("Nan", s):
    return False
  
  if re.match("Inf", s):
    return False
  
  try:
    val = float(s)
    return True
  except ValueError:
    return False

      
class Graph():
  def __init__(self, fn_setting):
    self.n_sum_data = 0
    self.set = Figure_setting( fn_setting )
    self.p = Plotif()
    self.d =[]
    for i in range (self.set.n_total_data):
      self.d.append(Data2d(0))
    self.p.set(self.set.n_fig, self.set.n_total_data, self.set.real0time1, self.set.idx_fig, )
    self.p.init_twinx(self.set.idx_fig, self.set.n_fig, self.set.n_total_data)
#  def set_labels(self):
#    p.set_labels

#  def set_twinx(self):
#    p.set_twinx( self.idx_fig )

    
  def return_n_sum_data(self ):
    return self.n_sum_data
  
  def input_data(self,  in_str ):
    self.n_sum_data = 0
    
    tmp_str=  str(in_str)
    tmpbufs = tmp_str.split()
    for i in range (self.set.n_total_data):

      if  len( tmpbufs ) <= self.set.xcol[i] :
        continue
      if  len( tmpbufs ) <= self.set.ycol[i] :
        continue
      
      if(self.set.real0time1==0): 

        if self.set.tag[i] in tmp_str :
          if  is_float_expression(tmpbufs[self.set.xcol[i]]) and is_float_expression(tmpbufs[self.set.ycol[i]]):
        
            #self.d[self.set.idx_fig[i]].x.append()
            #self.d[self.set.idx_fig[i]].y.append()
            self.d[i].x.append()
            self.d[i].y.append()
            
      if(self.set.real0time1==1): 
        if self.set.tag[i] in tmp_str :        
          if is_float_expression(tmpbufs[self.set.ycol[i]]):
            try:
              tdatetime = datetime.datetime.strptime(tmpbufs[self.set.xcol[i]], '%H:%M:%S')
            except ValueError:
              print ("TIME FMT wrong skipped", tmpbufs[self.set.xcol[i]])
              return
            
            #self.d[self.set.idx_fig[i]].t.append(tdatetime )
            #self.d[self.set.idx_fig[i]].y.append(tmpbufs[self.set.ycol[i]])
            self.d[i].t.append(tdatetime )
            self.d[i].y.append(tmpbufs[self.set.ycol[i]])
            self.n_sum_data += len (self.d[i].t)
          #else:
            #print ("l")
            #print (tmpbufs[self.set.ycol[i]])
            #print ("N_SUM_DATA ",  n_sum_data)

  def exec_plot(self):
#    self.p.set_twinx( self.set.n_total_data )
    for i in range (self.set.n_total_data):
      if(self.set.real0time1==0): 
        #self.p.plot_datain(self.set.idx_fig[i],self.d[self.set.idx_fig[i]].x, self.d[self.set.idx_fig[i]].y)
        self.p.plot_datain(i,self.d[i].x, self.d[i].y)

      if(self.set.real0time1==1): 
        #self.p.plot_datain(self.set.idx_fig[i],self.d[self.set.idx_fig[i]].t, self.d[self.set.idx_fig[i]].y)
        self.p.plot_datain(i,self.d[i].t, self.d[i].y)

        
    self.p.grid_set(self.set.n_total_data )
    self.p.plot_exe()
    return 0

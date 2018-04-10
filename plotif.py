import datetime
import threading
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

  
class Plotif():
    

    def __init__(self):
        self.axl=[]
        self.twinx_l=[]
        plt.ion()
      
    def init_twinx(self, fig_list, n_fig, n_total_data):

        c_twinx_l=[]
        
        for i in range( n_fig ):  
            c_twinx_l.append(0)
            
        for i in range( n_total_data ):  
            if c_twinx_l[ fig_list[i] ]==0 :
                    self.twinx_l.append(0)
                    c_twinx_l[fig_list[i]] =1
            else:
                    self.twinx_l.append(fig_list[i])
        
    def set_twinx(self, n_total_data):
                        
        for i in range( n_total_data ):

            if self.twinx_l[i] != 0:
                self.axl[i] = self.axl[ self.twinx_l[i] ].twinx()
        

            

            
#    def arrange_ax_x(self, n_figure,  ):

        
    def set(self, n_figure, n_total_data, real0time1, fig_list ):
#        self.fig, axl = plt.subplots(ncols=2, figsize=(10,4))
# plt.subplots(n_figure, 1)
        for i in range (n_total_data):
            #            print ("AX==", i, n_figure)
            if i==0 :
                self.axl.append(plt.subplot(n_figure, 1, fig_list[i]+1) )
            else:
                self.axl.append(plt.subplot(n_figure, 1, fig_list[i]+1, sharex=self.axl[0]))

        
        if(real0time1):
            xfmt = mdates.DateFormatter("%H:%M:%S")
            xloc = mdates.DayLocator()
            for i in range(n_figure):
                self.axl[i].xaxis.set_major_locator(xloc)
                self.axl[i].xaxis.set_major_formatter(xfmt)
       
 #   def set_labels(self,idx, t, y):
        
    def plot_datain(self,idx, t, y):

        self.axl[idx].plot(t, y)

    def set_xlim(self, ax_idx, min, max):
        self.axl[ax_idx].set_xlim( min, max )
        
        
    def set_ylim(self, ax_idx, min, max):
        self.axl[ax_idx].set_ylim( min, max )
        
        
    def grid_set(self, n):
        for i in range(n):
           self.axl[i].grid(which='major',axis='both', color='black',linestyle='--')
    
                
    def plot_exe(self):
        plt.draw()
        plt.pause(0.01)
        #plt.cla()

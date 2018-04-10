N_MAX_DATA_IN_SINGLE_LINE = 16
import sys



class Figure_setting():
  def __init__(self, fn):
    self.new_data_x = [0]*N_MAX_DATA_IN_SINGLE_LINE 
    self.new_data_y = [0]*N_MAX_DATA_IN_SINGLE_LINE 
    
    self.n_total_data =0
    self.tmpbufs = []
    self.tag     = []
    self.idx_fig = []
    self.x1yi  = []
    self.xcol  = []
    self.ycol  = []
    self.han  = []
    self.plt_with =[]
    self.file_setting = open(fn, 'r') 
  
    self.n_fig      = int( self.read_file() )
    self.real0time1 = int( self.read_file() )
    
    if( (self.real0time1 > 1)  and  ( self.real0time1 <0 )):
      sys.exit()
    while True:
        
      tmp = str(self.file_setting.readline()) 
      
      if(tmp.find('EOF')!=-1):
          break
      self.tmpbufs = tmp.split()
      self.idx_fig.append( int(self.tmpbufs[0]))
      self.tag.append(         self.tmpbufs[1])
      self.x1yi.append(   int( self.tmpbufs[2]))
      self.xcol.append(   int( self.tmpbufs[3]))
      self.ycol.append(   int( self.tmpbufs[4]))
      self.han.append(         self.tmpbufs[5])
      self.plt_with.append(    self.tmpbufs[6])
   
      #print(self.idx_fig[self.n_total_data ],self.x1yi[self.n_total_data ],self.xcol[self.n_total_data ],self.ycol[self.n_total_data ],self.han[self.n_total_data ] )
    
      self.n_total_data += 1

      
  def read_file(self):
    while True:
      tmp = self.file_setting.readline()
      if(tmp.find('#')!=-1):
        
        print("_")
      else:
        return tmp
 
  def return_x (self,  idx ) :
    return new_data_x[j]

  def return_y (self,  idx ) :
    return new_data_x[j]
  

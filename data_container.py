
class Data2d():
  def __init__(self, index_in):
    self.index = index_in
    self.n=0
    self.t=list()
    self.x=list()
    self.y=list()
    
  def add_data_2d_t(self, xin, yin):
    self.t.append(xin)
    self.y.append(yin)
    self.n+=1

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
  
  
def set_data( buf ):
  bufs = buf.split()
  tdatetime = datetime.datetime.strptime(bufs[2], '%H:%M:%S')
  add_data_2d_t(tdatetime , float(bufs[3]))


  

# udp_matplotlib_realtime


Data input on udp packet as ascii.

run as follows
python main.py PORT_UDP   CONFIGFILE

#Configfile
3  # number of axis

1  # Xaxis is 0: real, 1: time format

0 AT1 1 2 3 TAz l    # no_axis  TAG Yaxis Column_x Column_y  DataLabel plottype

1 AT2 1 2 4 time p

1 AT2 1 2 3 MAG l

2 CPF 1 2 3 dAz l

2 CPF 1 2 4 sAz l

***Not all the settting valid now. just a plan and design.




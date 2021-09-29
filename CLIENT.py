from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import socket
#import serial as sr
import time

#THIS WILL BE THE CLIENT
data = np.array([])
cond = False
#PLOT DATA
def plot_data():
    global cond, data
    if(cond==True):
        #a = message received from server
        #a.decode()
        if(len(data) < 100):
            data = 0
            #data = np.append(data,float(a[0:4]))
        else:
            data[0:99]=data[1:100]
            #data[99] - float(a[0:4])    
        lines.set_xdata(np.arange(0,len(data)))
        lines.set_ydata(data)

        canvas.draw()
    root.after(1,plot_data)    

#MAIN GUI CODE
root = tk.Tk()
root.title('Real Time Plot')
root.configure(background = 'light blue')
root.geometry("700x500")


#Create plot object on GUI
fig = Figure();
ax = fig.add_subplot(111)

ax.set_title('Serial Data');
ax.set_xlabel('time')
ax.set_ylabel('temp')
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
ax.set_xlim(300,0)
ax.set_ylim(10,50)
lines = ax.plot([],[])[0]

canvas = FigureCanvasTkAgg(fig,master=root)
canvas.get_tk_widget().place(x = 10, y =10, width = 600, height = 400)
canvas.draw()
root.after(1,plot_data)
root.mainloop()

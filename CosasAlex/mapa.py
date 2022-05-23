#!/usr/bin/env python
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.image as mpimg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from tkFileDialog import askopenfilename
from pylab import *
import tkMessageBox as mb
import pyodbc
import sys
import ttk

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

def connect_db():
    global c
    conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s' % filename)
    c = conn.cursor()

def query_db():
    global time
    global freq
    global pri
    global pw
    freq=[]
    time=[]
    pri = []
    pw = []

c.execute("SELECT utc_usec_time_stamp, freq_mhz, pri, pw FROM SampleData")
rows = c.fetchall()

for row in rows:
    time.append(row[0])
    freq.append(row[1])
    pri.append(row[2])
    pw.append(row[3])
    progressbar.step(0.0008)
    root.update_idletasks()

def plot(): 
    global sb1
    global sb2
    global sb3
    global canvas

    f = Figure()
    f.clf()
    f.subplots_adjust(bottom=0.05,top=0.98,left=0.08,right=0.98,hspace=0.1)
    sb1 = f.add_subplot(3,1,1)
    sb1.scatter(time,freq)
    setp(sb1.get_xticklabels(), visible=False)
    sb1.set_ylabel("FREQ (MHz)")

    sb2 = f.add_subplot(3,1,2, sharex=sb1)  
    sb2.scatter(time,pri)   
    setp(sb2.get_xticklabels(), visible=False)
    sb2.set_ylabel("PRI (usec)")

    sb3 = f.add_subplot(3,1,3, sharex=sb1)  
    sb3.scatter(time,pw)    
    setp(sb3.get_xticklabels(), visible=False)
    sb3.set_xlabel("TIME")
    sb3.set_ylabel("PW (usec)")

    canvas = FigureCanvasTkAgg(f, master=root)

    logo.pack_forget()

    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.RIGHT, fill=Tk.BOTH, expand=1)

    toolbar = NavigationToolbar2TkAgg( canvas, root )
    toolbar.update()
    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def test():
    global pri

    p = Tk.Toplevel(root)
    f = Tk.Frame(p)
    f.pack(side="top")
    f.grid_rowconfigure(1, weight=1)
    f.grid_columnconfigure(4, weight=1)
    lbl = Tk.Label(f, text="label")
    lbl.grid(row=1, column=1)
    e = Tk.Entry(f)
    e.grid(row=1, column=2)
    b = Tk.Button(f, text="Button")
    b.grid(row=1, column=3)
    lbl2 = Tk.Label(f, text=" ")
    lbl2.grid(row=1, column=4, padx=100)

    fig = Figure()
    sb1 = fig.add_subplot(1,1,1)
    sb1.hist(pri)

    canvas = FigureCanvasTkAgg(fig, master=p)

    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.RIGHT, fill=Tk.BOTH, expand=1)

    toolbar = NavigationToolbar2TkAgg( canvas, p )
    toolbar.update()
    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def __init__(): 
    global root
    global rmi
    global rma
    global prmi
    global prma
    global pwmi
    global pwma
    global pdf
    global progressbar
    global tf
    global logo

    root = Tk.Tk()
    root.wm_title("Airborne Tactical Analysis System (ATLAS)")
    root.wm_state('zoomed')

    menubar = Tk.Menu(root)
    File = Tk.Menu(menubar, tearoff=0)
    File.add_command(label="Open", command=open)
    File.add_separator()
    File.add_command(label="Exit", command=_quit)
    menubar.add_cascade(label="File", menu=File)
    Options = Tk.Menu(menubar, tearoff=0)
    Options.add_command(label="-Coming Soon-")
    menubar.add_cascade(label="Options", menu=Options)
    PlotData = Tk.Menu(menubar, tearoff=0)
    PlotData.add_command(label="FREQ v PW")
    PlotData.add_command(label="FREQ v PRI")
    PlotData.add_command(label="PRI v PW")
    PlotData.add_command(label="FREQ HISTOGRAM")
    PlotData.add_command(label="PRI HISTOGRAM", command=test)
    PlotData.add_command(label="PW HISTOGRAM")
    menubar.add_cascade(label="Plot Data", menu=PlotData)
    Geo = Tk.Menu(menubar, tearoff=0)
    Geo.add_command(label="Generate Map")
    menubar.add_cascade(label="Geo", menu=Geo)
    root.config(menu=menubar)

    pdf = Tk.Frame(borderwidth=1, relief="sunken")
    pdf.pack(side="left", fill="y")
    pdf.grid_rowconfigure(7, weight=1)
    pdf.grid_columnconfigure(1, weight=1)

    tf = Tk.Frame(borderwidth=1, relief="sunken")
    tf.pack(side="bottom", fill="x")
    progl = Tk.Label(text=" Processing: ")
    progl.pack(in_=tf, side="left", ipady=10)
    progressbar = ttk.Progressbar(orient='horizontal', length=200, mode='determinate')
    progressbar.pack(in_=tf, side="left")
    fl = Tk.Label(text="Current File:")
    fl.pack(in_=tf, side="left", ipadx=10)

    b1 = Tk.Button(pdf, text="Submit", command=filter_builder)
    b1.grid(in_=pdf, row=2, columnspan=3, pady=10)

    buf = Tk.Label(text="   ")
    mil = Tk.Label(text="MIN")
    mal = Tk.Label(text="MAX")
    rfl = Tk.Label(text="RF:")
    pwl = Tk.Label(text="PW:")
    prl = Tk.Label(text="PRI:")
    prmi = Tk.Entry()
    prma = Tk.Entry()
    pwmi = Tk.Entry()
    pwma = Tk.Entry()
    rmi = Tk.Entry()
    rma = Tk.Entry()
    buf.grid(in_=pdf, column=3,row=3)
    mil.grid(in_=pdf, column=1,row=3, pady=4)
    mal.grid(in_=pdf, column=2,row=3)
    rfl.grid(in_=pdf, column=0,row=4)
    rmi.grid(in_=pdf, column=1,row=4)
    rma.grid(in_=pdf, column=2,row=4)
    prl.grid(in_=pdf, column=0,row=5)
    prmi.grid(in_=pdf, column=1,row=5)
    prma.grid(in_=pdf, column=2,row=5)
    pwl.grid(in_=pdf, column=0,row=6)
    pwmi.grid(in_=pdf, column=1,row=6)
    pwma.grid(in_=pdf, column=2,row=6)

    photo = Tk.PhotoImage(file="image.gif")

    logo = Tk.Label(image=photo)
    logo.image = photo
    logo.pack(side="top", fill="both", pady=100)

    root.mainloop()

__init__()
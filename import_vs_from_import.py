'''
This just launches a basic Window / GUI. Decided to save this piece because it
illustrates a subtle but important difference between import and from import.
'''

import tkinter
#from tkinter import *

# The Window class is not standard - create a window
class Window(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master

# initialize tkinter
root = tkinter.Tk()
app = Window(root)

# set window title
root.wm_title("Tkinter window")

# show window
root.mainloop()

'''
This code below will work but, compared with code above demonstrates import-ant (eh? eh?)
differences between 'import tkinter' and 'from tkinter import *'

The first one (import) creates a reference to that module, which is why the objects then
need to be qualified with tkinter dot whatever.

The second one (from ... import *) creates a reference to all of that module's public 
objects within the local namespace of the current module - big difference.
'''

'''
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("Tkinter window")

# show window
root.mainloop()
'''

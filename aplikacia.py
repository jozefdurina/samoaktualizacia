import sys
import tkinter as tk


#config aplikacie
__version = "0.1"

def getVersion():
    return __version

#if -v argument is passed in, just print version information and exit
if ("-v" in sys.argv):
    print("Version: ", getVersion())
    sys.exit()


#na ukazku len prazdne okno
window = tk.Tk()

window.mainloop()


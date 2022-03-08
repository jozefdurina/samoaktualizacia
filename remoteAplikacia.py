import sys

#config aplikacie
__version = "0.2"

def getVersion():
    return __version

#if -v argument is passed in, just print version information and exit
if ("-v" in sys.argv):
    print("Version: ", getVersion())
    sys.exit()

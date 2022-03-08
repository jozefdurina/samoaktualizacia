import subprocess

def getLocalVersion():
    result = subprocess.run( ["python", "aplikacia.py", "-v"], stdout=subprocess.PIPE, text=True )
    version = result.stdout.partition(":")[2].strip(" \n")
    return version

def getRemoteVersion():
    result = subprocess.run( ["python", "remoteAplikacia.py", "-v"], stdout=subprocess.PIPE, text=True )
    version = result.stdout.partition(":")[2].strip(" \n")
    return version


localVersion = getLocalVersion()
remoteVersion = getRemoteVersion()

if localVersion!=remoteVersion:
    #zmaz stary lokalny zalohovy subor, ak existuje
    #premenuj lokalny subor pre jeho uchovanie pre pripad neuspesneho kopirovania zo vzdialeneho 
    #prekopiruj vzdialeny subor na lokalne umiestnenie
    #vsetko treba mat osetrene cez try ... except
    pass

#teraz spusti lokalnu aplikaciu z lokalneho umiestnenia a 
#vo verzii, ktora sa posledna podarila ziskat z dohodnuteho vzdialeneho uloziska
#toto spusti aplikaciu a funkcia hned vrati. Necaka sa teda na ukoncenie vyvolaneho procesu
subprocess.Popen( ["python", "aplikacia.py"] )  

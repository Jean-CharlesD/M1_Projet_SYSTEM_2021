import fnmatch
import os


for file in os.listdir('.'):
    if fnmatch.fnmatch(file,'*.sam'):
       FileSamT = print (file," est un fichier sam TADAAAM")
       info = os.stat (file)
       print (info)
       print (' Taille de  ', file, ' :  '  , info.st_size)
      # SamT = open (FileSamT, 'r')
      # with open (FileSamT) as SamT :
#           hea =  
#    else:
#       print (file," n'est pas un fichier sam ")
        


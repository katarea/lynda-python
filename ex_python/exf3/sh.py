import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("textfile.txt"):
        #src=path.realpath("textfile.txt")
        #dst =src+ ".bak"
        #shutil.copy(src,dst)
        #os.rename=("textfile.txt","newfile.txt")
        #root_dir,_tail = path.split(src)
        #shutil.make_archive("archive","zip",root_dir)
        with ZipFile("testzip.zip","w") as newzip:
         newzip.write=("textfile.txt")
         newzip.write=("textfile.txt.bak")
main()    

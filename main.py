import sys
from gencode.gen import *

if __name__ == "__main__" :

    p = 'C:\\Users\\ISS-Vendor\\Desktop\\gen\\'

    gen = Gen(p,sys.argv)
    gen.write()
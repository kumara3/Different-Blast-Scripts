'''
Created on Jul 16, 2014
This script records the top blast hits from blast .csv file
@author: kumara3
'''
from Bio import SeqIO
import argparse
from Bio.Blast import NCBIStandalone

def top_hits():
    parser = argparse.ArgumentParser(description="Get the top blast hits")
    parser.add_argument('-i', metavar='in-file', type=argparse.FileType('rt'))
    parser.add_argument('-o', metavar='out-file', type=argparse.FileType('wt'))

    try:
        results = parser.parse_args()
        
        print 'Input file:', results.i
        print 'Output file:', results.o
        blast_qresult = SeqIO.read(results.i, "tab")
        print (blast_qresult)
        
    except IOError, msg:
        parser.error(str(msg))  
    
    
top_hits()

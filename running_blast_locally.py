'''
Created on Jul 2, 2014

@author: kumara3
This script converts large fasta file into smaller chunks as requested by users. 
'''

import os

from Bio import SeqIO

def batch_iterator(iterator, batch_size):
    entry = True
    while entry:
        batch = []
        while len(batch) < batch_size:
            try:
                entry = iterator.next()
            except StopIteration:
                entry = None
            if entry is None:
                break
            batch.append(entry)
        if batch:
            yield batch

list_of_filename = []
record_iter = SeqIO.parse(open("/home/kumara3/workspace/Read_simulator/input_data/test_data/test_chunks_contigs.fasta"),"fasta")
for i, batch in enumerate(batch_iterator(record_iter, 10)) :
    filename = "group_%i.fasta" % (i+1)
    handle = open(filename, "w")
    count = SeqIO.write(batch, handle, "fasta")
    handle.close()
    list_of_filename.append(filename)
    print "Wrote %i records to %s" % (count, filename)

    



    
       
       
        
            
                
                
            
        
            
    
    

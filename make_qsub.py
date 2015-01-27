'''
Created on Jul 7, 2014
This script generates small script for executing the blast query file chunks
@author: kumara3
'''

from running_blast_locally import list_of_filename
import os

def generate_qsub_script():
    for eachfile in list_of_filename:
        
        out = 'run_qsub'+"_"+eachfile+'.sh'
        if os.path.exists(out):
            os.remove(out)
        
        outfile = 'out'+eachfile+'.blast'
        cmd = "blastx -db %s -query %s -out %s -outfmt %d -evalue %f -num_threads %d" %('eggNOG',eachfile,outfile,7,1e-8,8)
        working_directory ='/home/kumara3/workspace/Read_simulator'
        handle = open(out,'w')
        handle.write("#!/bin/bash -l")
        handle.write("\n")
        handle.write("#PBS -N blastx")
        handle.write("\n")
        handle.write("##PBS -N blast_program")
        handle.write("\n")
        handle.write("#PBS -l nodes=1:ppn=8")
        handle.write("\n")
        handle.write("#PBS -l walltime=480:0:0")
        handle.write("\n")
        handle.write("#PBS -q batchmodule load blast+")
        handle.write("\n")
        handle.write(working_directory)
        handle.write("\n")
        handle.write(cmd)
generate_qsub_script()


    
    
    
    
    
        
        

        
        
        
    
    
    
    
    
    

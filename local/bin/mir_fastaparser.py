#!/usr/bin/env python3

# 	Attributes of the object "record" are the following (with reference to miRNA.dat):
#	id =	miRNA id 	(e.g. MI0009703)
#	name =	miRNA name 	(e.g. hsa-mir-553)
#	seq = nucleotides sequence of the whole miRNA

import sys, os
from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("-f", "--format", help="file format.", type=string)

args = parser.parse_args()
print(args.print_string)

#FASTA = os.readlink('/proc/self/fd/0')
	# This only works on Linux to obtain filename as a string:
	# /proc is a filsystem that give information about processes
	# /self means the current running process (the one that opens the file)
	# /fd is a directory containing symbolic links for each open file descriptor in the process
	# /0 indicates the stdin

#for record in SeqIO.parse(FASTA, "fasta"):
	#if record.id.startswith("hsa"):
		#print(record.id, record.seq, record.name )

#sys.exit()

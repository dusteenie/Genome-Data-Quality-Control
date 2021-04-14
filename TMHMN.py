# --------------------------------------------------------------------------
# MOVE TO SEPERATE FILE UPON COMPLETION:
#
#  TO DO:
#  > add documentation where you need to have python 3+ and tmhmm installed
#
#
#
# TMHMM requires FASTA format. I need to convert the sequence first.
# more info on the format:   https://en.wikipedia.org/wiki/FASTA_format
#
#
# TMHMM valid console input:
''' 
$ tmhmm -h
  usage: tmhmm [-h] -f SEQUENCE_FILE [-m MODEL_FILE] [-p]

  optional arguments:
    -h, --help            show this help message and exit
    -f SEQUENCE_FILE, --file SEQUENCE_FILE
                          path to file in fasta format with sequences
    -m MODEL_FILE, --model MODEL_FILE
                          path to the model to use
    -p, --plot            plot posterior probabilies
'''
#
# Info on making system calls: 
# https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
# https://janakiev.com/blog/python-shell-commands/
#
# Info about sequences
# https://www.nature.com/scitable/topicpage/translation-dna-to-mrna-to-protein-393/
#
# TMhMM documentation
# https://pypi.org/project/tmhmm.py/
# --------------------------------------------------------------------------



# Main method
#
# @author	Stepak
# @since 	04.06.2021
# @ params: arg[]
# Order of Accepted arguments in arg[]:
#   Number of files    Type int
#   File Name(s)	   Type: string 

def startup(arg):
	numFiles = int(arg[1])
	i = 2 # First file in chain
	length = len(arg) # length of param


# DEBUG
print("Hello")
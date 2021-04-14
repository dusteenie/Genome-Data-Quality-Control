# Name: Dusty Stepak
# Date: 02.17.2021
# Program: ORF.py
# Purpose: Finds the Open Reading Frame of a given sequence



# --------------------------------------------------------------------------
# Import Statements
# --------------------------------------------------------------------------
import sys #Allows access to variables from a Terminal call
import os



# --------------------------------------------------------------------------
# Functions and Methods
# --------------------------------------------------------------------------

# shiftSequence is a method which "shifts" the current sequence (curSeq) 
# to the current possible frame (n)
#
#	@author Dusty Stepak
#	@since  02.17.2021
#	@param	curSeq	contains the current sequence- Values are either the inital 
#					sequence, or the reverse complement. Values are of type string
#	@param	n       contains the current possible frame to shift the sequence to.
#					Values are of type int
#
def shiftSequence(curSeq, n):
	yield curSeq[:n]
	curSeq = curSeq[n:]

	while curSeq:
		yield curSeq[:3]
		curSeq = curSeq[3:]


# reverseSequence is a function which converts the sequence (curSeq) 
# to its reverse complement. 
#
#	@author Dusty Stepak
#	@since  04.14.2021
#	@param	curSeq	contains the inital sequence. Values are of type string
#	@return			Returns the reverse complement of the sequence. Return is type string.
#
def reverseSequence(curSeq):
	return curSeq[::-1]


# startStop is a method which finds the starting and ending point 
# of the the current sequence (curSeq).
#
#	@author Dusty Stepak
#	@since  04.14.2021
#	@param	curSeq	contains the current sequence- Values are either the inital 
#					sequence, or the reverse complement. Values are of type string
#	@exception		passes NoneType exceptions.
#
def startStop(curSeq):
	startPossiblities = []
	endPossibilities = []
	possibilities = []
	index = 0

	for code in curSeq:
		if len(code) == 3 and code == "ATG":
			startPossiblities.append(index)
		elif len(code) == 3 and code == "TAG" or code == "TGA" or code == "TAA":
			endPossibilities.append(index)
			
		index = index+1
		

	# this function can be modified later to trim unaccessable results.
	for startingPoint in startPossiblities:
		for endingPoint in endPossibilities:
			if startingPoint > endingPoint:
				pass
			else:
				possibilities.append(str(curSeq[startingPoint:endingPoint+1]))
				break

	del(startPossiblities)
	del(endPossibilities)

	# Removes duplicates and trims the sequences to desired length
	for seq in possibilities:
		if len(seq) >= 300 and not seq in trimmed_results:
		#if len(seq) >= 350 and len(seq) <= 425 and not seq in trimmed_results:
			trimmed_results.append(seq)

		
			

# Creates a new file in the current directory path which contains the
# trimmed results.
# file naming convention goes as shown: Seq[instance]__ORF_Result.txt
#
#	@author: stepak
#	@since:  02.24.2021 
#	@params: instance		int 	Current position within file array
#	@return  None
#		
def writeToFile(instance):
	s = "Seq" + str(instance) + "__ORF_Result.txt"
	fileNames.append(s)
	w = open(s,'w')
	for item in trimmed_results:
		line = str(item)
		w.write(line+"\n")
	w.close()



# Resets all global variables to their original values
#
#	@author: stepak
#	@since:  02.24.2021 
#	@return  None
#		
def resetGlobal():
	curSeq = "" 
	possibleFrames = {3,2,1} 
	sequence = ""
	reverse_complement = "" 
	results = []  
	trimmed_results = [] 
	peptide_sequence = [] 



# Main method
#
# 	@author	Stepak
#	@since  04.14.2021
# 	@ params: arg[]
# 		Order of Accepted arguments in arg[]:
#   	Number of files    Type int
#   	File Name(s)	   Type: string 
#
def startup(arg):
	numFiles = int(arg[1])
	i = 2 # First file in chain
	length = len(arg) # length of param

	while i < length:
		f = open(arg[i])
		sequence = f.read()
		
		# Appends all possible shifts of the starting sequence to results
		for i in possibleFrames:
			curSeq = sequence
			curSeq = list(shiftSequence(curSeq,i))
			results.append(curSeq)

		# Calculates the reverse complement of the sequence
		curSeq = sequence
		reverse_complement = reverseSequence(curSeq)

		# Appends all possoble shifts of the reverse complement to results
		for i in possibleFrames:
			curSeq = reverse_complement
			curSeq = list(shiftSequence(curSeq,i))
			results.append(curSeq)
			
		# Trims all frames within results; adds these values to trimmed_results 
		for item in results:
			startStop(item)
		
		# Prints all frames into the output file
		for seq in trimmed_results:
			#if len(seq) >= 350 and len(seq) <= 425:
			writeToFile(i)
			#else:
			#	pass

		print("Length of trimmed results:")
		print(str(len(trimmed_results)))
		#Resets global variables for next file
		resetGlobal()

		#Closes the current sequence file
		f.close()

		# Increments i to the next file
		i = i +1;


# --------------------------------------------------------------------------
# Global Variable Declaration
# --------------------------------------------------------------------------
curSeq = "" # Placeholder for the current sequence
possibleFrames = {3,2,1} # Possible ORF frames
sequence = ""	# Contains sequence
reverse_complement = "" # Contains the reverse complement of the sequence
results = []  # Contains inital "untrimmed" frames
trimmed_results = [] # Contains "trimmed" frames
peptide_sequence = [] # Contains the peptide sequence for "trimmed" frames
fileNames = [] # Contains list of created files.


# --------------------------------------------------------------------------
# Main function call
# --------------------------------------------------------------------------
startup(sys.argv)
# Calls next python program
#for file in fileNames:
#	exec(open("./TMHMN.py").read(), dict(), file)
os.system('python3 TMHMN.py 1')


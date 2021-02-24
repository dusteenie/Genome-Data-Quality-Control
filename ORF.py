# Name: Dusty Stepak
# Date: 02.17.2021
# Program: ORF.py
# Purpose: Finds the Open Reading Frame of a given sequence



# --------------------------------------------------------------------------
# Import Statements
# --------------------------------------------------------------------------
import sys #Allows access to variables from a Terminal call



# --------------------------------------------------------------------------
# Functions and Methods
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
#
#	TO - DO
#	> Remove variables after useage
#	> Run tests
#	> Begin TMHMM
#
# --------------------------------------------------------------------------



#	shiftSequence is a method which "shifts" the current sequence (curSeq) 
#	to the current possible frame (n)
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


#	reverseSequence is a function which converts the sequence (curSeq) 
#	to its reverse complement. 
#
#	@author Dusty Stepak
#	@since  02.17.2021
#	@param	curSeq	contains the inital sequence. Values are of type string
#	@return			Returns the reverse complement of the sequence. Return is type string.
#
def reverseSequence(curSeq):
	reverse_complement = ""
	for c in sequence:
		if(c == "A" or c == "a"):
			reverse_complement  = "T" + reverse_complement 
		elif(c == "T" or c == "t"):
			reverse_complement  = "A" + reverse_complement 
		elif(c == "C" or c == "c"):
			reverse_complement  = "G" + reverse_complement 
		elif(c == "G" or c == "g"):
			reverse_complement  = "C" + reverse_complement 
		else:
			print("ERROR, BAD SEQUENCE")
			break
	return reverse_complement


#	startStop is a method which finds the starting and ending point 
#	of the the current sequence (curSeq).
#
#	@author Dusty Stepak
#	@since  02.17.2021
#	@param	curSeq	contains the current sequence- Values are either the inital 
#					sequence, or the reverse complement. Values are of type string
#	@exception		passes NoneType exceptions.
#
def startStop(curSeq):
	isFrame = False
	temp1,temp2,temp3 = None, None, None

	try:
		start = curSeq.index("ATG")
		isFrame = True
	except:
		pass

	if isFrame == True:
		try:		
			temp1 = curSeq.index("TAG")
		except:
			pass
		try:		
			temp2 = curSeq.index("TGA")
		except:
			pass	
		try:
			temp3 = curSeq.index("TAA")
		except:
			pass	

		# Checks to make sure the end point is past the starting point
		if(temp1 != None and temp1 < start or temp2 != None and temp2 < start or temp3 != None and temp3 < start):
			if temp1 < start:
				temp1 = None
			elif temp2 < start:
				temp2 = None
			else:
				temp3 = None


		if temp1 != None and temp2 != None and temp3 != None:
			stop = min(temp1,temp2,temp3)	

		elif temp1 != None and temp2 != None:
			stop = min(temp1,temp2)		

		elif temp1 != None and temp3 != None:
			stop = min(temp1,temp3)		

		elif temp2 != None and temp3 != None:
			stop = min(temp2,temp3)

		elif temp1 != None:
			stop = temp1
		elif temp2 != None:
			stop = temp2
		elif temp3 != None:
			stop = temp3

		del(temp1)
		del(temp2)
		del(temp3)


		trimmed_results.append(curSeq[start:stop+1])

		
#	peptideConvert is a method which converts the accepted trimmed frames
#	into it's accociated peptide sequence.
#
#	@author Dusty Stepak
#	@since  02.17.2021
#	@data	Boolean conversions are done based on the amino acid table
#	@url	https://vlab.amrita.edu/index.php?sub=3&brch=273&sim=1432&cnt=1
#
def peptideConvert():
	seq = ""

	for item in trimmed_results:
		for code in item:
			char1 = code[0]
			char2 = code[1]
			char3 = code[2]

			if char1 == "T" or char1 == "t":
				if char2 == "T" or char2 == "t":
					if char3 == "T" or char3 == "t" or char3 == "C" or char3 == "c":
						seq += "phe"
					else:
						seq += "leu"

				elif char2 == "C" or char2 == "c":
					seq += "ser"

				elif char2 == "A" or char2 == "a":
					if char3 == "T" or char3 == "t" or char3 == "C" or char3 == "c":
						seq += "tyr"
					else:
						seq += "STOP"

				else:
					if char3 == "T" or char3 == "t" or char3 == "C" or char3 == "c":
						seq += "cys"
					elif char3 == "A" or char3 == "a":
						seq += "STOP"
					else:
						seq += "trp"

			elif char1 == "C" or char1 == "c":
				if char2 == "T" or char2 == "t":
					seq += "leu"

				elif char2 == "C" or char2 == "c":
					seq += "pro"

				elif char2 == "A" or char2 == "a":
					if char3 == "T" or char3 == "t" or char3 == "A" or char3 == "a":
						seq += "his"
					else:
						seq += "gln"
						
				else:
					seq += "arg"


			elif char1 == "A" or char1 == "a":
				if char2 == "T" or char2 == "t":
					if char3 == "T" or char3 == "t" or char3 == "C" or char3 == "c" or char3 == "A" or char3 == "a":
						seq += "ile"
					else:
						seq += "met"

				elif char2 == "C" or char2 == "c":
					seq += "thr"

				elif char2 == "A" or char2 == "a":
					if char3 == "T" or char3 == "t" or char3 == "C" or char3 == "c":
						seq += "asn"
					else:
						seq += "lys"
						
				else:
					if char3 == "T" or char3 == "t" or char3 == "C" or char3 == "c":
						seq += "ser"
					else:
						seq += "arg"

			else:
				if char2 == "T" or char2 == "t":
					seq += "val"

				elif char2 == "C" or char2 == "c":
					seq += "ala"

				elif char2 == "A" or char2 == "a":
					if char3 == "T" or char3 == "t" or char3 == "C" or char3 == "c":
						seq += "asp"
					else:
						seq += "glu"
						
				else:
					seq += "gly"

		print(seq)
		print()

		peptide_sequence.append(seq)


		

# Creates a new file in the current directory path which contains the
# trimmed results.
# file naming convention goes as shown: Seq[instance]__ORF_Result.txt
#
# @author: stepak
# @since:  02.24.2021 
# @params: instance		int 	Current position within file array
# @Return  None
#		
def writeToFile(instance):
	s = "Seq" + str(instance) + "__ORF_Result.txt"
	w = open(s,'w')
	for item in trimmed_results:
		w.write("\n"+str(item))
	w.close()



# Resets all global variables to their original values
#
# @author: stepak
# @since:  02.24.2021 
# @Return  None
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
# @author	Stepak
# @since 	02.24.2021
# @ params: arg[]
# Order of Accepted arguments in arg[]:
#   Number of files    Type int
#   File Name(s)	   Type: string 

def startup(arg):
	numFiles = int(arg[1])
	i = 2 # First file in chain
	length = len(arg) # length of param

	while i < length:
		print(arg[i])
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
			if len(seq) >= 350 and len(seq) <= 425:
				writeToFile(i)
			else:
				pass

		#Resets global variables for next file
		resetGlobal()

		#Closes the current sequence file
		f.close()

		# Increments i to the next file
		i = i +1;










'''
Implement Later if Inquired

	if arg[(last)] == 1:
		# Converts all trimmed results into their affiliated peptide sequences.
		# Values are stored within peptide_sequence
		peptideConvert()

'''


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


# --------------------------------------------------------------------------
# Main function call
# --------------------------------------------------------------------------
startup(sys.argv)
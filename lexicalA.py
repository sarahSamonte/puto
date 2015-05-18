#to get command line args
import sys
import os.path

# Globals
start_boundary = ["{", "(", "["]	
end_boundary = ["}", ")", "]"]
operator = ["+", "-", "*", "/", "=", ">", "<", ">=", "<=", "!=", "=="]
keywords = ["maikling", "mahabang", "putulin", "anyo", "alyas", "ibalik", "laging", "wala", "tuloy", "sukat", "pumunta", "puno"]
data_types = ("titik", "bilang", "salita", "tuldok")
data_types2 = ["titik", "bilang", "salita", "tuldok"]
control = ["ediKung", "kung", "iba", "gawin", "habang", "tuwing", "kaso", "palit", "walangKaso"]
built_in = ["sulat", "kuha"] 
terminator = ";"
argDelimiter = ","
escape = ["\n", "\t"]
some = ["%c", "%d", "%f"]
#
IDENTIFIER = 1001
OPERATOR = 1002
CONTROL = 1003
DATA_TYPE = 1004
BUILT_IN = 1005
START_BOUNDARY = 1006
END_BOUNDARY = 1007
LIT_BOUNDARY = 1008
KEYWORD = 1009
LINE_COMMENT = 1010
MULT_COMMENT = 1011
INT_LIT = 1012
FLOAT_LIT = 1013
CHAR_LIT = 1014
STR_LIT = 1015
BUILT_IN = 1016
TERMINATOR = 1017
ARG_DELIMITER = 1018
INVALID = 1018

def main():
	#Get filename and loop over all lines if it exists 
	inputFilename = sys.argv[1]

	if os.path.isfile(inputFilename): 
		inputFile = open(inputFilename);

		# Processes every statement int every line
		# Statement always ends with a semicolon, except for conditionals (end with {) + other exceptions
		token = -1
		for line in inputFile:			
			# Fetch lexemes separated with space and determine token  
			# for lexeme in statement array/object 
			  	# Get first char of lexeme and determine class			  	
			  	# if class of first char is letter, continue until space
			  		# determine token, switch between identifier, conditionals, other keywords, built-in fxns
			  	# if class of first char is digit, continue unitl space while checking if all are digits or with one decimal point
			  	# else if comment ignore
			  	# else
			  		#switch between one character lexemes, relational operators, relational ops			  		 
			#sys.stdout.write(line)
			line = line.replace('\t', "")
			line = line.replace('\n', "")
			lexemes = line.split(" ")
			print "SIZE: " + str(len(lexemes))
			statementEnds = False		
			
			iterator = 0
			if token == MULT_COMMENT:
				if len(line) > 0 and line[len(line) - 1] == "~":
					token = -1	
				continue								
			for lexeme in lexemes:
				if lexeme == "":
					break
				print str(iterator) + ": " + lexeme	
				token = getToken(lexeme)			 
				if token == LINE_COMMENT or token == MULT_COMMENT or token == TERMINATOR or token == "{" or token == "}":
					break
				iterator += 1

	else:
		print "ERROR: File does not exists"
	

def getToken(line):		
	if line in start_boundary:	
		print "START_BOUNDARY"	
		return START_BOUNDARY
	if line in end_boundary:	
		print "END_BOUNDARY"	
		return END_BOUNDARY						
	elif line in operator:	
		print "OPERATOR"	
		return OPERATOR
	elif line in control:	
		print "CONTROL"	
		return CONTROL
	elif line in keywords:
		print "KEYWORD"	
		return KEYWORD
	elif line in data_types2:
		print "DATA_TYPE"	
		return DATA_TYPE
	elif line.startswith(data_types):
		print "IDENTIFIER"
		return IDENTIFIER		
	elif line == "#":
		print "LINE_COMMENT"
		return LINE_COMMENT
	elif line == "~":
		print "MULT_COMMENT"
		return MULT_COMMENT	
	elif line.isdigit():
		print "INT_LIT"
		return INT_LIT
	elif isFloat(line):
		print "FLOAT_LIT"
		return FLOAT_LIT	
	elif len(line) == 3 and line[0] == "'" and line[len(line) - 1] == "'":
		print "CHAR_LIT"
		return CHAR_LIT	
	elif line.count('"') == 2 and line[0] == '"' and line[len(line) - 1] == '"':
		print "STR_LIT"
		return STR_LIT
	elif line in built_in:
		print "BUILT_IN"
		return BUILT_IN 
	elif line == terminator:
		print "TERMINATOR"
		return TERMINATOR 
	elif line == argDelimiter:
		print "ARG_DELIMITER"
		return ARG_DELIMITER 				
	else:
		print "INVALID"
		return INVALID		
#function getLexeme

#function getstatement

def isFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

main()	
'''
	This show the tokens in the puto program
	To use: python puto.py (puto file)
'''

import sys
import os.path

class Parser:
	# tokens
	start_block 		= 	"{"
	end_block 			= 	"}"
	start_args 			= 	"("
	end_args			=	")"
	statement_end		= 	";"
	arg_delimiter		= 	","	
	assignment_op		= 	"="
	mult_comment 		= 	"~"
	line_comment 		= 	"#"
	return_statement	= 	"ibalik"
	main_fxn			= 	"puno"
	data_types 			=	("titik", "bilang", "salita", "tuldok")
	null 				= 	"wala"
	str_lit 			= 	'"'
	char_li 			= 	"'"
	control				= 	["kung","ediKung", "iba", "palit"]
	switch				= 	["kaso", "walangKaso"]
	loops 				= 	["gawin", "habang", "tuwing"]
	arithmetic_op		= 	["+", "-", "*", "/", "%"]
	relational_op		=	[">", "<", ">=", "<=", "!=", "=="]
	logical_op 			=	["||", "&&"]
	built_in_fxns		=	["sulat", "kuha"]

	#string tokens
	escape_seq 			= 	["\n", "\t"]
	format_specs 		= 	["%c", "%d", "%f"]

	#token codes
	START_BLOCK 		= 	1
	END_BLOCK 			=	2
	START_ARGS 			=  	3
	END_ARGS  			=	4
	STATEMENT_END 		=	5
	ARG_DELIMITER 		=	6
	ASSIGNMENT_OP 		=	7
	MULT_COMMENT 		=	8
	LINE_COMMENT 		=	9
	RETURN 				=	10
	MAIN_FXN 			=	11
	IDENTIFIER 			=	12
	NULL  				=	13
	CONTROL 			=	14
	LOOPS 				=	15
	ARITHMETIC_OP 		=	16
	RELATIONAL_OP 		=	17
	BUILT_IN 			=	18
	ESCAPE 				=	19
	FORMAT 				=	20
	INT_LIT 			= 	21 
	FLOAT_LIT 			=	22	
	CHAR_LIT 			= 	23
	SWITCH 				= 	25
	INVALID 			= 	100
	STR_LIT 			= 	26
	LOGICAL_OP 			= 	27

	inputfile = None
	isStrLit = False

	def main(self):

		# This gets the 2nd argument for python in the command prompt
		# python puto.py sample.puto <- this file
		inputFilename = sys.argv[1]

		# This checks if the given argument is a file and if it exists
		if os.path.isfile(inputFilename): 
			inputFile = open(inputFilename);
			# This var here refers to the code of the token (the values range from those UPPERCASE vars above)
			# The initial value is -1 which means that initially, there is no token parsed yet
			# CTRL-F token = self.getToken(lexeme) to see what this var mean
			token = -1
			for line in inputFile:			
				# These deletes the tabs and newlinges in each of the lines of the file
				line = line.replace('\t', "")
				line = line.replace('\n', "")
				lexemes = line.split(" ")

				# These ignores the lines inside the multiline_comment symbol ~
				if token == self.MULT_COMMENT:
					if len(line) > 0 and line[len(line) - 1] == "~":
						token = -1	
					continue			
				# CTRL+F lexemes = line.split(" ")
				# ^ means that all the tokens should separated with spaces, (for easier parsing) 	
				for lexeme in lexemes:					
					# If it encounters whitespace, it is ignored
					if lexeme == "":
						continue
					# This is to ignore the strings inside the quotation marks. Remember that we split the lines with space as a delimiter 	
					if token == self.STR_LIT and not lexeme.endswith(self.str_lit):
						isStrLit = True
						continue	
					# This is to signal that the other quotation mark for the string is found and to continue parsing the succeeding strings	
					elif token == self.STR_LIT and lexeme.endswith(self.str_lit):
						isStrLit = False
						sys.stdout.write("STR_end ")
						token = -1
						continue						
					token = self.getToken(lexeme)			 
					# This is to ignore the succeeding strings located in the same line with the comment symbols
					if token == self.LINE_COMMENT or token == self.MULT_COMMENT or token == self.STATEMENT_END:
						break									

		else:
			print "ERROR: File does not exist"
		

	# This returns the corresponding token code (the UPPERCASE global vars above) for a lexeme	
	def getToken(self, lexeme):	
		if 		lexeme == self.start_args:	
			sys.stdout.write("Args_start  ") 
			return self.START_ARGS
		elif 	lexeme == self.end_args:
			sys.stdout.write("Args_end  ") 
			return self.END_ARGS
		elif 	lexeme == self.start_block:
			sys.stdout.write("Block_start  \n")
			return self.START_BLOCK 
		elif	lexeme == self.end_block:
			sys.stdout.write("Block_end  \n")
			return self.END_BLOCK 
		elif	lexeme == self.arg_delimiter:
			sys.stdout.write("arg_delimiter  ")
			return self.ARG_DELIMITER 	
		elif 	lexeme == self.statement_end:
			sys.stdout.write("Terminator  \n")
			return self.STATEMENT_END
		elif	lexeme == self.arg_delimiter:
			sys.stdout.write("Args_bet  ") 
			return self.ARG_DELIMITER
		elif	lexeme == self.assignment_op:
			sys.stdout.write("Assignment_op  ")
			return self.ASSIGNMENT_OP 
		elif	lexeme == self.return_statement:
			sys.stdout.write("Return_statement  \n") 
			return self.RETURN		 
		elif	lexeme == self.main_fxn:
			sys.stdout.write("Main_fxn  ")
			return self.MAIN_FXN
		elif	lexeme == self.line_comment:
			sys.stdout.write("line_comment  \n")
			return self.LINE_COMMENT 	
		elif	lexeme == self.mult_comment:
			sys.stdout.write("mult_comment\n")
			return self.MULT_COMMENT	 					
		elif	lexeme.startswith(self.data_types):
			sys.stdout.write("Var/Fxn name  ")
			return self.IDENTIFIER
		elif 	lexeme == self.null:
			sys.stdout.write("null  ") 
			return self.NULL	
		elif 	lexeme in self.logical_op:
			sys.stdout.write("logical_op  ") 
			return self.LOGICAL_OP	
		elif 	lexeme in self.control:
			sys.stdout.write("Control fxn  ") 
			return self.CONTROL
		elif 	lexeme in self.switch:
			sys.stdout.write("Switch fxn  ") 
			return self.SWITCH	
		elif 	lexeme in self.loops:
			sys.stdout.write("Loop fxn  ") 
			return self.LOOPS	
		elif	lexeme in self.arithmetic_op:
			sys.stdout.write("arithmetic_Op  ") 
			return self.ARITHMETIC_OP
		elif 	lexeme in self.relational_op:
			sys.stdout.write("Relational_op  ") 
			return self.RELATIONAL_OP
		elif	lexeme in self.built_in_fxns:
			sys.stdout.write("Built-in Fxns  ")
			return self.BUILT_IN 		
		elif lexeme.isdigit():
			sys.stdout.write("Int_Lit  ")
			return self.INT_LIT 
		elif self.isFloat(lexeme):
			sys.stdout.write("Float_Lit  ") 
			return self.FLOAT_LIT	
		elif len(lexeme) == 3 and lexeme[0] == "'" and lexeme[len(lexeme) - 1] == "'":
			sys.stdout.write("Char_Lit  ")
			return self.CHAR_LIT  	
		elif lexeme.startswith(self.str_lit):
			sys.stdout.write("STR_start  ")
			return self.STR_LIT	
		else:	
			sys.stdout.write("Invalid :" + lexeme + "\n") 
			return self.INVALID	

	def isFloat(self, s):
	    try:
	        float(s)
	        return True
	    except ValueError:
	        return False

a = Parser()
a.main()	
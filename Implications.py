# StackOverflow How can I capture 'Ctrl-D' in python interactive console?
# edureka! Introduction to Input in Python
# StackOverflow NameError: global name 'myExample2' is not defined #
# 	modules
# SysTutorials How to print a line to Stderr and Stdout in Python?
# Quora What does [import sys] mean in Python?
# Simplifying multiple "or" conditions in if statement.
# Python Main Function with Examples: Understand __main__
# tutorialspoint Python IF...ELIF...ELSE Statements
#

import sys;
STR_MESSAGE = ("This program checks if the implications "
		"implies P -> Q or Q -> P.");
STR_EXPECTED_INPUT = ("Expected inputs are if then, implies, if,"
		" only if, whenever, sufficient for, necessary for.");
EXIT_PROGRAM = "Type exit to exit program.";
STR_NO_INPUT = "There was no input.\n";
STR_INVALID = "Invalid input: %s\n";
STR_BYE = "Bye!";

P_Q = "P->Q\n";
Q_P = "Q->P\n";

STR_EXIT = "exit";
STR_IFTHEN = "if then";
STR_IMPLIES = "implies";
STR_IF = "if";
STR_ONLYIF = "only if";
STR_WHENEVER = "whenever";
STR_SUFFICIENTFOR = "sufficient for";
STR_NECESSARYFOR = "necessary for";

STR_NEWLINE = "\n";

def whichWay():
	print;
	print( STR_EXPECTED_INPUT );
	print( EXIT_PROGRAM );

	try:
		userInput = raw_input();
	except EOFError:
		print( STR_BYE );
		return;
	
	if userInput == STR_EXIT:
		print( STR_BYE );
		return;

	if len(userInput) < 1:
		print( STR_NO_INPUT )

	elif userInput.lower() == (STR_IFTHEN or STR_IMPLIES
			or STR_ONLYIF or  STR_SUFFICIENTFOR):
		print( P_Q );

	elif userInput.lower() == (STR_IF or STR_WHENEVER
				or STR_NECESSARYFOR):
		print( Q_P );

	else:
		print >> sys.stderr, STR_INVALID % userInput;

	whichWay();

	return;

def main():
	print( STR_MESSAGE );
	whichWay();

if __name__ == "__main__":
	main();

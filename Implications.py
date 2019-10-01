# 
# The Implications program implements an application that returns the correct
# direction of the arrow for the given mathematical implication.
#
# Author: Akari-T
# Version: 1.0
# Since: 2019-09-29
#
# References:
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

#Define strings used for the program
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

# Returns the mathematicla implication in arrow form.
# It takes in user input and prints the correct arrow form depending on the
# input string. If invalid, notifies users. Method is called recursively, 
# until user inputs exit to stop program or terminates program by pressing
# ctrl-D.
#
# Side Effects: None.

def whichWay():
	# Print message to the users.
	print;
	print( STR_EXPECTED_INPUT );
	print( EXIT_PROGRAM );

	# If user input is detected, store in userInput.
	# If ctrl-d is detected, print message and return.
	try:
		userInput = raw_input();
	except EOFError:
		print( STR_BYE );
		return;

	# If "exit" is detected, print message and return.
	if userInput == STR_EXIT:
		print( STR_BYE );
		return;

	# If there was no input, print message to users.
	if len(userInput) < 1:
		print( STR_NO_INPUT )

	# If sring matches one of them, print corresponding arrow form.
	elif userInput.lower() == (STR_IFTHEN or STR_IMPLIES
			or STR_ONLYIF or  STR_SUFFICIENTFOR):
		print( P_Q );

	elif userInput.lower() == (STR_IF or STR_WHENEVER
				or STR_NECESSARYFOR):
		print( Q_P );

	# Otherwise, print message to users.
	else:
		print >> sys.stderr, STR_INVALID % userInput;

	# Recursively call method to continue tacking input.
	whichWay();

	return;

# Prints the statement and delegates main manipulation to whichWay().
# The purpose is to allow users to start the program.
#
# Side Effects: None.
def main():
	print( STR_MESSAGE );
	whichWay();

if __name__ == "__main__":
	main();

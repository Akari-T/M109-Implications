/**
 * The Implications program implements an application 
 * that returns the correct direction of the arrow for 
 * the given mathematical implication.
 *
 * Author: Akari-T
 * Version: 1.0
 * Since: 2019-09-14
 * */

#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include "ImplicationsStrings.h"

/** 
 * Returns the mathematical implication in arrow form.
 * It takes in user input and prints the correct arrow form depending 
 * on the input string. If invalid, notifies users. 
 * Method is called recursively, until user inputs exit to stop program
 * or terminates program by pressing ctrl+d.
 *
 * Side Effects: None.
 * */

void whichWay(){
    
    /*Buffer to store user input.*/
    char userInput[BUFSIZ];
    /*Pointer to find the new line character in buffer.*/
    char * ptr_newline = 0;
    /*To keep track of the index of the buffer.*/
    int index = 0;

    /*Prints message to the users.*/
    printf( STR_NEWLINE );
    printf( STR_NEWLINE );
    printf( STR_EXPECTED_INPUT );
    printf( EXIT_PROGRAM );

    /*If ctrl-D is detected, print message and return.*/
    if( fgets( userInput, BUFSIZ, stdin ) == NULL )
        printf( STR_BYE );
        return;

    /*Find the newline character and replace it with a NULL character.*/
    ptr_newline = strchr( userInput, CHAR_NEWLINE );
    *ptr_newline = NULL_CHAR;

    /*Convert all characters of user input to lower case.*/
    while( userInput[index] != NULL_CHAR ){
        userInput[index] = (char)tolower(userInput[index]);
        index++;
    }

    /*If stirng equals to exit, return.*/
    if( strcmp( userInput, STR_EXIT ) == 0 )
        printf( STR_BYE );
        return;

    /*If there is no input, print message to users.*/
    if( userInput[0] == NULL_CHAR ) 
        fprintf( stderr, STR_NO_INPUT );

    /*If string matches one of them, print corresponding arrow form.*/
    else if( strcmp( userInput, STR_IFTHEN ) == 0)
        printf( P_Q );
    
    else if( strcmp( userInput, STR_IMPLIES ) == 0)
        printf( P_Q );

    else if( strcmp( userInput, STR_ONLYIF ) == 0)
        printf( P_Q );

    else if( strcmp( userInput, STR_SUFFICIENTFOR ) == 0)
        printf( P_Q );


    else if( strcmp( userInput, STR_IF ) == 0)
        printf( Q_P );

    else if( strcmp( userInput, STR_WHENEVER ) == 0)
        printf( Q_P );

    else if( strcmp( userInput, STR_NECESSARYFOR ) == 0)
        printf( Q_P );
    
    /*Otherwise, print message to users.*/
    else
        fprintf( stderr, STR_INVALID, userInput );

    /*Print a newline char after corresponding message is printed.*/
    printf( STR_NEWLINE );

    /*Recursively call method to continue taking input.*/
    whichWay();
    /*Return.*/
    return;
}

/**
 * Prints the statement and delegates main manipulation to whichWay().
 * The purpose is to allow users to start the program.
 *
 * Paramters:
 *      argc - the number of inputs by the user
 *      argv - an array of pointers pointing to the user inputs
 *
 * Side Effects: None
 * */
int main( int argc, char * argv[] ){
    /*Print initial message to users.*/
    printf( STR_MESSAGE );
    /*Delegate main program to whichWay.*/
    whichWay();
}



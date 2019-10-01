/**
 * The Implications program implements an application 
 * that returns the correct direction of the arrow for 
 * the given mathematical implication.
 *
 * @author Akari-T
 * @version 2.0
 * @since 2019-09-12
 * */


import java.lang.String;
import java.util.*;

/**
 * The class contains the method whichWay() and main(String args[]).
 * When compiled the class Implications is created.
 * Users can input one of the given strings to the program, which will return
 * the arrow form. The user can end the program by typing in exit.
 **/
class Implications{

    final static String message = "This pogram checks if the implications "+
        "implies P -> Q or Q -> P.";
    final static String expectedInput = "Expected inputs are if then, " +
        "implies, if, only if, whenever, sufficient for, necessary for.";
    final static String exitProgram = "Type exit to exit program.";
    final static String noInput = "There was no input.\n";
    final static String invalid = "Invalid input: ";
    final static String bye = "Bye!";

    final static String PQ = "P->Q";
    final static String QP = "Q->P";

    final static String exit = "exit";
    final static String ifThen = "ifthen";
    final static String implies = "implies";
    final static String if1 = "if";
    final static String onlyIf = "onlyif";
    final static String whenever = "whenever";
    final static String sufficientFor = "sufficientfor";
    final static String necessaryFor = "necessaryfor";

    /** 
     * Returns the mathematical implication in arrow form.
     * It takes in user input and prints the correct arrow form depending 
     * on the input string. If invalid, notifies users. 
     * Method is called recursively, until user inputs exit to stop program.
     *
     * Side Effects: None.
     * */

    public static void whichWay(){

        /*Prints message to the users.*/
        System.out.println();
        System.out.println( expectedInput );
        System.out.println( exitProgram );

        /*Create new scanner with stdin and read user input.*/
        Scanner userInput = new Scanner(System.in);
        if( !userInput.hasNextLine() ){
            userInput.close();
            System.out.println( bye );
            return;
        }
        
        String inputString = userInput.nextLine();

        /*If stirng equals to exit, close the scanner and return.*/
        if(inputString.equalsIgnoreCase( exit )){
            userInput.close();
            System.out.println( bye );
            return;
        }

        /*If there is no input, print message to users.*/
        if(inputString.length() < 1) 
            System.out.println( noInput );

        /*If string matches one of them, print corresponding arrow form.*/
        else if(inputString.equalsIgnoreCase(ifThen) || 
                inputString.equalsIgnoreCase(implies) || 
                inputString.equalsIgnoreCase(onlyIf) || 
                inputString.equalsIgnoreCase(sufficientFor))
            System.out.println( PQ );

        /*If string matches one of them, print corresponding arrow form.*/
        else if(inputString.equalsIgnoreCase(if1) || 
                inputString.equalsIgnoreCase(whenever)
                || inputString.equalsIgnoreCase(necessaryFor))
            System.out.println( QP );

        /*Otherwise, print message to users.*/
        else
            System.err.println( invalid + inputString);
       
        /*Recursively call method to continue taking input.*/
        whichWay();
        /*Return.*/
        return;
    }
   
    /**
     * Prints the statement and delegates main manipulation to whichWay().
     * The purpose is to allow users to start the program.
     *
     * @param args The arugment passed. Not used in this program.
     * 
     * Side Effects: None
     * */
    public static void main(String[] args){
        System.out.println( message ); 
        whichWay();
    }
}



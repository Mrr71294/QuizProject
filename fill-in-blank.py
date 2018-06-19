#README: Id like to apologize in advance if this is incredibly inefficient, I know this could
#be a lot smaller and would love to know how small you pros got it. Please be as honest as
#possible with your review. I want to be a lot better at this than I am and need to know
#how to be more efficent. Thank you in advance!:)

# initiate variables-Easy////////////////////////////////////////////////////////////////////////////
e1 = ['"First_Blank"',"len"];
e2 = ['"Second_Blank2"',"print"];
e3 = ['"Third_Blank3"',"return"];
e4 = ['"Fouth_Blank"',"join"];
easyKey = [e1,e2,e3,e4];#answer key that lets me switch between "blank" and "answer" in the questions string.

easyQuestions = "The "+e1[0]+"() function returns the number of items of an object. The "+e2[0]+"() function prints the given object to the standard output device. The "+e3[0]+" statement is used when a function is ready to return a value to its caller. The "+e4[0]+"() method returns a string concatenated with the elements of an iterable.";

easy = [easyQuestions, easyKey];#package answer key and questions together.

# initiate variables-Medium////////////////////////////////////////////////////////////////////////////
m1 = ['"First_Blank"',"replace"];
m2 = ['"Second_Blank2"',"append"];
m3 = ['"Third_Blank3"',"pop"];
m4 = ['"Fouth_Blank"',"sort"];
mediumKey = [m1,m2,m3,m4];#answer key that lets me switch between "blank" and "answer" in the questions string.

mediumQuestions = "The method "+m1[0]+"() returns a copy of the string in which the occurrences of old have been replaced with new. The "+m2[0]+"() method adds a single item to the existing list. It doesn't return a new list; rather it modifies the original list. The "+m3[0]+"() method removes and returns the element at the given index (passed as an argument) from the list. The "+m4[0]+"() method sorts the elements of a given list in a specific order - Ascending or Descending."

medium = [mediumQuestions, mediumKey];#package answer key and questions together.

# initiate variables-Hard////////////////////////////////////////////////////////////////////////////
h1 = ['"First_Blank"',"open"];
h2 = ['"Second_Blank2"',"bool"];
h3 = ['"Third_Blank3"',"all"];
h4 = ['"Fouth_Blank"',"ascii"];
hardKey = [h1,h2,h3,h4];#answer key that lets me switch between "blank" and "answer" in the questions string.

hardQuestions = "The "+h1[0]+"() function opens the file (if possible) and returns a corresponding file object. The "+h2[0]+"() method converts a value to Boolean (True or False) using the standard truth testing procedure. The "+h3[0]+"() method returns True when all elements in the given iterable are true. If not, it returns False. The "+h4[0]+"() method returns a string containing a printable representation of an object."

hard = [hardQuestions, hardKey];#package answer key and questions together.


#function that promts user for difficulty and returns it./////////////////////////////////////////
def selectDiff():
  userInput = raw_input("*** Please type easy, medium, hard to select difficulty.").lower();
  if userInput == 'easy':

    return easy;
  elif userInput == 'medium':
    return medium;
  elif userInput == 'hard':
    return hard;
  else:
    print "That is not a valid difficulty. Please try again."
    return selectDiff();

#function that promts user for number of tries and returns it./////////////////////////////////////////
def numOfTries():
	tries = raw_input("*** How many tries would you like?")
	if tries.isdigit():
		return int(tries)
	else:
		print "You must enter a number (i.e. 0,1,2...)"
		numOfTries()

#function that answers questions with user input(main function)/////////////////////////////////////////
def askQuestions(cases, questions):#recives string of questions and answer key.
  tries = numOfTries()#sets number of tries.
  currentQuestions = questions;
  for q in cases:#for every answer in the key starting from the first,request an input and replace its position in the questions string if correct.
    correct = False;
    while correct == False:
      answer = raw_input("*** Please fill in the "+ q[0] +" by typing in the correct answer.");
      if answer == q[1]:
        print "*** Great job!, that was right!"
        currentQuestions = currentQuestions.replace(q[0],q[1]);
        print currentQuestions;
        correct = True;
      else:
        tries -= 1;
        if tries == 0:
          print "*** Oh no, You ran out of tries! The game will now reset."
          currentQuestions = questions;
          runGame();
        else:
          print "*** That was not correct, only "+str(tries)+" tries left!"
  print "*** Amazing! You got them all right! The game will now reset!";
  currentQuestions = questions;
  runGame();

#function that runs askQuestions based on difficulty input/////////////////////////////////////////
def runDiff(difficulty):
  print difficulty[0];
  askQuestions(difficulty[1],difficulty[0]);

#requests deficulty and initiates game////////////////////////////////////////////////////////
def runGame():
  selectedDiff = selectDiff();
  runDiff(selectedDiff);


#start the game for the first time/////////////////////////////////////////////////////////
runGame();

# initiate variables-Easy////////////////////////////////////////////////////////////////////////////
easyAnswer1 = ['"First_Blank"',"len"]
easyAnswer2 = ['"Second_Blank"',"print"]
easyAnswer3 = ['"Third_Blank"',"return"]
easyAnswer4 = ['"Fouth_Blank"',"join"]
easyAnswerKey = [easyAnswer1,easyAnswer2,easyAnswer3,easyAnswer4]#answer key that lets me switch between "blank" and "answer" in the questions string.

easyQuestions = "The "+easyAnswer1[0]+"() function returns the number of items of an object. The "+easyAnswer2[0]+"() function prints the given object to the standard output device. The "+easyAnswer3[0]+" statement is used when a function is ready to return a value to its caller. The "+easyAnswer4[0]+"() method returns a string concatenated with the elements of an iterable."

easy = [easyQuestions, easyAnswerKey]#package answer key and questions together.

# initiate variables-Medium////////////////////////////////////////////////////////////////////////////
mediumAnswer1 = ['"First_Blank"',"replace"]
mediumAnswer2 = ['"Second_Blank"',"append"]
mediumAnswer3 = ['"Third_Blank"',"pop"]
mediumAnswer4 = ['"Fouth_Blank"',"sort"]
mediumAnswerKey = [mediumAnswer1,mediumAnswer2,mediumAnswer3,mediumAnswer4]#answer key that lets me switch between "blank" and "answer" in the questions string.

mediumQuestions = "The method "+mediumAnswer1[0]+"() returns a copy of the string in which the occurrences of old have been replaced with new. The "+mediumAnswer2[0]+"() method adds a single item to the existing list. It doesn't return a new list rather it modifies the original list. The "+mediumAnswer3[0]+"() method removes and returns the element at the given index (passed as an argument) from the list. The "+mediumAnswer4[0]+"() method sorts the elements of a given list in a specific order - Ascending or Descending."

medium = [mediumQuestions, mediumAnswerKey]#package answer key and questions together.

# initiate variables-Hard////////////////////////////////////////////////////////////////////////////
hardAnswer1 = ['"First_Blank"',"open"]
hardAnswer2 = ['"Second_Blank"',"bool"]
hardAnswer3 = ['"Third_Blank"',"all"]
hardAnswer4 = ['"Fouth_Blank"',"ascii"]
hardAnswerKey = [hardAnswer1,hardAnswer2,hardAnswer3,hardAnswer4]#answer key that lets me switch between "blank" and "answer" in the questions string.

hardQuestions = "The "+hardAnswer1[0]+"() function opens the file (if possible) and returns a corresponding file object. The "+hardAnswer2[0]+"() method converts a value to Boolean (True or False) using the standard truth testing procedure. The "+hardAnswer3[0]+"() method returns True when all elements in the given iterable are true. If not, it returns False. The "+hardAnswer4[0]+"() method returns a string containing a printable representation of an object."

hard = [hardQuestions, hardAnswerKey]#package answer key and questions together.


#Function that promts user for difficulty and returns it./////////////////////////////////////////
#INPUT: Easy, medium, or hard.
#OUTPUT: The selected difficulty.
def selectDiff():
  userInput = raw_input("*** Please type easy, medium, hard to select difficulty.").lower()
  if userInput == 'easy':
    return easy
  elif userInput == 'medium':
    return medium
  elif userInput == 'hard':
    return hard
  else:
    print "That is not a valid difficulty. Please try again."
    return selectDiff()

#Function that promts user for number of tries./////////////////////////////////////////
#INPUT:Prompts user for number of tries they would like.
#OUTPUT:The number of tries the user input
def numOfTries():
	tries = raw_input("*** How many tries would you like?")
	if tries.isdigit():
		return int(tries)
	else:
		print "You must enter a number (i.e. 0,1,2...)"
		numOfTries()

#function that checks if user is out of tries.
#INPUT:Takes the number of tries remaining and the current list of questions.
#OUTPUT:Resets game if out of tries or returns amount of tries remaining.
def checkIfOutOfTries(numOfTriesLeft, questionsString):
    if numOfTriesLeft == 0:
      print "*** Oh no, You ran out of tries! The game will now reset."
      currentQuestions = questionsString
      runGame()
    else:
      print "*** That was not correct, only "+str(numOfTriesLeft)+" tries left!"


#function that answers questions with user input(main function)/////////////////////////////////////////
#INPUT:Takes in the a list a string of questions and its matching answer keyself.
#OUTPUT:Replaces blank spot if user input is correct.Restarts game on win or loss.
def askQuestions(answerKey, questionsString):#recives string of questions and answer key.
  tries = numOfTries()#sets number of tries.
  currentQuestions = questionsString
  for blank in answerKey:#for every answer in the key starting from the first,request an input and replace its position in the questionsString string if correct.
    correct = False
    while correct == False:
      answer = raw_input("*** Please fill in the "+ blank[0] +" by typing in the correct answer.")
      if answer == blank[1]:
        print "*** Great job!, that was right!"
        currentQuestions = currentQuestions.replace(blank[0],blank[1])#Find and "switch" from blank to the correct answer in the question string.
        print currentQuestions
        correct = True
      else:
        tries -= 1
        checkIfOutOfTries(tries, questionsString)
  print "*** Amazing! You got them all right! The game will now reset!"
  currentQuestions = questionsString
  runGame()


#Requests deficulty and initiates game////////////////////////////////////////////////////////
#INPUT:Takes no input.
#OUTPUT:Runs askQuestion on the selected difficulty.
def runGame():
  selectedDiff = selectDiff()
  print selectedDiff[0]
  askQuestions(selectedDiff[1],selectedDiff[0])


#Initiate the game for the first time./////////////////////////////////////////////////////////
runGame()

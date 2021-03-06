from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0

    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None

    # For each word in the wordList
    for newWord in wordList:
        
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(newWord, hand, wordList) == True:

            # Find out how much making that word is worth
            thisScore = getWordScore(newWord, n)

            # If the score for that word is higher than your best score
            if thisScore > maxScore:
                
                # Update your best score, and best word accordingly
                maxScore = thisScore
                bestWord = newWord


    # return the best word you found.
    return bestWord


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    
    # Have the computer choose the best word
    while calculateHandlen(hand) > 0:
        print ("Current hand: "),
        displayHand(hand) 
        
        # have computer find best word from list
        compWord = compChooseWord(hand, wordList, n)
        
        # if computer couldn't find word, we're done
        if compWord == None:
            break
        
        # if computer found optimal word, display points earned and update total score
        else:
            currentScore = 0
            currentScore += getWordScore(compWord, n)
            totalScore += currentScore
            print( '"' + str(compWord) + '"' + " earned " + str(currentScore) + " points. Total : " + str(totalScore) + "points")
                
            # Update the hand 
            hand = updateHand(hand, compWord)

    # Game is over
    print("Total score: " + str(totalScore) + " points.")
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    firstHand = True
    while True:
        gameChoice = str(raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if gameChoice == 'n':
            myHand = dealHand(HAND_SIZE)
            while True:
                personORproc = str(raw_input('Enter u to have yourself play, c to have the computer play: '))
                if personORproc == 'u':
                    #person plays
                    playHand(myHand, wordList, HAND_SIZE)
                    firstHand = False
                    break
                elif personORproc == 'c':
                    #cpu plays
                    compPlayHand(myHand, wordList, HAND_SIZE)
                    firstHand = False
                    break
                else:
                    print ("Invalid command.")
        elif gameChoice == 'r' and firstHand == True:
            print ('You have not played a hand yet. Please play a new hand first!')
        elif gameChoice == 'r' and firstHand == False:
            while True:
                personORproc = str(raw_input('Enter u to have yourself play, c to have the computer play: '))
                if personORproc == 'u':
                    #person plays
                    playHand(myHand, wordList, HAND_SIZE)
                    firstHand = False
                    break
                elif personORproc == 'c':
                    #cpu plays
                    compPlayHand(myHand, wordList, HAND_SIZE)
                    firstHand = False
                    break
                else:
                    print ("Invalid command.")
        elif gameChoice == 'e':
            break
        else:
            print ("Invalid command.")

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

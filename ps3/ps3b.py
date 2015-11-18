
from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    score = 0
    words_perms = []
    wordOut = None
    for length in xrange( 1 , HAND_SIZE+1 ):
        words_perms.extend( get_perms( hand , length ) )

    for items in words_perms:
        if items in word_list:
            if score < get_word_score( items , HAND_SIZE ):
                score = get_word_score( items , HAND_SIZE )
                wordOut = items

    return wordOut

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    
    total_score = 0
    count =0
    print "Current hand is :",
    display_hand( hand )

    word_in = comp_choose_word( hand , word_list )

    while( word_in != None ):
        count = count+1
        total_score = total_score + get_word_score( word_in , HAND_SIZE )
        hand = update_hand( hand , word_in )
        print " the chosen word is:" , word_in
        print " the score of the chosen word is:", str( get_word_score( word_in , HAND_SIZE ))
        print " the remaining hand is:",
        display_hand( hand )
        print " the total score is:", str( total_score )
        word_in = comp_choose_word( hand , word_list )
    if count==0:
        print " the total score is :", 0

#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.


    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    hand = deal_hand(HAND_SIZE)

    comp_play_hand( hand , word_list )
    
#    print comp_choose_word(hand, word_list)
#    print hand

   
    

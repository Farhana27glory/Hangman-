import random
import sys
import string
import time

def print_scaffold(guesses, wd): # prints the scaffold
		if (guesses == 0):
				print ("_________")
				print ("||	 ||")
				print ("||")
				print ("||")
				print ("||")
				print ("||")
				print ("||________")
		elif (guesses == 1):
				print ("_________")
				print ("|	 ||")
				print ("|	 😐")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (guesses == 2):
				print ("_________")
				print ("|	 ||")
				print ("|	 😐")
				print ("|	 ||")
				print ("|	 ||")
				print ("|")
				print ("|________")
		elif (guesses == 3):
				print ("_________")
				print ("|	 ||")
				print ("|	 😐")
				print ("|	\||")
				print ("|	 ||")
				print ("|")
				print ("|________")
		elif (guesses == 4):
				print ("_________")
				print ("|	 ||")
				print ("|    😐")
				print ("|	\||/")
				print ("|	 ||")
				print ("|")
				print ("|________")
		elif (guesses == 5):
				print ("_________")
				print ("|	 ||")
				print ("|	 😐")
				print ("|	\||/")
				print ("|	 ||")
				print ("|	/ ")
				print ("|________")
		elif (guesses == 6):
				print ("_________")
				print ("|	 ||")
				print ("|	 😐")
				print ("|	\||/")
				print ("|	 ||")
				print ("|	/  \ ")
				print ("|________")
				print ("\n")
				print ("The word was:", wd)
				print ("\n")
				print ("\nYOU ARE DEAD! TRY AGAIN!")
				print ("\nWould you like to play again, type 1 for yes or 2 for no?")
				again = str(input("> "))
				again = again.lower()
				if again == "1":
				  hangMan()
				return

def selectWord():
  file = open('FREQ.txt')
  words = file.readlines() 
  myword = 'a'
  myword = random.choice(words)
  myword = str(myword).strip('[]')
  myword = str(myword).strip("''")
  myword = str(myword).strip("\n")
  myword = str(myword).strip("\r")
  myword = myword.lower()
  return myword


def hangMan():
  guesses = 0					
  word = selectWord()				
  word_list = list(word)	
  blanks = "_"*len(word)	
  blanks_list = list(blanks) 
  new_blanks_list = list(blanks)
  guess_list = []
  
  print ("Start guessing...\n")
  time.sleep(0.5)
  print_scaffold(guesses, word)
  print ("\n")
  print ("" + ' '.join(blanks_list))
  print ("\n")
  print ("Guess a letter now.\n")
  
  while guesses < 6:
  
  		guess = str(input("> "))
  		guess = guess.lower()
  		
  		if len(guess) > 1:
  				print ("Hold your horses! Enter one letter at time.")
  		elif guess == "":
  				print ("Gear Up! Enter one letter at a time.")
  		elif guess in guess_list:
  				print ("You already guessed that letter! Here is what you've guessed:")
  				print (' '.join(guess_list))
  		else:
  				guess_list.append(guess)
  				i = 0
  				while i < len(word):
  						if guess == word[i]:
  								new_blanks_list[i] = word_list[i]
  						i = i+1
  
  				if new_blanks_list == blanks_list:
  						print( "Your letter isn't here.")
  						guesses = guesses + 1
  						print_scaffold(guesses, word)
  						
  						if guesses < 6:
  								print ("Guess again.")
  								print (' '.join(blanks_list))
  						
  				elif word_list != blanks_list:
  						
  						blanks_list = new_blanks_list[:]
  						print (' '.join(blanks_list))
  						
  						if word_list == blanks_list:
  						  print ("\nYOU WIN! Here is your prize:")
  						  print( "\n🏆 🏆 🏆 🏆 🏆 \n")
  						  print ("Would you like to play again?")
  						  print ("Type 1 for yes or 2 for no.")
  						  again = str(input("> "))
  						  if again == "1":
  						    hangMan()
  						  quit()
  						
  						else:
  								print ("Great guess! Guess another!")
                                
                                
def main():
    name = input("What is your name? ")
    print ("Hello, " + name, "Time to play Hangman!")
    print ("Let's have fun!")
    time.sleep(1)
    hangMan()

if __name__ == "__main__":
    main()
												



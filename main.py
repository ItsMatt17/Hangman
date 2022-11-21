#Step 5

import random
from hangman_art import stages, logo
from hangman_words import word_list



#Create blanks

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter


    #Check if user is wrong.
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
  

    #Join all the elements in the list and turn it into a String.

  


randomWord = random.choice(word_list)
lives = 6
print(stages[lives])

a = list("_"*len(randomWord))

print("".join(a), randomWord)
print(logo)

givenLetters = []
while lives != 0 and "".join(a) != randomWord:
	userLetter = input("Please enter a character to guess: ").lower()
	if len(userLetter) > 1 or userLetter.isalpha() == False:
		print('invalid input')
	else:
		isFound = 0
	
		for i in range(0, len(randomWord)):
			if userLetter == randomWord[i]:
				a.pop(i)
				isFound += 1
				a.insert(i, userLetter)
				#print(isFound)
		
		
		if isFound == 0 and  userLetter not in givenLetters:
			givenLetters.append(userLetter)
			lives -= 1 
			print(f"You guessed {userLetter}, that's not in the word. You have {lives} more lives")
		
		elif userLetter in givenLetters:
			print(f"You've already guessed {userLetter}")
			print(stages[lives])
		else:
			
			print(stages[lives])
			print(f"{userLetter} is in the word!")
			givenLetters.append(userLetter)
				
		
		
			
		print("".join(a))

		
if "".join(a) == randomWord:
	print(f"You won the word was {randomWord}")

else:
	print(f"You lost the word was {randomWord}")



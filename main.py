import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear


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
		clear()

		isFound = 0
		for i in range(0, len(randomWord)):
			if userLetter == randomWord[i]:
				a.pop(i)
				isFound += 1
				a.insert(i, userLetter)
		
		
		if isFound == 0 and  userLetter not in givenLetters:
			givenLetters.append(userLetter)
			lives -= 1 
			print(f"""Letters guessed: {givenLetters}\nYou guessed {userLetter}, that's not in the word. You have {lives} more lives\n{stages[lives]}""")
		elif userLetter in givenLetters:
			print(f"""Letters guessed: {givenLetters}\nYou've already guessed {userLetter}\n{stages[lives]}""")
		
		else:
			givenLetters.append(userLetter)
			print(f"""Letters guessed: {givenLetters}\n {stages[lives]}\n{userLetter} is in the word!""")
				
		
			
			
		print("".join(a))
	
		
if "".join(a) == randomWord:
	print(f"You won, the word was {randomWord}")

else:
	print(f"You lost, the word was {randomWord}")



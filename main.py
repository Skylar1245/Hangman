import turtle
import random as R
import csv

pole = turtle;
pole.goto(10,10)

yes = ["Y","y","E","e","S","s"]
no = ["N","n","O","o"]
wordlist = []

with open('words.csv') as file:
 reader = csv.reader(file)
 for word in reader:
   wordlist.append(word[0])

secretword = R.choice(wordlist)
letters_guessed = []
word = ""

for letter in secretword:
  if letter in letters_guessed:
    word = word + letter
  else:
    word = word + "-"

print(word)
guesses = 15
print("You have", guesses,"remaining")

while (guesses != 0):
  print(secretword)
  guess = input("Guess a letter in the secret word: ")
  if guess in letters_guessed or guess.lower() in letters_guessed or guess.upper() in letters_guessed:
    print("You already guess that!")
  letters_guessed.append(guess)
  if guess in secretword or guess.lower() in secretword or guess.upper() in secretword:
    pass
  else:
    guesses -= 1
  word = ""
  for letter in secretword:
    if letter in letters_guessed or letter.upper() in letters_guessed  or letter.lower() in letters_guessed:
      word = word + letter
    else:
      word = word + "-"
  if "-" in word:
    print(word)
    print("You have",guesses,"guesses left!")
    print("")
  else:
    print("You win!")
    print("Guessed in", (len(letters_guessed)), "tries!")
    break

if guesses == 0:
  print("You ran out! The word was", secretword)
  replay = input("Do you Want to play again?")
  if replay in yes:
    guesses = 15
    



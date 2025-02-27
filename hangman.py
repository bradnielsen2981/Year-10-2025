print('\33c')
import random

listofwords = []
with open('words.txt','r') as file:
    for line in file:
        listofwords.append(line.strip())

def game():
    word = random.choice(listofwords)
    listofwords.remove(word)

    lives = 7 # user starts with 7 lives
    spacedword = '_'*len(word)
    spacedword = list(spacedword)
    print(spacedword)
    correct = 0
    while (lives > 0) and (correct < len(word)):
        letter = input("Guess: ") # user will guess a letter
        # check if letter is in word 
        if ((letter in word) and (letter not in spacedword)):
            print("You are correct!")
            for index in range(len(word)):
                if letter == word[index]:
                    spacedword[index] = letter
                    correct = correct + 1
        else:
            print("You are incorrect")
            lives = lives - 1 # false - lose a life, and draw the hangman
        print(spacedword)

    if correct < len(word):
        print("You died you loser")
    else:
        print("You survived. You champion")
    
    with open('score.txt','w') as file:
        file.write(str(correct))

response = "play"
while response == "play":
    game()
    response = input("Do you want to play again? (play/quit): ")
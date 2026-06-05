import random
# 5 predefined words
words=["aaple","banana","grape","mango","orange"]
# randomly choose a word
word=random.choice(words)
#to store guessed letters
guessed_letters=[]
# number of chances
wrong_guessed=0
max_wrong=6
print("Wlecome to my Hangman Game!")
# creat display function
def display_word():
    display=""
    for letter in word:
           if letter in guessed_letters:
               display+=letter+" "
           else:
                display+="_"
    return display
                # Game loop
while wrong_guessed < max_wrong:
                    print("\nword:",display_word())
                    print("Wrong guessed left:",max_wrong-wrong_guessed)
                    guess=input("Enter only one letter!").lower()
                    #input validation
                    if len(guess)!=1:
                       print("Enter only one letter!")
                       continue
                    if guess in guessed_letters:
                         print("Already gusesed!")
                         continue
                         gussesed_letters.append(guess)
                            #Check guess
                    if guess in word:
                           print("correct guess!")
                    else:
                      wrong_guessed+=1
                      print("Wrong guess!")
                             #Win condition
                    if all(letter in guessed_letters for letter in word):
                                        print("\n You Won! the word was:",word)
                                        break
                    if wrong_guessed==max_wrong: 
                             print("\n You lost ! the word was:",word)
                           
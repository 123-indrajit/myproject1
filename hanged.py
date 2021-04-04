# it's a hanged man game , here you will save a man , who will be hanged, when you take 5 wrong chance
# and you able to see what type of letters you already used
# here i'm using (list, tuple, variables, loops, & if , else statement )
# and random.choice function

# so at first import random

import random

# print some details for this game

print("\t\t        WELCOME TO THE HANGED MAN GAME")
print("\t\t HERE YOU WILL SAVE A MAN, WHO WILL BE HANGED")
print("\t\t    HERE YOU WLL GET ONLY 5, WRONG CHANCES")

# start button

input("\n\nPLEASE PRESS THE ENTER KEY TO START:- ")

# system bell

print("\a")
# start tuples
# if any one win this game then i use "UNHANGED"-tuple
UNHANGED = ("""
                    ----------
                 |       
                 |  |   0
                 |  |---+---|
                 |      |   |
                 |      |  
                 |      |
                 |      |
                 |   ---+---
                 |   |     |
                 |   |     |
                 |   |     |
                 |___|____ |______________
                 
                 I'M SAVE
                 THANKS;;
           """)
# loss probability tuple "HANGED"
# "HANGED"- here i'm used 5 elements
HANGMAN = ("""

               HELP ME

                ------
                |    |
                |
                |
                |
                |
                |
                |
                |
                |
                _______________

                """,
         """

               SAVE ME
                --------
                |     |
                |     0
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                ___________________
            """,
         """

                SAVE ME! PLEACE
                ---------
                |       |
                |       0
                |   /---+---/
                |
                |
                |
                |
                |
                |
                |
                |
                _________________

            """,
         """

                LAST CHANCE 
                 ----------
                 |       | 
                 |       0
                 |   /---+---/
                 |       |
                 |       |
                 |       |
                 |       |
                 |
                 |
                 |
                 |
                 |_____________________
                 """,
         """
                 I'M HANGED
                 I THINK YOU LOSS
                 CHECK THE RESULT
                  ----------
                 |       | 
                 |       0
                 |   /---+---/
                 |  |    |   |
                 |       |
                 |       |
                 |       |
                 |    ---+---
                 |    |     |
                 |    |     |
                 |    |     |
                 |_____________________
                 """,)
# start variables

# creat a list
WORD = ["location","breakfast","convenient","shuttle","mountain", "transport", "punishment","organization","measure","instrument",
        "insurance","opinion","property", "reaction","smash","regret","industry","hearing","nation"]

# use random.choice function function

word = random.choice(WORD)

# creat a list here i will be  store used letters
used = []
# create word hint variable

s = "-"*len(word)
print("WORD LENGTH HINT\n", s)
k = 0

# when guess is right then it will be store in new "str"
# later i convert new to s
new = ""
hg = len(HANGMAN)-1
# start input(1st)
guess=input("\nEnter Your Guess:- ").lower()
wrong = 0

# start loop
# if k<len(word)-1, then the loop will be run

while k <= len(word)-1:

# if s==word then it will be break

    if s == word:
        break
    if guess not in word:
        used.append(guess)
        print(HANGMAN[wrong], "\nSorry! You Wrong ")
        print("\nYour Used Alphabets is:- \n", used)
        if wrong == hg:
            break
        print("\a")
        guess = input("\nENTER YOUR GUESS:- ").lower()
        wrong = wrong+1
# convert part
    if guess in word and guess not in used:
        print("Yes!!! You Guess The Right Alphabet")

        new = ""

        for i in range(len(word)):

            if guess == word[i]:

                new = new+guess
            else:

                new = new+s[i]
        s = new
        used.append(guess)
# hint print part
        print("\nYour Used Alphabets is:- \n", used)
        print("Your Word Hint is:-\n", s)

        if s == word:
            break
        print("\a")
# another guess input
        guess = input("\nENTER YOUR GUESS:- ").lower()
        k = k+1
    if guess in used:
        print("You Already Used This")
        print("\nYour Used Alphabets is:- \n", used)
        print("\a")
        guess = input("\nENTER YOUR GUESS:- ").lower()


# win and loss probability (result)
if wrong == hg:
    print("\nSORRY YOU LOSS THIS GAME:")
    print("\nTHE WORD WAS:-", word)
    print("\a")
if s == word:
    print("CONGRATS YOU WIN")
    print(UNHANGED)
    print("\a")

print("THANKS FOR COMING")

# exit input

input("\nPLEASE PRESS THE ENTER KEY TO EXIT:-")

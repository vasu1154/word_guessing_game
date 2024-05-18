import random
print("---------------Word Guess Game---------------")
print()
name=input("What is your name : ")
print()
print("Welcome to word guessing game",name)
print()
print("---------------------------------------------")
words=['computer','java','python','coding','program','google','microsoft','flipkart','reverse', 'water', 'board', 'geeks']
word=random.choice(words)
print("Word Guess automatic by computer")
print()
print("You have a 10 chance to guess word")
print()
print("Guess a characters ")
guesses=""
chance=10
while chance>0:
    fail=0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_")
            fail+=1
    if fail==0:
        print()
        print(name,"Congratulation you win the game..")
        print()
        print("Guess Word is : ",word)
        break    
    print()        
    guess=input("Guess the character :")
    guesses+=guess
    if guess not in word:
        chance-=1
        print("You have a ",chance,"chance to guess word")
        
        if chance==0:
            print(name,"you loss the game!!")
            print(name,"better luck next time!!")    
        
            
            
    
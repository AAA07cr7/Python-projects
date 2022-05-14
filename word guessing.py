import random 
name=input("Enter your name:")
print("Good luck",name)
words = ['Donkey', 'Aeroplane', 'America', 'Program',  
         'Python', 'language', 'Cricket', 'Football',  
         'Hockey', 'Spaceship', 'bus', 'flight']  
word=random.choice(words)
print("please guess the numbers")
guess=''
turns=10
while(turns>0):
    failed=0
    for char in words:
        if char  in guess:
            print(char)
        else :
            print("_")
            failed+=1
    if(failed==0):
        print("you won")
        print("Correct word is",word)
        break
    guesses=input("Enter another input")
    guess+=guesses
    if guesses not in (word):
        turns-=1
        print("wrong guess")
        print("You have ", + turns, 'more guesses ')   
        if turns == 0:  
            print("User Loose")  
    

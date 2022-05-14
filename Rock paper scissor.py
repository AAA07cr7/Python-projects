import random
options=['Rock','Paper','Scissor']
while(True):
    print("WELCOME TO ROCK,PAPER AND SCISSOR GAME")
    print("Player it's your turn press 1 for Rock ,2 for paper and 3 for scissor")
    choice=int(input("Enter your choice"))
    if(choice>3 or choice<1):
        choice=int(input("Enter a valid choice:"))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
    print(f"player has choosen {choice_name}")
    
    computer=random.choice(options)
    print(f"computer's {computer} vs player's {choice_name}")
    if(computer==choice_name):
        print("draw")
    elif(computer=='Rock' and choice_name == 'paper'):
        print("Player won")
    elif(choice_name == 'Rock' and computer=='Paper'):
        print("computer won")
    elif(computer=='Rock' and choice_name == 'scissor'):
        print("computer won")
    elif(choice_name == 'scissor' and computer=='Rock'):
        print("Player won")
    elif(computer=='paper' and choice_name == 'scissor'):
        print("Player won")
    elif(choice_name =='paper' and computer=='scissor'):
        print("computer won") 

import random
choice =['Rock','Paper','Scissor']
n= int(input("Enter the Number of times you Want to play:  "))
youwin,computerwin=0,0
for i in range(1,n+1):
    print("Round ",i,"Start:")
    userchoice= input("Select Your Choice->\n 1.Rock\n 2.Paper\n 3.Scissor\n")
    computerchoice=random.choice(choice)
    print("You Select: ",userchoice)
    print("Computer Select: ",computerchoice)
    if userchoice =='Rock':
        if computerchoice=='Scissor':
            print("You win This round",i)
            youwin+=1
        elif computerchoice== 'Rock':
                print("This Round is Draw")
                # youwin+=1
                # computerwin+=1
        else:
            print("You loose This Round")
            computerwin+=1
    elif userchoice =='Paper':
        if computerchoice=='Rock':
            print("You win This round",i)
            youwin+=1
        elif computerchoice=='Paper':
            print("This Round is Draw")
            # youwin+=1
            # computerwin+=1
        else:
            print("You loose This Round")
            computerwin+=1
    elif userchoice=='Scissor':
        if computerchoice== 'Paper':
            print("You Win this Round")
            youwin+=1
        elif computerchoice=='Scissor':
            print("This Round is Draw")
            # youwin+=1
            # computerwin+=1
        else:
            print("You Loose this Round")
            computerwin+=1
print("Your Score: ",youwin)
print("Computer Score: ",computerwin)
if youwin>computerwin:
    print("You Win")
elif youwin==computerwin:
    print("Game Drawn")
else:
    print("You Loose")
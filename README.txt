---- Rock, Paper and Scissor Game ----

1 = Rock
2 = Paper
3 = Scissor


# Brute force approach
if(computer==your_ch) means Tie.
Otherwise
computer = 1(Rock)
	your_ch = 2(Paper) --> You Win
	your_ch = 3(Scissor) --> You Lose
computer = 2(Paper)
	your_ch = 1(Rock) --> You Lose
	your_ch = 3(Scissor) --> You Win
computer = 3(Scissor)
	your_ch = 1(Rock) --> You Win
	your_ch = 3(Paper) --> You Lose

# Code
if(computer == your_ch):
    print("It's a Tie.")
else:
    if(computer==1 and your_ch==2):
        print("You Win.")
    elif(computer==1 and your_ch==3):
        print("You Lose!")
    elif(computer==2 and your_ch==1):
        print("You Lose!")
    elif(computer==2 and your_ch==3):
        print("You Win.")
    elif(computer==3 and your_ch==1):
        print("You Win.")
    elif(computer==3 and your_ch==2):
        print("You Lose!")
    else:
        print("Error 404!")


#Optimized Approach
We use (your_ch - computer) to optimize our code :

your_ch(Rock=1) - computer(Rock=1) = 0(Tie)
your_ch(Paper=2) - computer(Rock=1) = 1(Win)
your_ch(Scissor=3) - computer(Rock=1) = 2(Lose)

your_ch(Rock=1) - computer(Paper=2) = -1(Lose)
your_ch(Paper=2) - computer(Paper=2) = 0(Tie)
your_ch(Scissor=3) - computer(Paper=2) = 1(Win)

your_ch(Rock=1) - computer(Scissor=3) = -2(Win)
your_ch(Paper=2) - computer(Scissor=3) = -1(Lose)
your_ch(Scissor=3) - computer(Scissor=3) = 0(Tie)

Concusion is :
if (your_ch - computer) = 0 or (computer == your_ch)
	Tie
if (your_ch - computer) = 1 or -2
	You Win
if (your_ch - computer) = -1 or 2
	You Lose

#Code
if((your_ch-computer) == 1 or (your_ch-computer) == -2):
        print("You Win.")
else:
        print("You Lose!")
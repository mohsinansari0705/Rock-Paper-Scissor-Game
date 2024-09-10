import random

print("""Enter
r for Rock,
p for Paper,
s for Scissor &
STOP to break.""")

dict_ch = {"r":1, "p":2, "s":3}
reverse_dict_ch = {1:"Rock", 2:"Paper", 3:"Scissor"}

while True:
    computer = random.choice([1, 2, 3])

    ch = input("\nEnter your choice : ")
    your_ch = dict_ch.get(ch)

    if(ch.lower() == "stop"):
        break
    else:
        print(f"\nYou choose : {reverse_dict_ch.get(your_ch)}\nComputer choose : {reverse_dict_ch[computer]}")

        if(not(ch=="r" or ch=="p" or ch=="s")):
            print("Error 404")
        elif(computer == your_ch):
            print("It's a Tie.")
        else:
            if((your_ch-computer) == 1 or (your_ch-computer) == -2):
                print("You Win.")
            else:
                print("You Lose!")
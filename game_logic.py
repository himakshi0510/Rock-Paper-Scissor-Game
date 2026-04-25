import random 
def game():
    computer = random.choice([-1,0,1])
    your_choice = input("enter your choice[rock(r),paper(p),scissor(s)]:")
    youstr = {"r":-1,"p":0,"s":1}
    you = youstr[your_choice]
    reversedict = {-1:"ROCK",0:"PAPER",1:"SCISSOR"}
    print(f"your choice is {reversedict[you]} and computer's choice is {reversedict[computer]}")
    if you == computer:
        print("it's draw.")
    else:
        if (you == -1 and computer == 0):
            print("you lose.")
        elif (you == 0 and computer == 1):
            print("you lose.")
        elif (you == 1 and computer == -1):
            print("you lose.") 
        elif (you == 0 and computer == -1):
            print("you win.")
        elif (you == 1 and computer == 0):
            print("you win.")
        elif (you == -1 and computer == 1):
            print("you win.")
        else:
            print("there's problem")
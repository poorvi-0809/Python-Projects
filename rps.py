import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice= input("Type 0 for rock, 1 for paper and 2 for scissors\n")
hand =["rock", "paper", "scissors"]
if choice== "0":
    print(rock)
    comp= random.choice(hand)
    if comp == "rock":
        print(f"Computer chose {rock}")
        print("Tie")
    elif comp== "paper":
        print(f"Computer chose {paper}")
        print("You lose")
    elif comp == "scissors":
        print(f"Computer chose {scissors}")
        print("You won")
elif choice=="1":
    print(paper)
    comp = random.choice(hand)
    if comp == "rock":
        print(f"Computer chose {rock}")
        print("You win")
    elif comp == "paper":
        print(f"Computer chose {paper}")
        print("Tie")
    elif comp == "scissors":
        print(f"Computer chose {scissors}")
        print("You lose")
elif choice =="2":
    print(scissors)
    comp = random.choice(hand)
    if comp == "rock":
        print(f"Computer chose {rock}")
        print("You lose")
    elif comp == "paper":
        print(f"Computer chose {paper}")
        print("You win")
    elif comp == "scissors":
        print(f"Computer chose {scissors}")
        print("Tie")
else:
    print("Invalid choice")

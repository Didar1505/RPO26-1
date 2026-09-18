rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """
scissor = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """

import random
art = {0:rock, 1:scissor, 2: paper}
user_score = 0
comp_score = 0

while user_score < 3 and comp_score < 3:
    print("Your score:", user_score)
    print("Computer score:", comp_score)
    move = int(input("Что вы выбераете? 0-камень, 1-ножницы, 2-бумага.\n"))
    comp = random.randint(0,2)

    print(art[move])
    print(art[comp])
    if (move == 0 and comp == 1) or (move == 1 and comp==2) or (move == 2 and comp ==0):
        print("you won")
        user_score += 1
    elif move == comp:
        print("it is tie")
    else:
        print("you lost")
        comp_score += 1
    print("="*30)
print("Hang Man")

print("""
Player 1 picks the secret word for Player 2 to guess.

You have 15 Guesses.

Type 'hint' for a hint.
Type 'help' for this help.
""")


def guesses_left():
    print("You have {} guesses {}".format(guesses, player_two_name))


def draw_1():
    print("__________")


def draw_2():
    print("""
| 
|         
|__________
""")


def draw_3():
    print("""
|   
|          |
|__________|
""")


def draw_4():
    print("""
|    ______
|          |
|__________|
""")


def draw_5():
    print("""
|   |______
|          |
|__________|
""")


def draw_6():
    print("""
       
  |          
  |       
  |    
  |   
 _|_
|   |______
|          |
|__________|
""")


def draw_7():
    print("""
________
  |         
  |          
  |       
  |    
  |   
 _|_
|   |______
|          |
|__________|
""")


def draw_8():
    print("""
________
  |    |      
  |          
  |        
  |    
  |   
 _|_
|   |______
|          |
|__________|
""")


def draw_9():
    print("""
________
  |    |      
  |    o      
  |        
  |    
  |   
 _|_
|   |______
|          |
|__________|
""")


def draw_10():
    print("""
________
  |    |      
  |    o      
  |    |     
  |    |
  |   
 _|_
|   |______
|          |
|__________|
""")


def draw_11():
    print("""
________
  |    |      
  |    o      
  |   /|     
  |    |
  |   
 _|_
|   |______
|          |
|__________|
""")


def draw_12():
    print("""
________
  |    |      
  |    o      
  |   /|\     
  |    |
  |   
 _|_
|   |______
|          |
|__________|    
""")


def draw_13():
    print("""
________
  |    |      
  |    o      
  |   /|\     
  |    |
  |   < 
 _|_
|   |______
|          |
|__________|
""")


def draw_14():
    print("""
________
  |    |      ***************
  |    o      *  Game Over  *
  |   /|\     *************** 
  |    |
  |   < >
 _|_
|   |______
|          |
|__________|
""")


guesses = 14


player_one_name = input("Player 1: What is your name:  ")
player_two_name = input("PLayer 2: What is your name:  ")

player_one = input("{}, enter a word:  ".format(player_one_name))


while True:
    guesses_left()

    player_two = input("Guess my word:  ")

    if player_two == player_one:
        print("Great {}, You won!".format(player_two))
        break
    else:
        guesses -= 1

    if guesses == 13:
        draw_1()
        continue
    elif guesses == 12:
        draw_2()
        continue
    elif guesses == 11:
        draw_3()
        continue
    elif guesses == 10:
        draw_4()
        continue
    elif guesses == 9:
        draw_5()
        continue
    elif guesses == 8:
        draw_6()
        continue
    elif guesses == 7:
        draw_7()
        continue
    elif guesses == 6:
        draw_8()
        continue
    elif guesses == 5:
        draw_9()
        continue
    elif guesses == 4:
        draw_10()
        continue
    elif guesses == 3:
        draw_11()
        continue
    elif guesses == 2:
        draw_12()
        continue
    elif guesses == 1:
        draw_13()
        continue
    elif guesses == 0:
        draw_14()
        print("\n" * 2)
        print("{}, You won!".format(player_one_name))
        break




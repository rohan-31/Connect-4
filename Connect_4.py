import random
import os


#Creating the playing board

Board = []
Rows = int(input("Enter the number of rows of the playing board(6 to 26 rows): "))     
Columns = int(input("Enter the number of columns of the playing board(7 to 26 columns): "))
if (Rows < 6 or Rows > 26) or (Columns < 7 or Columns > 26):      # Restricts the number of rows between 6 and 26 and columns between 7 and 26.
    print("Please enter a valid number of rows and columns")

else:
    Correspond = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M": 12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
    Correspond1 = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z"}

    def printer():             # Function defined to print the board.
        os.system("clear")
        for cols in range(Columns):
            print('  ' + Correspond1[cols], end=' ')

        print("\n +" + "---+" * (Columns))
        for row in range(Rows):
            print( ' | ', end=' ')
            for col in range(Columns):
                  print(Board[row][col] + '| ', end=' ')  
            print("\n +"+"---+"* (Columns))
    for r in range(Rows):     
        Row = []
        for c in range(Columns):
            Row.append(" ")        # Initializing the board with spaces in each square.
        Board.append(Row)
    print("                Initial Board")
    printer()

    # Function to determine the end of the game

    def endgame():
        run = True 
        while run == True:
            run = False
            # Horizontal win check
            for row in range(Rows):
                for col in range(Columns-3):
                    if Board[row][col] != " " and Board[row][col+1] != " " and Board[row][col+2] != " " and Board[row][col+3] != " ":    #Checking if adjacent spaces are filled.
                        Piece = Board[row][col]
                        if Board[row][col+1] == Piece and Board[row][col+2] == Piece and Board[row][col+3] == Piece:
                            run = True
            # Vertical win check
            for row in range(Rows):
                for col in range(Columns):
                    if Board[row][col] != " " and Board[row-1][col] != " " and Board[row-2][col] != " " and Board[row-3][col] != " ":    #Checking if adjacent spaces are filled.
                        Piece = Board[row][col]
                        if Board[row-1][col] == Piece and Board[row-2][col] == Piece and Board[row-3][col] == Piece:
                            run = True
            # Diagonal win check
            for row in range(Rows-3):
                for col in range(Columns-3):
                        if (Board[row][col] != " " and Board[row+1][col+1] != " " and Board[row+2][col+2] != " " and Board[row+3][col+3] != " "):     #Checking if adjacent spaces are filled.
                            Piece = Board[row][col]
                            if Board[row+1][col+1] == Piece and Board[row+2][col+2] == Piece and Board[row+3][col+3] == Piece:
                                run = True
                        elif Board[row+3][col] != " " and Board[row+2][col+1] != " " and Board[row+1][col+2] != " " and Board[row][col+3] != " ":
                            Piece = Board[row+3][col]
                            if Board[row+2][col+1] == Piece and Board[row+1][col+2] == Piece and Board[row][col+3] == Piece:
                                run = True
                        
            if run == True:
                return "Game over"
    
# User Inputs

    NUM_PLAYERS = int(input("Enter the number of players(2 to 5 players): "))
    if NUM_PLAYERS < 2 or NUM_PLAYERS > 5:
            print("Enter a valid number of players")
    else:
        print("         Player 1 starts with O. Player 2 starts with X. Player 3 starts with V. Player 4 starts with H. Player 5 starts with M.")
        count = 0
        turn = -2     # Initailizing count and turn variables.
        Player_Dict = {0: "Player_1", 1:"Player_2", 2:"Player_3", 3:"Player_4", 4:"Player_5"}
        first_turn = random.randint(0,NUM_PLAYERS - 1)
        User = Player_Dict[first_turn]
        turn = first_turn
        Correspond_1 = []
        if User == "Player_1":
            print("You are Player 1. Your will start and your default input will be an 'O'")           # Determines which player starts the game.
        if User == "Player_2":
            print("You are Player 2. Your will start and your default input will be an 'X'")
        if User == "Player_3":
            print("You are Player 3. Your will start and your default input will be an 'V'")
        if User == "Player_4":
            print("You are Player 4. Your will start and your default input will be an 'H'")
        if User == "Player_5":
            print("You are Player 5. Your will start and your default input will be an 'M'")
        while turn<6:
            count = 0
            if turn == 0:
                for row in range(len(Board)):
                    for element in Board[row]:
                        if element == " ":      # Used to check if there are any empty spaces on the board.
                            count+=1
                if count == 0:
                    print("Game drawn.")
                    turn = 6                     # If there are no empty spaces, this terminates the game and results in a draw.
                else:
                    while turn == 0:
                        Place = input("Enter the column in which you want to place your piece(eg : A will place your token in the first column) : ")     # Input function to place your piece in the square.
                        for i in Correspond:
                            if Correspond[i] < Columns:
                                Correspond_1.append(i)
                        if Place not in Correspond_1:
                            print("Please enter a valid column within the given dimensions of the board")
                            continue
                        if Board[Rows-1][Correspond[Place]] == " ":
                            Board[Rows-1][Correspond[Place]] = "O"
                            printer()
                        elif Board[Rows-1][Correspond[Place]] != " ":
                            if Board[0][Correspond[Place]] != " ":
                                print("Invalid turn. This column is full.")     # Used to penalize invalid inputs and skip the player's turn.
                                turn += 1
                                if turn == 1:
                                    print("Player 2 plays now")                 # Switching turn to player 2
                                break
                            else:
                                Board[0][Correspond[Place]] = "O"
                                run = True
                                while run == True:
                                    run = False
                                    for row in range(Rows - 2, -1, -1):
                                        for col in range(Columns):
                                            if Board[row][col] != " " and Board[row+1][col] == " ":
                                                Board[row][col] = " "
                                                Board[row+1][col] = "O"
                                                run = True
                                printer()        
                        checker = endgame()
                        if checker == "Game over":
                            print("Game over.", Player_Dict[turn], "has won the game.")
                            turn = 6
                            break        
                        turn+=1                     # Switching turn to player 2
                        if turn == 1:
                            print("Player 2 plays now")
            count = 0
            if turn == 1:
                for row in range(len(Board)):
                    for element in Board[row]:
                        if element == " ":         # Used to check if there are any empty spaces on the board.
                            count+=1
                if count == 0:
                    print("Game drawn.")
                    turn = 6                       # If there are no empty spaces, this terminates the game and results in a draw.
                else:
                    while turn == 1:
                        Place = input("Enter the square in which you want to place your piece : ")    # Input function to place your piece in the square.
                        for i in Correspond:
                            if Correspond[i] < Columns:
                                Correspond_1.append(i) # Appending the corresponding alphabetic column names into a list to restrict invalid token entries.
                        if Place not in Correspond_1:
                            print("Please enter a valid column within the given dimensions of the board")
                            continue
                        if Board[Rows-1][Correspond[Place]] == " ":
                            Board[Rows-1][Correspond[Place]] = "X"
                            printer()
                        elif Board[Rows-1][Correspond[Place]] != " ":
                            if Board[0][Correspond[Place]] != " ":
                                print("Invalid turn. This column is full.")          # Used to penalize invalid inputs and skip the player's turn.
                                if NUM_PLAYERS == 2:
                                    turn-=1                                           # Switching turn to player 1
                                    if turn == 0:
                                        print("Player 1 plays now")
                                    break
                                else:
                                    turn+=1
                                    if turn == 2:
                                        print("Player 3 plays now")
                                    break
                            else:
                                Board[0][Correspond[Place]] = "X"
                                run = True
                                while run == True:
                                    run = False
                                    for row in range(Rows - 2, -1, -1):
                                        for col in range(Columns):
                                            if Board[row][col] != " " and Board[row+1][col] == " ":
                                                Board[row][col] = " "
                                                Board[row+1][col] = "X"
                                                run = True
                                printer()
                        checker = endgame()
                        if checker == "Game over":
                            print("Game over.", Player_Dict[turn], "has won the game.")
                            turn = 6
                            break                                
                        if NUM_PLAYERS == 2:
                            turn-=1                                           # Switching turn to player 1
                            if turn == 0:
                                print("Player 1 plays now")
                        else:                                                 # Switching turn to player 3
                            turn+=1
                            if turn == 2:
                                print("Player 3 plays now")
            if turn == 2:
                for row in range(len(Board)):
                    for element in Board[row]:
                        if element == " ":      # Used to check if there are any empty spaces on the board.
                            count+=1
                if count == 0:
                    print("Game drawn.")
                    turn = 6                     # If there are no empty spaces, this terminates the game and results in a draw.
                else:
                    while turn == 2:
                        Place = input("Enter the square in which you want to place your piece : ")    # Input function to place your piece in the square.
                        for i in Correspond:
                            if Correspond[i] < Columns:
                                Correspond_1.append(i) # Appending the corresponding alphabetic column names into a list to restrict invalid token entries.
                        if Place not in Correspond_1:
                            print("Please enter a valid column within the given dimensions of the board")
                            continue
                        if Board[Rows-1][Correspond[Place]] == " ":
                            Board[Rows-1][Correspond[Place]] = "V"
                            printer()
                        elif Board[Rows-1][Correspond[Place]] != " ":
                            if Board[0][Correspond[Place]] != " ":
                                print("Invalid turn. This column is full.")             # Used to penalize invalid inputs and skip the player's turn.
                                if NUM_PLAYERS == 3:
                                    turn-=2                                           # Switching turn to player 1
                                    if turn == 0:
                                        print("Player 1 plays now")
                                    break
                                else:
                                    turn+=1
                                    if turn == 3:
                                        print("Player 4 plays now")
                                    break
                            else:
                                Board[0][Correspond[Place]] = "V"
                                run = True
                                while run == True:
                                    run = False
                                    for row in range(Rows - 2, -1, -1):
                                        for col in range(Columns):
                                            if Board[row][col] != " " and Board[row+1][col] == " ":
                                                Board[row][col] = " "
                                                Board[row+1][col] = "V"
                                                run = True
                        printer()
                        checker = endgame()
                        if checker == "Game over":
                            print("Game over.", Player_Dict[turn], "has won the game.")
                            turn = 6
                            break
                        if NUM_PLAYERS == 3:
                            turn-=2                                           # Switching turn to player 1
                            if turn == 0:
                                print("Player 1 plays now")
                        else:                                                # Switching turn to player 4
                            turn+=1
                            if turn == 3:
                                print("Player 4 plays now")
            if turn == 3:
                for row in range(len(Board)):
                    for element in Board[row]:
                        if element == " ":      # Used to check if there are any empty spaces on the board and results in a draw.
                            count+=1
                if count == 0:
                    print("Game drawn.")
                    turn = 6                     # If there are no empty spaces, this terminates the game.
                else:
                    while turn == 3:
                        Place = input("Enter the column in which you want to place your piece(eg : A will place your token in the first column) : ")     # Input function to place your piece in the square.
                        for i in Correspond:
                            if Correspond[i] < Columns:
                                Correspond_1.append(i)
                        if Place not in Correspond_1:
                            print("Please enter a valid column within the given dimensions of the board")
                            continue
                        if Board[Rows-1][Correspond[Place]] == " ":
                            Board[Rows-1][Correspond[Place]] = "H"
                            printer()
                        elif Board[Rows-1][Correspond[Place]] != " ":
                            if Board[0][Correspond[Place]] != " ":
                                print("Invalid turn. This column is full.")
                                if NUM_PLAYERS == 4:
                                    turn-=3                                           # Switching turn to player 1
                                    if turn == 0:
                                        print("Player 1 plays now")
                                    break
                                else:
                                    turn+=1
                                    if turn == 4:
                                        print("Player 5 plays now")
                                    break
                            else:
                                Board[0][Correspond[Place]] = "H"
                                run = True
                                while run == True:
                                    run = False
                                    for row in range(Rows - 2, -1, -1):
                                        for col in range(Columns):
                                            if Board[row][col] != " " and Board[row+1][col] == " ":
                                                Board[row][col] = " "
                                                Board[row+1][col] = "H"
                                                run = True
                                printer()
                        checker = endgame()
                        if checker == "Game over":
                            print("Game over.", Player_Dict[turn], "has won the game.")
                            turn = 6
                            break
                        if NUM_PLAYERS == 4:
                            turn-=3                                           # Switching turn to player 1
                            if turn == 0:
                                print("Player 1 plays now")
                        else:
                            turn+=1                     # Switching turn to player 5
                            if turn == 4:
                                print("Player 5 plays now")
            if turn == 4:
                for row in range(len(Board)):
                    for element in Board[row]:
                        if element == " ":      # Used to check if there are any empty spaces on the board.
                            count+=1
                if count == 0:
                    print("Game drawn")
                    turn = 6                     # If there are no empty spaces, this terminates the game.
                else:
                    while turn == 4:
                        Place = input("Enter the column in which you want to place your piece(eg : A will place your token in the first column) : ")     # Input function to place your piece in the square.
                        for i in Correspond:
                            if Correspond[i] < Columns:
                                Correspond_1.append(i)
                        if Place not in Correspond_1:
                            print("Please enter a valid column within the given dimensions of the board")
                            continue
                        if Board[Rows-1][Correspond[Place]] == " ":
                            Board[Rows-1][Correspond[Place]] = "M"
                            printer()
                        elif Board[Rows-1][Correspond[Place]] != " ":
                            if Board[0][Correspond[Place]] != " ":
                                print("Invalid turn. This column is full.")                # Used to penalize invalid inputs and skip the player's turn.
                                turn-=4                     # Switching turn to player 1
                                if turn == 0:
                                    print("Player 1 plays now")
                                break
                            else:
                                Board[0][Correspond[Place]] = "M"
                                run = True
                                while run == True:
                                    run = False
                                    for row in range(Rows - 2, -1, -1):
                                        for col in range(Columns):
                                            if Board[row][col] != " " and Board[row+1][col] == " ":
                                                Board[row][col] = " "
                                                Board[row+1][col] = "M"
                                                run = True
                                printer()
                        checker = endgame()
                        if checker == "Game over":
                            print("Game over.", Player_Dict[turn], "has won the game.")
                            turn = 6
                            break
                        turn-=4                     # Switching turn to player 1
                        if turn == 0:
                            print("Player 1 plays now")
                
         

        

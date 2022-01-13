# CSE 210 Week 02 Ponder and Prove: Tic-Tac-Toe Assignment - Erin Strydom

# Create the playing board.
board = {'1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' ' }

# Create the main function.
def main():

    # Call the game function.
    game(board)

# Create the print_board function to print the playing board when called.
def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Create the game function.
def game(board):

    count = 0
    turn = 'X'

    # Iterate through this loop ten times to give enough time to play the game. (There are only 9 possible moves)
    for i in range(9):

        # Print the board every turn
        print_board(board)

        # Ask the user whose turn it is where they want to place their move.
        move = input("\nIt's your turn " + turn + ". Where do you want to place your move? ")

        # Place the user's move on the board, first checking that it is a valid move.
        if board[move] == ' ':
            board[move] = turn

            # Check if they won by calling the win function.
            win(board, turn)

            # Use this if/else statement to swap players
            if turn =='X':
                turn = 'O'
            else:
                turn = 'X'
            count += 1

        # In case the move is invalid.
        else:
            print("That place has already been taken. \nWhich place do you want to move to?")


        # Use this in case of a draw.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a draw.")

# Create the win function to see if a player has won the game.
def win(board, turn):
        
        # Create a boolian variable.
        game = True

        # Use a while loop to iterate through the various methods of winning.
        while game == True:

            # Win horizontally.
            if board['1'] == board['2'] == board['3'] != ' ':
                print_board(board)
                print("\nGame Over. " + turn + " won.")
                game = False
                break

            # Win horizontally.
            elif board['4'] == board['5'] == board['6'] != ' ':
                print_board(board)
                print("\nGame Over. " + turn + " won.")
                game = False
                break

            # Win horizontally.
            elif board['7'] == board['8'] == board['9'] != ' ':
                print_board(board)
                print("\nGame Over. " + turn + " won.")
                game = False
                break

            # Win vertically.
            elif board['1'] == board['4'] == board['7'] != ' ':
                print_board(board)
                print("\nGame Over. " + turn + " won.")
                game = False
                break

            # Win vertically.
            elif board['2'] == board['5'] == board['8'] != ' ':
                print_board(board)
                print("\nGame Over. " + turn + " won.")
                game = False
                break

            # Win vertically.
            elif board['3'] == board['6'] == board['9'] != ' ':
                print_board(board)
                print("\nGame Over. " + turn + " won.")
                game = False
                break

            # Win diagonally.
            elif board['1'] == board['5'] == board['8'] != ' ':
                print_board(board)
                print("\nGame Over. " + turn + " won.")
                game = False
                break

            # Win diagonally.
            elif board['7'] == board['5'] == board['7'] != ' ':
                print_board(board)
                print("\nGame Over. " + turn + " won.")
                game = False
                break

            # If no one has won this round, exit the loop and return to the game function.
            else:
                game = True
                break

if __name__ == "__main__":
    main()
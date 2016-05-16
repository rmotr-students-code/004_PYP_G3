"""
Write a simple program to play a game of Tic-Tac-Toe. The game is between two 
players. The computer starts displaying the board with all the empty spots 
and asks for the first move. The computer asks each player for her move; the 
player will inform the coordinates to place her mark with a letter and a 
number; the letter indicating the column and the number the row. Example: B2 
is the center of the board. A1 is the top left corner of the board. C3 is the 
bottom right corner (furthermost from the A1).

The computer will keep asking both player for their marks until one of them 
win or there are no more places in the board to position marks.
"""

class Player:
    def __init__(self, symbol, moves):
        self.symbol = symbol
        self.moves = moves
        
x = Player('X', [])
o = Player('O', [])

board = {'A1': ' ', 
         'A2': ' ', 
         'A3': ' ', 
         'B1': ' ',
         'B2': ' ',
         'B3': ' ',
         'C1': ' ',
         'C2': ' ',
         'C3': ' '
         }

# Print Board
def print_board():
    print ""
    print "  1 2 3"
    print " -------"
    print "A|" + board['A1'] + '|' + board['A2'] + '|' + board['A3'] + '|'
    print " |-----|"
    print "B|" + board['B1'] + '|' + board['B2'] + '|' + board['B3'] + '|'
    print " |-----|"
    print "C|" + board['C1'] + '|' + board['C2'] + '|' + board['C3'] + '|'
    print " -------"
    print ""
    
# make move
def make_move(player, opponent):
    # Ask for move
    move = raw_input("Which space do you wish to move {}?: ".format(player.symbol)).upper()
    # Check if move is valid
    valid_move = False
    while valid_move == False:
        valid_move = True
        if move in player.moves or move in opponent.moves:
            move = raw_input("Please enter a valid move: ").upper()
        elif move not in ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']:
            move = raw_input("Please enter a valid move: ").upper()
        else:
            valid_move = True
        
    # Update player list
    player.moves.append(move)
    # Update board
    board[move] = player.symbol
    
# Determine Win
def check_win(player):
    win = (['A1', 'A2', 'A3'],
           ['A1', 'B2', 'C3'],
           ['A1', 'B1', 'C1'],
           ['A2', 'B2', 'C2'],
           ['A3', 'B2', 'C1'],
           ['A3', 'B4', 'C3'],
           ['B1', 'B2', 'B3'],
           ['C1', 'C2', 'C3']
          )
    for x in win:
        if x[0] in player.moves and x[1] in player.moves and x[2] in player.moves:
            return True
        
    return False
    
# Play game
def play():
    print "Welcome to Tic-Tac-Toe!"
    while check_win(x) == False and check_win(o) == False:
        print_board()
        make_move(o, x)
        if check_win(o) == True:
            print_board()
            print "Player O Wins!"
            quit()
        print_board()
        
        make_move(x, o)
        if check_win(x) == True:
            print_board()
            print "Player X Wins!"
            quit()
        print_board()
        
play()
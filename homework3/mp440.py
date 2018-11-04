from copy import copy, deepcopy #Makes copying 2D arrays into new memory addresses really easy
import heapq as hq

'''
Compute the value brought by a given move by placing a new token for player
at (row, column). The value is the number of opponent pieces getting flipped
by the move. 

A move is valid if for the player, the location specified by (row, column) is
(1) empty and (2) will cause some pieces from the other player to flip. The
return value for the function should be the number of pieces hat will be moved.
If the move is not valid, then the value 0 (zero) should be returned. Note
here that row and column both start with index 0. 
'''
def check_up(state, player, row, column):
    opponent = 'W' if player == 'B' else 'B'
    flipped = 0
    i = row + 1
    j = column
    while i < len(state):
        if state[i][j] == opponent:
            flipped += 1
            i += 1 
        #No sandwiching player piece:
        elif state[i][j] == ' ': 
            return 0 
        elif state[i][j] == player:
            return flipped
    return 0

def check_down(state, player, row, column):
    opponent = 'W' if player == 'B' else 'B'
    flipped = 0
    i = row - 1
    j = column
    while i >= 0:
        if state[i][j] == opponent:
            flipped += 1
            i -= 1 
        elif state[i][j] == ' ': 
            return 0 
        elif state[i][j] == player:
            return flipped
    return 0

def check_right(state, player, row, column):
    opponent = 'W' if player == 'B' else 'B'
    flipped = 0
    i = row
    j = column + 1
    while j < len(state[i]):
        if state[i][j] == opponent:
            flipped += 1
            j += 1 
        elif state[i][j] == ' ': 
            return 0
        elif state[i][j] == player:
            return flipped 

    return 0

def check_left(state, player, row, column):
    opponent = 'W' if player == 'B' else 'B'
    flipped = 0
    i = row
    j = column - 1
    while j >= 0:
        if state[i][j] == opponent:
            flipped += 1
            j -= 1 
        elif state[i][j] == ' ': 
            return 0 
        elif state[i][j] == player:
            return flipped
    return 0

def check_diagonal_bottom_right(state, player, row, column):
    opponent = 'W' if player == 'B' else 'B' 
    flipped = 0
    i = row + 1
    j = column + 1
    while i < len(state) and j < len(state[i]):
        if state[i][j] == opponent:
            flipped += 1
            i += 1 
            j += 1
        elif state[i][j] == ' ': 
            return 0 
        elif state[i][j] == player:
            return flipped
    return 0

def check_diagonal_bottom_left(state, player, row, column):
    opponent = 'W' if player == 'B' else 'B' 
    flipped = 0
    i = row + 1
    j = column - 1
    while i < len(state) and j >= 0:
        if state[i][j] == opponent:
            flipped += 1
            i += 1 
            j -= 1
        elif state[i][j] == ' ': 
            return 0
        elif state[i][j] == player:
            return flipped
    return 0


def check_diagonal_top_right(state, player, row, column):
    opponent = 'W' if player == 'B' else 'B' 
    flipped = 0
    i = row - 1
    j = column + 1
    while i >= 0 and j < len(state[i]):
        if state[i][j] == opponent:
            flipped += 1
            i -= 1 
            j += 1
        elif state[i][j] == ' ': 
            return 0 
        elif state[i][j] == player:
            return flipped
    return 0


def check_diagonal_top_left(state, player, row, column):
    opponent = 'W' if player == 'B' else 'B' 
    flipped = 0
    i = row - 1
    j = column - 1
    while i >= 0 and j < len(state[i]):
        if state[i][j] == opponent:
            flipped += 1
            i -= 1 
            j -= 1
        elif state[i][j] == ' ': 
            return 0 
        elif state[i][j] == player:
            return flipped
    return 0


def get_move_value(state, player, row, column):
    total_flipped = 0

    total_flipped += check_up(state, player, row, column)
    total_flipped += check_down(state, player, row, column)
    total_flipped += check_right(state, player, row, column)
    total_flipped += check_diagonal_top_right(state, player, row, column)
    total_flipped += check_diagonal_top_left(state, player, row, column)
    total_flipped += check_diagonal_bottom_right(state, player, row, column)
    total_flipped += check_diagonal_bottom_left(state, player, row, column)

    return total_flipped

'''
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 
'''
def execute_move(old_state, player, row, column):
    if row > len(old_state) or row < 0 or column > len(old_state[0]) or column < 0:
        return None

    state = deepcopy(old_state)
    state[row][column] = player
     
    opponent = 'W' if player == 'B' else 'B'
    
    #Check if you gain points flipping pieces above
    if check_up(state, player, row, column) > 0:
        #Up
        i = row + 1
        j = column
        while i < len(state):
            if state[i][j] == opponent:
                state[i][j] = player
                i += 1 
            #No sandwiching player piece:
            elif state[i][j] == ' ': 
                break
            elif state[i][j] == player:
                break
    
    #Check if any points are gained flipping pieces below in the row
    if check_down(state, player, row, column) > 0:
        i = row - 1
        j = column
        while i >= 0:
            if state[i][j] == opponent:
                state[i][j] = player
                i -= 1 
            elif state[i][j] == ' ': 
                break
            elif state[i][j] == player:
                break

    if check_right(state, player, row, column) > 0:
        i = row
        j = column + 1
        while j < len(state[i]):
            if state[i][j] == opponent:
                state[i][j] = player
                j += 1 
            elif state[i][j] == ' ': 
                break
            elif state[i][j] == player:
                break
        
    if check_left(state, player, row, column) > 0:
        i = row
        j = column - 1
        while j >= 0:
            if state[i][j] == opponent:
                state[i][j] = player
                j -= 1 
            elif state[i][j] == ' ': 
                break
            elif state[i][j] == player:
                break


    # Check pieces flipped diagonally #
    if check_diagonal_bottom_right(state, player, row, column) > 0:
        i = row + 1
        j = column + 1
        while i < len(state) and j < len(state[i]):
            if state[i][j] == opponent:
                state[i][j] = player
                i += 1 
                j += 1
            elif state[i][j] == ' ': 
                break
            elif state[i][j] == player:
                break

    #Down Left:
    if check_diagonal_bottom_left(state, player, row, column) > 0:
        i = row + 1
        j = column - 1
        while i < len(state) and j >= 0:
            if state[i][j] == opponent:
                state[i][j] = player
                i += 1 
                j -= 1
            elif state[i][j] == ' ': 
                break
            elif state[i][j] == player:
                break

    #Up Right:
    if check_diagonal_top_right(state, player, row, column) > 0:
        i = row - 1
        j = column + 1
        while i >= 0 and j < len(state[i]):
            if state[i][j] == opponent:
                state[i][j] = player        
                i -= 1 
                j += 1
            elif state[i][j] == ' ': 
                break
            elif state[i][j] == player:
                break

    #Top left
    if check_diagonal_top_left(state, player, row, column) > 0:
        i = row - 1
        j = column - 1
        while i >= 0 and j >= 0:
            if state[i][j] == opponent:
                state[i][j] = player 
                i -= 1 
                j -= 1
            elif state[i][j] == ' ': 
                break
            elif state[i][j] == player:
                break

    return state 

'''
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,

    return (4, 3)
'''
def count_pieces(state):
    #If there's no state there are no pieces
    if not state:
        return (0, 0)
    
    blackpieces = 0
    whitepieces = 0
    
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 'W':
                whitepieces += 1
            if state[i][j] == 'B':
                blackpieces += 1

    return (blackpieces, whitepieces)

'''
Check whether a state is a terminal state. 
'''
def is_terminal_state(state, state_list = None):
    if not state:   #If there is no state, we're in a terminal state
        return True

    for i in range(len(state)):
        for j in range(len(state)):
                #Check if black or white can gain points by moving to an empty position:
                if state[i][j] == ' ':
                    black_value = get_move_value(state, 'B', i, j)
                    if black_value > 0: 
                            return False 

                    white_value = get_move_value(state, 'W', i, j)
                    if white_value > 0:
                            return False 

    #No moves have been found for black or white
    return True 

'''
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player. 
'''
def minimax(state, player, d=0):
    print 'iteration: ' + str(d) + ":", 'player', player
    for i in range(len(state)):
        for j in range(len(state[0])):
            print (state[i][j]), 
        print

    print('------------------')

    if is_terminal_state(state):
        (blackpieces, whitepieces) = count_pieces(state)
        value = blackpieces - whitepieces
        return (value, (-1, -1))
    
    value = 0
    if player == 'B':
        for i in range(len(state)):
            for j in range(len(state[i])):

                if state[i][j] == ' ' and get_move_value(state, 'B', i, j) > 0:  
                    possible_state = execute_move(state, 'B', i, j) 
                    (possible_value, moves) = minimax(possible_state, 'W', d+1) 
                    value = max(possible_value, value)
        return (value, (-1, -1))

    if player == 'W':
        for i in range(len(state)):
            for j in range(len(state[i])):

                if state[i][j] == ' ' and get_move_value(state, 'W', i, j) > 0: 
                    possible_state = execute_move(state, 'W', i, j) 
                    (possible_value, moves) = minimax(possible_state, 'B', d+1) 
                    value = min(possible_value, value)
        
        return (value, (-1, -1))
'''
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
'''
def full_minimax(state, player):
    value = 0
    move_sequence = []
    (value) = minimax(state, player)
    return (value)


'''
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player. 
'''
def minimax_ab(state, player, alpha = -10000000, beta = 10000000):
    value = 0
    row = -1
    column = -1
    # Your implementation goes here 
    return (value, row, column)

'''
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
'''
def full_minimax_ab(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here 
    return (value, move_sequence)



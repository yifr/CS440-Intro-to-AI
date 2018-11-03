from copy import copy, deepcopy #Makes copying 2D arrays into new memory addresses really easy

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
def get_move_value(state, player, row, column):
    flipped = 0
    # Check pieces flipped in a row #
    i = row + 1
    j = column
    #Forwards:
    while i < len(state) and (state[i][j] == 'W' or state[i][j] == 'B'):
        if state[i][j] != player:
            flipped += 1
            i += 1 
        else: 
            break
    i = row - 1
    j = column
    #Backwards:
    while i >= 0 and (state[i][j] == 'W' or state[i][j] == 'B'):
        if state[i][j] != player:
            flipped += 1
            i -= 1 
        else: 
            break
    
    # Check pieces flipped in a column #
    #Up:
    i = row
    j = column + 1
    while j < len(state) and (state[i][j] == 'W' or state[i][j] == 'B'):
        if state[i][j] != player:
            flipped += 1
            j += 1 
        else: 
            break
    #Down:
    i = row
    j = column - 1
    while j >= 0 and (state[i][j] == 'W' or state[i][j] == 'B'):
        if state[i][j] != player:
            flipped += 1
            j -= 1 
        else: 
            break

    # Check pieces flipped diagonally #
    #Up:
    i = row + 1
    j = column + 1
    while (i < len(state) and j < len(state[i])) and (state[i][j] == 'W' or state[i][j] == 'B'):
        if state[i][j] != player:
            flipped += 1
            i += 1 
            j += 1
        else: 
            break
    #Down:
    i = row - 1
    j = column - 1
    while (i >= 0 and j >= 0) and (state[i][j] == 'W' or state[i][j] == 'B'):
        if state[i][j] != player:
            flipped += 1
            i -= 1 
            j -= 1
        else: 
            break

    return flipped


'''
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 
'''
def execute_move(state, player, row, column):
    new_state = deepcopy(state)
    new_state[row][column] = player
    return new_state

'''
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,

    return (4, 3)
'''
def count_pieces(state):
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
    if not state:   #If there is no state, we're in a terminal state?
        return True

    for i in range(len(state)):
        for j in range(len(state)):
                if state[i][j] == '':
                    #Check if black or white have possible moves at this position:
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
def minimax(state, player):
    value = 0
    row = -1
    column = -1
     
    return (value, row, column)

'''
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
'''
def full_minimax(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here 
    return (value, move_sequence)


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



import random
from random import randint
import heapq as hq


''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
        For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
bfs_q = [] #Queue for BFS (append/pop(0))
dfs_stack = [] #Stack for DFS (insert(0)/pop(0))
astar_q = [] #Priority Queue
uc_q = []   #Priority Queue

'''
BFS add to queue 
'''
def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    bfs_q.append((node_id, parent_node_id)) 
    return

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    if bfs_q:
        return False
    else:
        return True

'''
BFS pop from queue
'''
def pop_front_BFS():
    (node_id, parent_node_id) = bfs_q.pop(0)
    return (node_id, parent_node_id)

'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    dfs_stack.append((node_id,parent_node_id))
    return 

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    if dfs_stack:
        return False
    else:
        return True

'''
DFS pop from queue
'''
def pop_front_DFS():
    (node_id, parent_node_id) = dfs_stack.pop()
    return (node_id, parent_node_id)

'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    node = (cost, (node_id,parent_node_id))
    hq.heappush(uc_q,node)
    return 

'''
UC add to queue 
'''
def is_queue_empty_UC():
    if uc_q:
        return False
    else:
        return True

'''
UC pop from queue
'''
def pop_front_UC():
    (node_id, parent_node_id) = (0, 0)
    (node_id, parent_node_id) = hq.heappop(uc_q)[1]
    return (node_id, parent_node_id)

'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    node = (cost, (node_id,parent_node_id))
    hq.heappush(astar_q,node)
    return 
'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    if astar_q:
        return False
    else:
        return True

'''
A* pop from queue
'''
def pop_front_ASTAR():
    (node_id, parent_node_id) = (0, 0)
    (node_id, parent_node_id) = hq.heappop(astar_q)[1]
    return (node_id, parent_node_id)


''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
        For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
    state = []
    c = 0
    while c < n:
        state.append(random.randint(1,n))
        c = c+1
    '''  
    #PrintChessboard
    chessboard = []
    for x in range(n):
        newchessrow = []
        for y in range (n):
            newchessrow.append("[]")
        chessboard.append(newchessrow)
    
    for x in range( len(state)):
        chessboard[state[x]][x] = "Q "
    
    for x in chessboard:
        print x
        print " "
    '''
    return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    #It's all good vertically
    
    #CheckHorizontally
    for x in range(0,len(state)):
        for y in range(0,len(state)):
            if x != y:
                if state[x] == state[y]:
                    number_attacking_pairs = number_attacking_pairs + 1
    
    #CheckDiagonals
    for x in range(0,len(state)):
        for y in range(0,len(state)):
            if x != y:
                if (abs(x - y)) == (abs(state[x]-state[y])):
                    number_attacking_pairs = number_attacking_pairs + 1
    
    number_attacking_pairs = number_attacking_pairs/2
    #print number_attacking_pairs
    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
    
    #state = [4,5,7,5,2,5,1]
    #comp_att_pairs(state)
    
    #My Code Here
    n = len(state)
    
    alternateState = state
    
    options = []
    
    for x in range(0,n):
        alternateState = state
        options = []
        for y in range(1,n+1):
            alternateState[x] = y
            options.append(comp_att_pairs(alternateState))
        a = min(options)
        state[x] = options.index(a) + 1
    
    final_state = state
    
    return final_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    
    x = 1
    state = []
    
    while(x != 0):
        state = get_rand_st(n)
        hill_descending(state,comp_att_pairs)
        x = comp_att_pairs(state)
    
    final_state = state
    
    #print comp_att_pairs(final_state)
    # Your code here
    return final_state

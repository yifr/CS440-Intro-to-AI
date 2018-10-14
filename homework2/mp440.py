import random
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
    rand = []
    c = 0
    while c < n:
        rand.append(random.randint(0,n-1))
        c = c+1
        
    #PrintChessboard
    state = []
    for x in range(n):
        newchessrow = []
        for y in range (n):
            newchessrow.append("[]")
        state.append(newchessrow)
    
    for x in range( len(state)):
        state[rand[x]][x] = "Q"
    
    for x in state:
        print x
        print " "
    
    return state


def queens_attacking(state, x, y):
        pairs = 0
        #Horizontal:
        for i in range(x + 1, len(state)):
            if state[i][y] == 'Q':
                pairs += 1 
        
        #Vertical:
        for j in range(y+1, len(state)):
                if state[x][j] == 'Q':
                        pairs += 1


        #Diagonal right
        i = x + 1
        j = y + 1
        while i < len(state) and j < len(state):
                if state[i][j] == 'Q':
                        pairs += 1

                i += 1
                j += 1

        #Diagonal left
        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0:
                if state[i][j] == 'Q':
                        pairs += 1

                i -= 1
                j -= 1
        
        return pairs

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    attacking_pairs = 0
    
    for x in range(len(state)):
        for y in range(len(state)):
                if state[x][y] and state[x][y] == 'Q':
                        attacking_pairs += queens_attacking(state, x, y)
    print "attacking_pairs: " , attacking_pairs
    return attacking_pairs




'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
    final_state = []
    # Your code here
    return final_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    final_state = []
    # Your code here
    return final_state

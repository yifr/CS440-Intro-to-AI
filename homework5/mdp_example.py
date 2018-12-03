#Policy iteration for a Markov Decision Process
 
#Example here is for a 4x3 board

def main():
    state = [[0 for j in range(4)] for i in range(3)]
    state[0][3] = 1
    state[1][3] = -1
    state[1][1] = "OBSTACLE"
    gamma = 0.9
    initial_reward = -0.05
    policies = policy_iteration(state, gamma, initial_reward)
    for i in range(len(state)):
        for j in range(len(state[i])):
            print state[i][j], policies[i][j], '\t', 
        print

def policy_iteration(state, gamma, initial_reward):
    #Policies can be Up, Down, Left or Right
    #Initialize a 2D array of random policies
    policies = [['U' for j in range(len(state[i]))] for i in range(len(state))]
    unchanged = True
    
    while unchanged:
        #Calculate utilities for the current state and policies
        state = policy_eval(policies, state, gamma, initial_reward)
        for i in range(len(state)):
            for j in range(len(state[i])):
                if accessible(state, i, j):
                    #Find max policy for that state
                    left = calculate_transition(state, i, j, 'L')
                    right = calculate_transition(state, i, j, 'R')
                    up = calculate_transition(state, i, j, 'U')
                    down = calculate_transition(state, i, j, 'D')
                    
                    if left > state[i][j]:
                        state[i][j] = left
                        policies[i][j] = 'L'
                        unchanged = False

                    if right > state[i][j]:
                        state[i][j] = right
                        policies[i][j] = 'R'
                        unchanged = False
                    
                    if up > state[i][j]:
                        state[i][j] = up
                        policies[i][j] = 'U'
                        unchanged = False

                    if down > state[i][j]:
                        state[i][j] = down
                        policies[i][j] = 'D'
                        unchanged = False

    return policies

def policy_eval(policy, state, gamma, reward):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 'OBSTACLE':
                transition = calculate_transition(state, i, j, policy[i][j])
                state[i][j] = reward + gamma * transition  
    
    return state


#Defines our transition model:
#Our transition model has a .9 chance of going in the right direction
#And a .1 chance of going left
#If our movement takes us into an obstacle or off the map, 
#Our transition model keeps us at our current state
def calculate_transition(state, i, j, policy): 
    ans = 0

    if policy == 'U':
        if i - 1 < 0:
            ans += state[i][j] * 0.9
        elif state[i-1][j] == 'OBSTACLE':
            ans += state[i][j] * 0.9
        else:
            ans += state[i-1][j] * 0.9

        if j - 1 < 0:
            ans += state[i][j] * 0.1
        elif state[i][j-1] == 'OBSTACLE':
            ans += state[i][j] * 0.1
        else:
            ans += state[i][j-1] *0.1
        
        return ans
    
    elif policy == 'R':
        if j + 1 >= len(state):
            ans += state[i][j] * 0.9
        elif state[i][j+1] == 'OBSTACLE':
            ans += state[i][j] * 0.9
        else:
            ans += state[i][j+1] * 0.9

        if i - 1 < 0:
            ans += state[i][j] * 0.1
        elif state[i-1][j] == 'OBSTACLE':
            ans += state[i][j] * 0.1
        else:
            ans += state[i-1][j] *0.1
        
        return ans
    
    elif policy == 'D':
        if i + 1 >= len(state):
            ans += state[i][j] * 0.9
        elif state[i+1][j] == 'OBSTACLE':
            ans += state[i][j] * 0.9
        else:
            ans += state[i+1][j] * 0.9

        if j + 1 >=len(state[i]):
            ans += state[i][j] * 0.1
        elif state[i][j+1] == 'OBSTACLE':
            ans += state[i][j] * 0.1
        else:
            ans += state[i][j+1] *0.1
        
        return ans

    elif policy == 'L':
        if j - 1 < 0:
            ans += state[i][j] * 0.9
        elif state[i][j-1] == 'OBSTACLE':
            ans += state[i][j] * 0.9
        else:
            ans += state[i][j-1] * 0.9

        if i + 1 >= len(state):
            ans += state[i][j] * 0.1
        elif state[i+1][j] == 'OBSTACLE':
            ans += state[i][j] * 0.1
        else:
            ans += state[i+1][j] *0.1
        
        return ans
    
    else:
        print("policies are expected to be 'r', 'l', 'u' or 'd'")
        sys.exit(1)

def accessible(state, i, j):
    if state[i][j] != 1 and state[i][j] != -1 and state[i][j] != 'OBSTACLE':
        return True
    else:
        return False

if __name__ == "__main__":
    main()


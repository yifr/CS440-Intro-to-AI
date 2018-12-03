#Policy iteration for a Markov Decision Process
#Example here is for a 4x3 board
import sys

def main():
    state = [[0 for j in range(4)] for i in range(3)]
    state[0][3] = 1
    state[1][3] = -1
    state[1][1] = "OBSTACLE"
    gamma = 0.9
    initial_reward = -0.05
    policies = policy_iteration(state, gamma, initial_reward)
    f = open('mdp_output.txt', 'a')
    for i in range(len(state)):
        for j in range(len(state[i])):
            val = "OBSTACLE"
            if state[i][j] != 'OBSTACLE':
                val = "{:.3f}".format(state[i][j])
            s = str(val) + ' ' +str(policies[i][j]) +'\t\t'
            f.write(s)
        f.write("\n")

        

def policy_iteration(state, gamma, initial_reward):
    #Policies can be Up, Down, Left or Right
    #Initialize a 2D array of random policies
    policies = [['U' for j in range(len(state[i]))] for i in range(len(state))]
    policies[0][3] = 'N/A'
    policies[1][3] = 'N/A'
    policies[1][1] = 'N/A'
    k = 0
    
    while k < 9:
        
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

                    max_policy = left
                    policies[i][j] = 'L' 

                    if down > max_policy:
                        policies[i][j] = 'D'
                        max_policy = down

                    if right > max_policy:
                        policies[i][j] = 'R'
                        max_policy = right 

                    if up > max_policy:
                        policies[i][j] = 'U'
                           
        k += 1
        
    return policies

def policy_eval(policy, state, gamma, reward):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if accessible(state, i, j):
                transition = calculate_transition(state, i, j, policy[i][j])
                state[i][j] = reward + gamma * transition  

    return state


#TRANSITION MODEL OPERATES ACCORDING TO THE FOLLOWING RULES:
#1) 0.9 chance of going in the right direction
#2) 0.1 chance of going 90 degrees to the left of intended direction
#3) If intended movement takes us into an obstacle or off the map, remain in same location
def calculate_transition(state, i, j, policy): 
    ans = 0

    if policy == 'U':
        #Check up
        if i - 1 < 0:
            ans += state[i][j] * 0.9
        elif state[i-1][j] == 'OBSTACLE':
            ans += state[i][j] * 0.9
        else:
            ans += state[i-1][j] * 0.9

        #Check left of up (left)
        if j - 1 < 0:
            ans += state[i][j] * 0.1
        elif state[i][j-1] == 'OBSTACLE':
            ans += state[i][j] * 0.1
        else:
            ans += state[i][j-1] *0.1
        
        return ans
    
    elif policy == 'R':
        
        #Check right:
        if j + 1 >= len(state[i]):
            ans += state[i][j] * 0.9
        elif state[i][j+1] == 'OBSTACLE':
            ans += state[i][j] * 0.9
        else:
            ans += state[i][j+1] * 0.9
        
        #Check left of right (Up)
        if i - 1 < 0:
            ans += state[i][j] * 0.1
        elif state[i-1][j] == 'OBSTACLE':
            ans += state[i][j] * 0.1
        else:
            ans += state[i-1][j] *0.1
        
        return ans
    
    elif policy == 'D':
        #Check down:
        if i + 1 >= len(state):
            ans += state[i][j] * 0.9
        elif state[i+1][j] == 'OBSTACLE':
            ans += state[i][j] * 0.9
        else:
            ans += state[i+1][j] * 0.9

        #Check left of down (right)
        if j + 1 >=len(state[i]):
            ans += state[i][j] * 0.1
        elif state[i][j+1] == 'OBSTACLE':
            ans += state[i][j] * 0.1
        else:
            ans += state[i][j+1] *0.1
        
        return ans

    elif policy == 'L':
        #Check left:
        if j - 1 < 0:
            ans += state[i][j] * 0.9
        elif state[i][j-1] == 'OBSTACLE':
            ans += state[i][j] * 0.9
        else:
            ans += state[i][j-1] * 0.9

        #Check left of left (down)
        if i + 1 >= len(state):
            ans += state[i][j] * 0.1
        elif state[i+1][j] == 'OBSTACLE':
            ans += state[i][j] * 0.1
        else:
            ans += state[i+1][j] *0.1
        
        return ans
    
    else:
        print("policies are expected to be 'R', 'L', 'U' or 'D'")
        sys.exit(1)

def accessible(state, i, j):
    if state[i][j] != 1 and state[i][j] != -1 and state[i][j] != 'OBSTACLE':
        return True
    else:
        return False

if __name__ == "__main__":
    main()


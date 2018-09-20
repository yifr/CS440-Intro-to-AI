

'''
GCD algorithm
'''
def gcd(a, b):
    while(b):
        a, b = b, a % b
        
    return a

'''
Rectangles on a rubik's cube
'''
def rubiks(n):
    return 6 * ((n * (n+1) * n * (n+1)) // 4)


'''
Guessing a number
'''
def guess_unlimited(n, is_this_it):
    # The code here is only for illustrating how is_this_it() may be used 
    guess = n
    while(guess > 0):
        if is_this_it(guess) == True:
            return guess
        else: 
            guess = guess - 1
    
    return -1
        
'''
Guessing a number where you can only make two guesses that are larger
'''
def guess_limited(n, is_this_smaller):
    
    if n == 1:
        return 1
    
    step = n//30
    
    if n <= 1000000:
        step = 1500
        
    if n <= 500000:
        step = 
        
    if n <= 1000:
        step = n//30
        
    if n <= 100:
        step = 20
    
    if n <= 30:
        step = 10
    
    if n <= 20:
        step = 2
    
    if n <= 10:
        step = 1
        
    guess = 1
    stepback = 1
    
    if is_this_smaller(guess) == False:
        return 1
    else:
        guess = 2
        while(guess <= n):
            if is_this_smaller(guess) == False:
                while(stepback < guess):
                    if is_this_smaller(stepback) == False:
                        return stepback
                    else: stepback = stepback + 1
            stepback = guess
            guess = guess + step
        
                
'''
Guessing a number, bonus problem
'''
def guess_limited_plus(n, is_this_smaller):
    #print "hellobuddy"
    mini = 1
    maxi = n
    answer = recursiveBuddyFriendPal(mini, maxi, is_this_smaller)
    return answer

def recursiveBuddyFriendPal(mini, maxi, is_this_smaller):
    
    #print "Range of " + str(mini) + " - " + str(maxi)
    
    if maxi == mini:
        #print "hello my name is the final answer: "
        #print maxi
        return maxi
    
    mid = ((maxi + mini)//2)
    
    if (is_this_smaller(mid)):
        #if this is true, mid is smaller than the number
        #print "larger than " + str(mid)
        mini = mid + 1
        return recursiveBuddyFriendPal(mini, maxi, is_this_smaller)
            
    if (is_this_smaller(mid) == False):
        #if mid is not smaller, mid is either equal or bigger
        #print "smaller than " + str(mid)
        maxi = mid
        return recursiveBuddyFriendPal(mini, maxi, is_this_smaller)
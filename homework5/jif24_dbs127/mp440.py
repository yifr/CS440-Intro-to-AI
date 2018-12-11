import inspect
import sys
import math
import numpy as np 
from numpy import linalg as LA
from numpy import dot
from numpy import transpose 
from numpy.linalg import inv
import matplotlib.pyplot as plt

'''
Raise a "not defined" exception as a reminder 
'''
def _raise_not_defined():
    print "Method not implemented: %s" % inspect.stack()[1][3]
    sys.exit(1)

def kf_predict(A, X_prev, B, U, P_prev, Q):
    predicted_x = A*X_prev + B*U 
    predicted_p = A*P_prev*transpose(A) + Q

    return (predicted_x, predicted_p)

def kf_update(H, P, X, R, z):
    #Kalman gain = PH^T((HPH^T)+R)-1
    kalman_gain = P*transpose(H)*inv(H*P*transpose(H) + R)
    x_updated = X + kalman_gain*(z - H*X)
    p_updated = (np.identity(2) - kalman_gain*H)*P 

    return (x_updated, p_updated)

'''
Kalman 2D
'''
def kalman2d(data, lambd = 1.5):
    estimated = []
    A = np.identity(2)
    B = np.identity(2)
    H = np.identity(2)
    Q = np.matrix([[0.0001, 0.00002], [ 0.00002,0.0001]])    #Covariance matrix for zero mean Gaussian system noise w
    R = np.matrix([[0.01, 0.005], [0.005, 0.02]])            #Covariance matrix for zero mean Gaussian measurement noise 
    
    #Initial estimates
    P_prev = lambd * np.identity(2)
    X = transpose(np.matrix([0, 0]))                #Initial position estimated as first measurement
    estimated.append(X)
    i = 0
    for d in data:
        u = transpose(np.matrix([d[0], d[1]]))
        z = transpose(np.matrix([d[2], d[3]]))
        x = estimated[i]
        P = P_prev
        (x_predicted, p_predicted) = kf_predict(A, x, B, u, P, Q)
        (x_updated, p_updated) = kf_update(H, p_predicted, x_predicted, R, z)
        P_prev = p_updated
        estimated.append(x_updated)
        i += 1

    return estimated

'''
Plotting
'''
def plot(data, output):
    x_data = []
    y_data = []
    x_output = []
    y_output = []
    for d in data:
        x_data.append(d[2])
        y_data.append(d[3])
    for o in output:
        #print o.item(0), o.item(1)
        x_output.append(o.item(0))
        y_output.append(o.item(1))
    
    l1 = plt.plot(x_data, y_data, label="Observations")
    l2 = plt.plot(x_output, y_output, label="Estimated Position")
    plt.setp(l1, color='Blue')
    plt.setp(l2, color='Red')
    plt.legend()
    plt.show()
    return

'''
Kalman 2D 
'''
P0 =  2 * np.identity(2)
last_ghost_sighting = transpose(np.matrix([0, 0]))
error_estimates = [P0]
def kalman2d_shoot(ux, uy, ox, oy, reset=False):
    global P0
    global last_ghost_sighting
    global error_estimates

    if reset == True:
        P0 =  2 * np.identity(2)
        last_ghost_sighting = transpose(np.matrix([0, 0]))
        error_estimates = [P0]

    A = np.identity(2)
    B = np.identity(2)
    H = np.identity(2)
    Q = np.matrix([[0.0001, 0.00002], [ 0.00002,0.0001]])    #Covariance matrix for zero mean Gaussian system noise w
    R = np.matrix([[0.01, 0.05], [0.05, 0.02]])            #Covariance matrix for zero mean Gaussian measurement noise
    u = transpose(np.matrix([ux, uy]))
    z = transpose(np.matrix([ox, oy])) 
    #u = transpose([ux, uy])
    #z = transpose([ox, oy])
    x_prev = last_ghost_sighting
    error_prev = error_estimates.pop()
    (x_pred, p_pred) = kf_predict(A, x_prev, B, u, error_prev, Q)
    (x_updated, p_updated) = kf_update(H, p_pred, x_pred, R, z)
    #Maybe use sum of eigenvalues as shooting metric?
    w, v = LA.eig(p_updated)
    distance_traveled = difference(x_updated, x_prev)
    '''
    print 'Distance calculated from last sighting: ', distance_traveled
    print 'Error covariance: \t', p_updated
    print "Eigenvalue calculations:"
    print w, sum(w), sum(v)
    print
    print
    '''
    if sum(w) < 0.005 and distance_traveled < 5:  #\
    #or (p_updated.item(0) < .0015 and p_updated.item(3) < 0.01 or p_updated.item(1) < .0015 and p_updated.item(2) < 0.015):
    #if sum(w) < 0.005 and distance_traveled < 10:
        return ((x_updated.item(0), x_updated.item(1), True))
    
    last_ghost_sighting = x_updated
    error_estimates.append(p_updated)

    return ((x_updated.item(0), x_updated.item(1), False))


def difference(current, prev):
    return math.sqrt((current[0] - prev[0])**2 + (current[1] - prev[1])**2)
'''
Kalman 2D 
'''
def kalman2d_adv_shoot(ux, uy, ox, oy, reset=False):
    decision = (0, 0, False)
    # Your code starts here 
    # Your code ends here 
    _raise_not_defined()
    return decision



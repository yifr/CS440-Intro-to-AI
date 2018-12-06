import inspect
import sys
import numpy as np 
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
    #Kalman gain = PH^T((HPH^T)+R)^-1
    kalman_gain = P*transpose(H)*inv(H*P*transpose(H) + R)
    x_updated = X + kalman_gain*(z - H*X)
    p_updated = (np.identity(2) - kalman_gain*H)*P 

    return (x_updated, p_updated)


'''
Kalman 2D
'''
def kalman2d(data):
    estimated = []
    A = np.identity(2)
    B = np.identity(2)
    H = np.identity(2)
    Q = np.array([[0.0001, 0.00002], [ 0.00002,0.0001]])    #Covariance matrix for zero mean Gaussian system noise w
    R = np.array([[0.01, 0.005], [0.005, 0.02]])            #Covariance matrix for zero mean Gaussian measurement noise 
    
    #Initial estimates
    P_prev = np.multiply(.5, np.identity(2))
    X = np.array([0, 0])                 #Initial position estimated as first measurement
    estimated.append(X)
    i = 0
    for d in data:
        u = np.array([d[0], d[1]])
        z = np.array([d[2], d[3]])
        x = estimated[i]
        P = P_prev
        (x_predicted, p_predicted) = kf_predict(A, x, B, u, P, Q)
        (x_updated, p_updated) = kf_update(H, p_predicted, x_predicted, R, z)
        x_updated = [x_updated[0][0], x_updated[1][1]]
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
        x_output.append(o[0])
        y_output.append(o[1])
    
    l1 = plt.plot(x_data, y_data, label="Data Received")
    l2 = plt.plot(x_output, y_output, label="Predicted Position")
    plt.setp(l1, color='Blue')
    plt.setp(l2, color='Red')
    plt.legend()
    plt.show()
    return

'''
Kalman 2D 
'''
def kalman2d_shoot(ux, uy, ox, oy, reset=False):
    decision = (0, 0, False)
    # Your code starts here 
    # Your code ends here 
    _raise_not_defined()
    return decision

'''
Kalman 2D 
'''
def kalman2d_adv_shoot(ux, uy, ox, oy, reset=False):
    decision = (0, 0, False)
    # Your code starts here 
    # Your code ends here 
    _raise_not_defined()
    return decision



from collections import Counter
import inspect
import math
import sys


Pf_i = [[0 for j in range(784)] for i in range(10)]         #Probability of feature being True/False for pixel j, label i
P_edges = [[0 for j in range(784)] for i in range(10)]      #Probability of edges being true for pixel j, label i
P_body = [[0 for j in range(784)] for i in range(10)]       #Probability of body being true for pixel j, label i
P_whitespace = [[0 for j in range(784)] for i in range(10)]      #Probability of edges being true for pixel j, label i

quadrant_density =[[0 for j in range(4)] for i in range(10)]
p_label = [0]*10

'''
Raise a "not defined" exception as a reminder 
'''
def _raise_not_defined():
    print "Method not implemented: %s" % inspect.stack()[1][3]
    sys.exit(1)


'''
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit) 
'''
def extract_basic_features(digit_data, width, height):
    features=[]
    for i in range(height):
        for j in range(width):
            if digit_data[i][j] != 0:
                features.append(True)
            else:
                features.append(False)
    return features

'''
Extract advanced features that you will come up with 
'''
def extract_advanced_features(digit_data, width, height):
    features=[]
    #1) Compute quadrant density:
    #quad_size = 196     #14 x 14 squares
    density = [0]*4
    edges = []
    body = []
    whitespace = []
    #compute: whitespace, # count, + count
    for i in range(28):
        for j in range(28):
            if digit_data[i][j] == 2:
                edges.append(True)
                body.append(False)
                whitespace.append(False)
            elif digit_data[i][j] == 1:
                body.append(True)
                edges.append(False)
                whitespace.append(False)
            else:
                body.append(False)
                edges.append(False)
                whitespace.append(True)
            
            '''
            if i < 14 and j < 14 and digit_data[i][j] != 0:
                density[0] += 1
            elif i > 14 and j >= 14 and digit_data[i][j] != 0:
                density[1] += 1
            elif i >= 14 and j < 14 and digit_data[i][j] != 0:
                density[2] += 1
            elif i >= 14 and j >= 14 and digit_data[i][j] != 0:
                density[3] += 1

        for d in density:
            d /= quad_size
            '''     
    features.append(edges)
    features.append(body)
    features.append(whitespace)

    return features

'''
Extract the final features that you would like to use
'''
def extract_final_features(digit_data, width, height):
    features=[]
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here 
    _raise_not_defined()
    return features

'''
Compupte the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training. 
'''
def compute_statistics(data, labels, width, height, feature_extractor, percentage=100.0, k=.0005):
    num_training = int(percentage*len(data)/100)     #Number of examples to use in training
    label_freq = [0]*10                                 #Instances of label y
   
    ###############################
    # BASIC FEATURES
    ###############################
    if feature_extractor == extract_basic_features:
        pix_freq = [[0 for i in range(784)] for j in range(10)]     #Count of features for label i
        #Counting up occurrences of "True" features for label i at pixel j (i in [0,9], j in [0, 783])
        for i in range(num_training):
            label = labels[i]
            label_freq[label] += 1
            features = feature_extractor(data[i], width, height)
            for j in range(len(features)):
                if features[j] == True:
                    pix_freq[label][j] += 1

        #Compute the probability of a given label: P(y)
        for i in range(10):
            p_label[i] = label_freq[i]*1.0 / num_training

        #Calculate probabilities:
        for i in range(len(pix_freq)):
            for j in range(len(pix_freq[i])):
                a = (pix_freq[i][j] + k)/(label_freq[i] + (k))
                Pf_i[i][j] = a
    
    ###############################
    # ADVANCED FEATURES
    ###############################
    elif feature_extractor == extract_advanced_features:
        Ef_i = [[0 for i in range(784)] for j in range(10)]   #Count of edge pixels (features) for label i
        Bf_i = [[0 for i in range(784)] for j in range(10)]   #Count of body pixels (features) for label i
        Wf_i = [[0 for j in range(784)] for i in range(10)]     #Count of quadrant density for label i
        
        #Counting up occurrences of "True" features for label i at pixel j (i in [0,9], j in [0, 783])
        for i in range(num_training):
            label = labels[i]
            label_freq[label] += 1
            features = feature_extractor(data[i], width, height)
            edges = features[0]
            body = features[1]
            whitespace = features[2]
            

            for i in range(len(edges)):
                Ef_i[label][i] += edges[i]
                Bf_i[label][i] += body[i]
                Wf_i[label][i] += whitespace[i]

        #Compute the probability of a given label: P(y)
        for i in range(10):
            p_label[i] = label_freq[i]*1.0 / num_training

        #Calculate probabilities:
        for i in range(len(Ef_i)):
            for j in range(len(Ef_i[i])):
                a = (Ef_i[i][j] + k)/(label_freq[i] + (2*k))
                P_edges[i][j] = a

                b = (Bf_i[i][j] + k)/(label_freq[i] + (2*k))
                P_body[i][j] = b

                c = (Wf_i[i][j] + k)/(label_freq[i] + (2*k))
                P_whitespace[i][j] = c
'''
For the given features for a single digit image, compute the class 
'''
def compute_class(features, feature_extractor=None):
    predicted = {'label': -1, 'prob': -100000000}

    if feature_extractor == extract_basic_features:
        for i in range(10):
            prob = math.log(p_label[i])        #Probability of image belonging to class i
            for j in range(len(features)):
                if features[j] == True:
                    prob += math.log(Pf_i[i][j]) 
                else:
                    prob += math.log(1 - Pf_i[i][j])
            
            if predicted['prob'] < prob:
                predicted['label'] = i
                predicted['prob'] = prob
    
    elif feature_extractor == extract_advanced_features:
        edges = features[0]
        body = features[1]
        #q_density = features[2]

        for i in range(10):
            prob = math.log(p_label[i])        #Probability of image belonging to class i
            for j in range(len(features[0])):
                if edges[j] == True:
                    prob += math.log(P_edges[i][j]) 
                    prob += math.log(1-P_body[i][j]) 
                    prob += math.log(1-P_whitespace[i][j]) 
                elif body[j] == True:
                    prob += math.log(1 - P_edges[i][j])
                    prob += math.log(P_body[i][j]) 
                    prob += math.log(1 - P_whitespace[i][j])
                else:
                    prob += math.log(1 - P_edges[i][j]) 
                    prob += math.log(1 - P_body[i][j]) 
                    prob += math.log(P_whitespace[i][j])

                   
            if predicted['prob'] < prob:
                predicted['label'] = i
                predicted['prob'] = prob
        print predicted['prob']
        #Use density corrections for commonly misclassified numbers
        #9 -> 4
        '''
        if predicted['label'] == 9:
            #9 has a higher average third quadrant density than four
            if abs(quadrant_density[3][2] - q_density[2]) > abs(quadrant_density[8][2] - q_density[2]):
                predicted['label'] = 4
        
        
        if predicted['label'] == 3:
            #9 has a higher average third quadrant density than four
            if abs(quadrant_density[2][2] - q_density[2]) < abs(quadrant_density[7][2] - q_density[2]):
                predicted['label'] = 8
        '''

    return predicted['label']

'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''
def classify(data, width, height, feature_extractor):
    predicted=[]

    for picture in data:
        features = feature_extractor(picture, width, height)
        label = compute_class(features, feature_extractor)
        predicted.append(label)

    return predicted



        
    

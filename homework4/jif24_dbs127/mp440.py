from collections import Counter
import inspect
import math
import sys


Pf_i = [[0 for i in range(784)] for j in range(10)]     #Probability of features for label i
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
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here 
    _raise_not_defined()
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
def compute_statistics(data, label, width, height, feature_extractor, percentage=80.0, k = 0.001):
    num_training = int(percentage*len(data)/100)     #Number of examples to use in training
    label_freq = [0]*10                                 #Instances of label y
    
    #Count up the instances of each training label
    for i in range(num_training):
        label_freq[label[i]] += 1

    #Compute the probability of a given label: P(y)
    for i in range(10):
        p_label[i] = label_freq[i]*1.0 / num_training

    if feature_extractor == extract_basic_features:
        Cf_i = [[0 for i in range(784)] for j in range(10)]     #Count of features for label i
        #Counting up occurrences of "True" features for label i at pixel j (i in [0,9], j in [0, 783])
        for i in range(num_training):
            features = feature_extractor(data[i], width, height)
            for j in range(len(features)):
                if features[j] == True:
                    Cf_i[label[i]][j] += 1
        #Calculate probabilities:
        for i in range(len(Cf_i)):
            for j in range(len(Cf_i[i])):
                a = (Cf_i[i][j] + k)/(label_freq[i] + k)
                Pf_i[i][j] = a
'''
For the given features for a single digit image, compute the class 
'''
def compute_class(features):
    predicted = {'label': -1, 'prob': -100000000}
    for i in range(10):
        prob = math.log(p_label[i])        #Probability of image belonging to class i
        for j in range(len(features)):
            if features[j] == True:
                prob += math.log(Pf_i[i][j])
        
        if predicted['prob'] < prob:
            predicted['label'] = i
            predicted['prob'] = prob

    return predicted['label']

'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''
def classify(data, width, height, feature_extractor):
    predicted=[]

    for picture in data:
        features = feature_extractor(picture, width, height)
        label = compute_class(features)
        predicted.append(label)

    return predicted



        
    

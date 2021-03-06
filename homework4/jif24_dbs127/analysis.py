import time
import sys
import os
import random

DATA_WIDTH=28
DATA_HEIGHT=28
NUMBER_OF_TRAINING_EXAMPLES=5000
NUMBER_OF_VALIDATION_EXAMPLES=1000

ALL_TRAINING_IMAGES=[]
ALL_TRAINING_LABELS=[]
ALL_VALIDATION_IMAGES=[]
ALL_VALIDATION_LABELS=[]

'''
Convert ASC-II pixel into numerical data and vise versa

    - ' ' is converted to 0, which means it's part of the background
    - '#' is converted to 1, part of the image interior
    - '+' is converted to 2, part of the image exterios (i.e., edges)
    
'''
def _pixel_to_value(character):
    if(character == ' '):
        return 0
    elif(character == '#'):
        return 1
    elif(character == '+'):
        return 2    

def _value_to_pixel(value):
    if(value == 0):
        return ' '
    elif(value == 1):
        return '#'
    elif(value == 2):
        return '+'    

'''
Function for loading data and label files
'''
def _load_data_file(filename, n, width, height):
    fin = [l[:-1] for l in open(filename).readlines()]
    fin.reverse()
    items = []
    for i in range(n):
        data = []
        for j in range(height):
            row = map(_pixel_to_value, list(fin.pop()))
            data.append(row)
        items.append(data)
    return items
        
def _load_label_file(filename, n):
    fin = [l[:-1] for l in open(filename).readlines()]
    labels = []
    for i in range(n):
        labels.append(int(fin[i]))
    return labels

'''
Helper function for prting an image
'''
def _print_digit_image(data):
    for row in range(len(data)):
        print ''.join(map(_value_to_pixel, data[row]))

'''
Loading all data into a list of "pixels" with some edge information
'''
def _load_all_data():
    
    global t_image 
    global t_label 
    global ALL_VALIDATION_IMAGES
    global ALL_VALIDATION_LABELS

    t_image = _load_data_file("digitdata/trainingimages",
        NUMBER_OF_TRAINING_EXAMPLES, DATA_WIDTH, DATA_HEIGHT)
    t_label = _load_label_file("digitdata/traininglabels",
        NUMBER_OF_TRAINING_EXAMPLES)

    ALL_VALIDATION_IMAGES = _load_data_file("digitdata/validationimages",
        NUMBER_OF_VALIDATION_EXAMPLES, DATA_WIDTH, DATA_HEIGHT)
    ALL_VALIDATION_LABELS = _load_label_file("digitdata/validationlabels",
        NUMBER_OF_VALIDATION_EXAMPLES)


def analyze():
    label_count = [0]*10
    whitespace = [0]*10
    edges = [0]*10
    body = [0]*10 

    for i in range(len(t_image)):
        label_count[t_label[i]] += 1
        for j in range(len(t_image[i])):
            for k in range(len(t_image[j])):
                if t_image[i][j][k] == 1:
                    body[t_label[i]] += 1
                elif t_image[i][j][k] == 2:
                    edges[t_label[i]] += 1
                else:
                    whitespace[t_label[i]] += 1


    for i in range(10):
        whitespace[i] = whitespace[i] / label_count[i] 
        body[i] = body[i] / label_count[i]
        edges[i] = edges[i] / label_count[i]
    
    f = open('stats.txt', 'a')
    for i in range(10):
        s = "Number: "+ str(i) + '\n'
        s += "Whitespace: " + str(whitespace[i]) + '\n'
        s += str(body[i])+ ' #s\n'
        s += str(edges[i])+ " +s\n\n"
                
        f.write(s)

def edges_vs_body():
    for i in range(len(t_image)):
        pic = t_image[i]
        label = t_label[i]
        print "Body: "
        for j in range(28):
            for k in range(1, 28):
                if pic[j][k] == 1:
                    print '#',
                else:
                    print ' ',
            print "\n"
        
        print "Edges: "
        for j in range(28):
            for k in range(1, 28):
                if pic[j][k] == 2:
                    print '+',
                else:
                    print ' ',
            print "\n"


def avg_horizontal_lines():
    horizontal_width = [0]*10
    line_count = [0]*10
    
    for i in range(len(t_image)):
        pic = t_image[i]
        label = t_label[i]

        for j in range(28):
            width = 0
            for k in range(1, 28):
                if pic[j][k] != 0:
                    width += 1
                elif pic[j][k-1] != 0 and pic[j][k-2] != 0:
                    if width > horizontal_width[label] / line_count[label]:
                        horizontal_width[label] += width
                        line_count[label] += 1       
            line_count[label] += 1

    print 'Label', 'Total pixels', 'Number of Horizontal lines'
    print '-----','----------','  -----------------------'
    for i in range(len(horizontal_width)):
        print str(i)+')', '\t', horizontal_width[i], '\t\t',line_count[i]
        horizontal_width[i] /= line_count[i]
    print horizontal_width

_load_all_data()
#analyze()
edges_vs_body()
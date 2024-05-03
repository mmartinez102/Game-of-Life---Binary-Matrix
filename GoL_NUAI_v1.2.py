#Game of Life - Neuromorphic AI Algorithm Application (v1.1)
#by Michael Martinez
#This program will be the first start of applying the Game of Life (GOL) as a neuromorphic AI algorithm to control a basic robot. The robot
#will have a basic ultrasonic sensor for vision, a servo motor to moving this ultrasonic sensor, & four-wheel drive
#(4x modes - forward/backward drive for both right and left side wheels). The idea is to test whether the patterns that develop in the GOL
#can be used as a method of storing information over past stimuli but in an ever changing manner. A basic matrix will be created for this
#algorithm. The hope is that the robot will learn to perform obstacle avoidance without having been programmed to do so.

#First import numpy
import numpy as np

#Set the dimenstions of the matrix under study A = [M,N]
M = 29 #Max number of rows
N = 29 #Max number of columns

#We will run a forever while loop
#K = 500 #Number of iterations to run the code

#Generate a random binary matrix
pre_pad_A = np.random.randint(2, size=(M,N))

#Need to make a copy of pre_pad_A to save the next generation of values from Gen A to Gen B.
from copy import copy, deepcopy
pre_pad_B = deepcopy(pre_pad_A)


#print("Pre padded A is: ")
#print(pre_pad_A)
#print("Pre padded B is: ")
#print(pre_pad_B)


A = np.pad(pre_pad_A, pad_width=1)
#print(A)
B = np.pad(pre_pad_B, pad_width=1)
#print(B)




#We must perform a while loop here that runs the program
print("We now run the 3x3 filter to find the number of 1's and 0's.")
k = 1

#Utilize a forever loop
#while k < K:
while True:
    #Now one must take a 3x3 filter across each index in the array (with padding)
    #and apply the basic GoL rules. First we find the number of 1's and 0's for each index.
    for i in range(1,M+1):
        for j in range(1,N+1):
            neighbor_states = [A[i-1,j-1], A[i-1,j], A[i-1,j+1], A[i,j-1], A[i,j+1], A[i+1,j-1], A[i+1,j], A[i+1,j+1]]
            zeros = neighbor_states.count(0)
            ones = neighbor_states.count(1)
            #Below are the conditions
            #Death
            if A[i,j] == 1: 
                #Overpopulation
                if ones > 3:
                    B[i,j] = 0
                    continue
                #Loneliness
                if ones < 2:
                    B[i,j] = 0
                    continue
            else:
            #Birth
                if A[i,j] == 0: 
                    if ones == 3:
                        B[i,j] = 1
                        continue
            
    print("In iteration ")
    print(k)
    print("The original matrix is: ")
    print(A)
    print("The transformed matrix is: ")
    print(B)
    
    #Make the next iteration of matrix A equal to the current B matrix (which holds all the next states)
    from copy import copy, deepcopy
    A = deepcopy(B)

    k += 1   
        
    #We continue in this GoL_NUAI_v1.2.py file to allow for the input of sensor values and output of motor values over the serial network
    
    
    
        
        
        












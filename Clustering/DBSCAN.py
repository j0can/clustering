import clustering_functions as CL
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math

#TODO: Write your full name.
name = 'Your Name'
#ENDTODO

# TODO: Selest one of the two problems by commenting the rest of the lines using # before each line
#_, problem, database = CL.uploadDataBase1() # Function that upload the database 1
_, problem, database = CL.uploadDataBase2() # Function that upload the database 2
# ENDTODO
#print (len(examples))

# Important parameters used in DBSCAN
# TODO: Change these parameters so Genetic algorithms works better.
R = 10 # Radius to check neighbouring points. Positive number.
minPoints = 2 # Minimum number of points within the radius to be consider a cluster. Positive integer.
# ENDTODO

CL.DBSCAN_checkErrorsInParameters(R, minPoints) # Function that will double-check if your parameters are in the correct range.

nonVisited, visited, actualCluster, visitedColor, action, nextToVisit = CL.DBSCAN_initialize(database) # Function that will initialize the algorithm

CL.DBSCAN_visualize(nonVisited, visited, visitedColor, [], [], R, name) # Function to visualize the data and how the algorithm works

while True: # Main loop of the program that will run forever

    # If there are not next to visit datapoints, one is randomly selected.
    if nextToVisit == []:
        index = random.randint(0, len(nonVisited)-1)
        nextToVisit.append(index)
        action = False

    neighbours = CL.DBSCAN_checkNeighbours(nonVisited, nextToVisit, R) # Function that will find the neighbours of the recently visited datapoints

    nextToVisit, visited, nonVisited, visitedColor, aura, auraColor, actualCluster, action = CL.DBSCAN_updateVisited(nextToVisit, visited, nonVisited, neighbours, action, actualCluster, visitedColor, minPoints) # Function that will update the visited nodes

    CL.DBSCAN_visualize(nonVisited, visited, visitedColor, aura, auraColor, R, name) # Function to visualize the data and how the algorithm works

    if len(nonVisited) == 0: # If all the datapoints have been visited
        break # If the condition in the line above, break will force the while loop to stop

CL.DBSCAN_saveResults(nonVisited, visited, visitedColor, name, problem) # Function that save the results of the algorithm

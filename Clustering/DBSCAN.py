import clustering_functions as CL
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import math


name = 'Your Name'


_, problem, database = CL.uploadDataBase2()



R = 10
minPoints = 2


CL.DBSCAN_checkErrorsInParameters(R, minPoints)

nonVisited, visited, actualCluster, visitedColor, action, nextToVisit = CL.DBSCAN_initialize(database)

CL.DBSCAN_visualize(nonVisited, visited, visitedColor, [], [], R, name)

while True:

    
    if nextToVisit == []:
        index = random.randint(0, len(nonVisited)-1)
        nextToVisit.append(index)
        action = False

    neighbours = CL.DBSCAN_checkNeighbours(nonVisited, nextToVisit, R)

    nextToVisit, visited, nonVisited, visitedColor, aura, auraColor, actualCluster, action = CL.DBSCAN_updateVisited(nextToVisit, visited, nonVisited, neighbours, action, actualCluster, visitedColor, minPoints) # Function that will update the visited nodes

    CL.DBSCAN_visualize(nonVisited, visited, visitedColor, aura, auraColor, R, name)

    if len(nonVisited) == 0:
        break

CL.DBSCAN_saveResults(nonVisited, visited, visitedColor, name, problem)

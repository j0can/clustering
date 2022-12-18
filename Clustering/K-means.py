import clustering_functions as CL

#TODO: Write your full name.
name = 'Your Name'
#ENDTODO

# TODO: Selest one of the two problems by commenting the rest of the lines using # before each line
df, problem, _ = CL.uploadDataBase1() #  Function that upload the database 1
#df, problem, _ = CL.uploadDataBase2() #  Function that upload the database 2
# ENDTODO

# Important parameter used in K-means
# TODO: Define the number of clusterings.
k = 1 # The number should be possitive and less than 8. Integer.
#ENDTODO

CL.K_means_checkErrorsInParameters(k) # Function that will double-check if your parameters are in the correct range.

df, centroids = CL.K_means_initialize(df, k) # Function that will initialize the algorithm

CL.K_means_visualize(df, centroids, name) # Function to visualize the data and how the algorithm works

df = CL.K_means_assignment(df, centroids) # Function that assigns each data point to a centroid

CL.K_means_visualize(df, centroids, name) # Function to visualize the data and how the algorithm works

while True: # Main loop of the program that will run forever
    closest_centroids = df['closest'].copy(deep=True) # Save a copy of the current position of the centroids

    centroids = CL.K_means_update(df, centroids)  # Function that update the centroids position

    df = CL.K_means_assignment(df, centroids)  # Function that assigns each data point to a centroid

    if closest_centroids.equals(df['closest']): # If the centroids did not change
        break # If the condition in the line above, break will force the while loop to stop

        CL.K_means_visualize(df, centroids, name) # Function to visualize the data and how the algorithm works

CL.K_means_saveResults(df, centroids, name, problem) # Function that save the results of the algorithm

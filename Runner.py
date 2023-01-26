import sys
import os
import pandas as pd

from Helpers import helper
from GridCollection import Grid1

from Algorithms import isValid
from Algorithms import dfs

from copy import deepcopy

sys.setrecursionlimit(10**5)

# Defining the current working directory 
cwd = sys.path[0]

# Path to a foldercontaining the csv files
csvStatesPath = os.path.join(cwd, '..', 'csvStates')

# CSV File Name
csvFileName = 'State175_13.csv'

# This Contains the final path to the csv file
csvFilePath = os.path.join(csvStatesPath, csvFileName)

# Online Link can also be provided
# csvFilePath = ''

# Reading the csv file
initialState = pd.read_csv(csvFilePath, header=None, dtype=int).to_numpy()

# Final File Path 
fPath = helper.createFolder(cwd, initialState)

# Creating the grid object
grid = Grid1(npgrid = initialState, fPath = fPath)

# Set the Starting Location
startingLocation = (0, 8)

# Set the ending Location
endingLocation = (173, 5)

if not isValid(grid.getShape(), startingLocation):
  raise Exception("Starting Location Outside the grid")
if not isValid(grid.getShape(), endingLocation):
  raise Exception("Ending Location Outside the grid")

# Setting the starting Location
grid.set(startingLocation, 2)
grid.set(endingLocation, 3)

dfsObject = dfs(deepcopy(grid), startingLocation)

assert endingLocation == dfsObject.start()
print("Found the ending Location")









# A Function to check if the point of interest is inside or outside the grid
def isValid(shape, coordinates) -> bool:
    rows, cols = shape
    i, j = coordinates
    return (i >= 0) and (i < rows) and (j >= 0) and (j < cols)

class algorithms:
    def dfs(grid, coordinates):
        # If the coordinates are out of maze then return false
        if not algorithms.isValid(grid.getShape(), coordinates): return False

        # Get the grid state
        gridState = grid.get(coordinates)

        # Check if the coordinates are end point
        if gridState == 3:
            print(coordinates)
            return True

        # if the coordinates are representing a wall then return False
        if gridState == 1: return False

        # if the coordinates are previously visited then return False
        if gridState == 4: return False

        # Now make the element at specified coordinates visited
        grid.set(coordinates, 4)

        # Traverse the grid in 4 directions
        
        #left 
        if algorithms.dfs(grid, (coordinates[0] + 0, coordinates[1] + 1)): return True
        # right
        if algorithms.dfs(grid, (coordinates[0] + 0, coordinates[1] - 1)): return True
        # up
        if algorithms.dfs(grid, (coordinates[0] + 1, coordinates[1] + 0)): return True
        # down
        if algorithms.dfs(grid, (coordinates[0] - 1, coordinates[1] + 0)): return True

        return False


class dfs:
    def __init__(self, grid, startCoordinates):
        self.__grid = grid
        self.__startCoordinates = startCoordinates
        self.__endCoordinates = None
    
    def __recur(self, coordinates):
        # If the coordinates are out of maze then return false
        if not isValid(self.__grid.getShape(), coordinates): return False

        # Get the self.__grid state
        gridState = self.__grid.get(coordinates)

        # Check if the coordinates are end point
        if gridState == 3:
            self.__endCoordinates = coordinates
            return True

        # if the coordinates are representing a wall then return False
        if gridState == 1: return False

        # if the coordinates are previously visited then return False
        if gridState == 4: return False

        # Now make the element at specified coordinates visited
        self.__grid.set(coordinates, 4)

        # Traverse the grid in 4 directions
        
        #left 
        if self.__recur((coordinates[0] + 0, coordinates[1] + 1)): return True

        # right
        if self.__recur((coordinates[0] + 0, coordinates[1] - 1)): return True
        
        # up
        if self.__recur((coordinates[0] + 1, coordinates[1] + 0)): return True
        
        # down
        if self.__recur((coordinates[0] - 1, coordinates[1] + 0)): return True

        return False

    def start(self):
        self.__recur(self.__startCoordinates)
        return self.__endCoordinates

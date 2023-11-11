'''
Author: Cole Bartley
KUID: 3050138
Date: 10/4/22
Lab: lab05
Last modified: 10/17/22
Purpose: This file holds the executive class, which does most of the file reading and printing
'''
from mazewalking import MazeWalker
#initialization of the executive object with the file name as its member variable
class Executive:
    def __init__(self, file_name):
        self.file_name = file_name

#reads into the file, gets the total and starting rows and columns, sets the maze into a list of lists, creates the visited maze by taking the maze
#and making the walls a 2, creates the mazewalking object and passes in corresponding parameters, finds the sewer locations of that particular maze, 
#then walks through the maze, and finally prints the final maze with the blob and all
    def run(self):
        ofile = open(self.file_name)
        num = 0
        maze = []
        visited = []
        for line in ofile:
            if num < 1:
                total = line.split(" ")
                totalrows = int(total[0])
                totalcolumns = int(total[1])
                num = num + 1
            elif num < 2:
                starting = line.split(" ")
                startingrow = int(starting[0])
                startingcol = int(starting[1])
                num = num + 1
            else:
                maze.append(list(line.strip()))
        for line in maze:
            visited.append([0 if x != "#" else 2 for x in line])
        if totalrows < 1:
            raise Exception("The total rows have to be greater than 1")
        if totalcolumns < 1:
            raise Exception("The total columns have to be greater than 1")
        if startingrow > totalrows or startingcol > totalcolumns:
            raise Exception("The starting position is invalid")
        themaze = MazeWalker(maze, visited, totalrows, totalcolumns)
        themaze.findsewerslocation()
        themaze.walk(startingrow, startingcol)
        for line in themaze.maze:
            print("".join(line))
        print("Total eaten: " + str(themaze.eaten))

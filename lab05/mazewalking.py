'''
Author: Cole Bartley
KUID: 3050138
Date: 10/4/22
Lab: lab05
Last modified: 10/17/22
Purpose: This file holds the Mazewalker class, in which it holds all the methods that are needed to spread the blob through the maze
'''
class MazeWalker:
#creation of the mazewalker object
    def __init__(self, maze, visited, totalrows, totalcol):
        self.maze = maze
        self.visited = visited
        self.totalrows = totalrows
        self.totalcol = totalcol
        self.eaten = 0
        self.sewerslocation = []
        
#marks the maze by changing it to B and marks the visited by changing it to 1. Doesn't change to B if that part of the maze is a sewer (@). 
#if the spot was P, then it adds 1 to the total eaten.
    def mark(self, row, col):
        if self.maze[row][col] == "P":
            self.eaten = self.eaten + 1
            self.maze[row][col] = "B"
            self.visited[row][col] = 1
        elif self.maze[row][col] == "@":
            self.maze[row][col] = "@"
        else:
            self.maze[row][col] = "B"
            self.visited[row][col] = 1
    
#first checks if the spot is out of bounds. If it is, it returns False. Then checks the visited maze by seeing of it is a 2 or a 1
#(a 2 is a wall and a 1 is a spot already visited). If that is the case, it returns false. Otherwise it returns True
    def is_valid_move(self, row, col):
        if row < 0 or col < 0 or row >= self.totalrows or col >= self.totalcol:
            return False
        elif self.visited[row][col] == 2 or self.visited[row][col] == 1:
            return False
        else:
            return True
    
#Main portion. This function walks through the maze by checking if a move is valid in the clockwise direction, then takes the step by using recusion
    def walk(self, row, col):
        self.mark(row, col)        
        
        if self.is_valid_move(row-1, col):
            self.walk(row-1, col)
            
        if self.is_valid_move(row, col+1):
            self.walk(row, col+1)
        
        if self.is_valid_move(row+1, col):
            self.walk(row+1, col)
        
        if self.is_valid_move(row, col-1):
            self.walk(row, col-1)

        if self.maze[row][col] == "@":
            if (row, col) in self.sewerslocation:
                self.sewerslocation.remove((row, col))
            for alist in self.sewerslocation:
                self.walk(alist[0], alist[1])

            
#finds the sewers in the maze, then appends the coordinantes to a list
    def findsewerslocation(self):
        for i in range(self.totalrows):
            for j in range(self.totalcol):
                if self.maze[i][j] == "@":
                    self.sewerslocation.append((i, j))


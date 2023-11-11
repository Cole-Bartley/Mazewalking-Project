'''
Author: Cole Bartley
KUID: 3050138
Date: 10/4/22
Lab: lab05
Last modified: 10/17/22
Purpose: This gets the file name from the user and hands control over to the executive class
'''
from executive import Executive

#gets the file, then hands control to the executive class
def main():
  file_name = input("Enter the name of the input file: ")
  my_exec = Executive(file_name)
  my_exec.run()

if __name__ == "__main__":
  main()
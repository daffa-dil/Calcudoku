#Calcudoku Main Function
#
#Names: Brian Beggs and Rohith Dara
#Instructor: S. Einakian
#Section: 01

from calcudoku_funcs import *
import sys

'''
Pseudocode for main function:
Initialize all cells in a 5x5 grid to 0
Input the cage values that includes the sum of each case and the location of each cage
Run through the cells 1 at a time
If the cell value is less than 5, increment the cell value by 1
If the current cell value after incrementing by 1 is identical to any other values in the row or column that it is in, increment it by 1 again (0's are exempt)
Repeat the previous step until the cell value is unique in its column AND row
If the cell value is unique in its row and column AND the cage that it is in is either less than or equal to the indicated sum, move to the next cell
If the above condition is not met, check if the cell value is equal to 5 or is not unique/<= cage sum --> set the cell value to 0 and move back to the previous cell
Continue checking the validity of the row, column, and cage sum until you can move on to the next cell
Print the final grid without the list format and have a space between each number
'''

#This function runs through Calcudoku and prints the solution in a 5x5 grid
#->
def main():
   cages = inputter()

   grid = []
   for x in range (5):
      grid.append([0, 0, 0, 0, 0])

   cell = 0
   while cell < 25:
      if grid[cell//5][cell%5] < 5:
         grid[cell//5][cell%5] += 1
         if validate_all(grid, cages) == True:
            cell += 1
      elif grid[cell//5][cell%5] == 5 or validate_all(grid, cages) == False:
         grid[cell//5][cell%5] = 0
         cell -= 1

   for nested in grid:
      print(*nested, sep = ' ')

if __name__ == '__main__':
   main()


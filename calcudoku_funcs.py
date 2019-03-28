#Calcudoku Functions
#
#Names: Brian Beggs and Rohith Dara
#Instructor: S. Einakian
#Section: 01

import sys

'''
Pseudocode for transpose function:
Create a 1D list where each subset of the list is based on the indexes of the previous nested list (all index 0's go together, all index 1's go together, etc.)
Append every list of 5 numbers (representing each column) into a 2D list
'''
#This function puts the nested list where each sublist is a row into a nested list where each sublist is a column
#list->list
def transpose(grid):
   t_grid = []
   t_grid1 = []
   for i in range(5):
      for x in range(5):
         t_grid.append(grid[x][i])
   for i in range(0, 25, 5):
      t_grid1.append(t_grid[i:i+5])
   return t_grid1

'''
Pseudocode for validate rows function:
Set 'val' equal to the value of the first index of the sublist
Run through every number in the sublist
If it is 0, move to the next value as 0's are exempt
Skip the sublist value if it matches the same index as 'val'
If the sublist value is the same as 'val', return False
If none of the sublist values match 'val', increment the index of 'val' by 1
Repeat the above steps for every index of the sublist
If none of the values in the sublist are equal (except for 0's), return True
'''

#This function checks if every value in each row are different (except for 0)
#list->bool
def validate_rows(grid):
   for i in grid:
      w = 0
      while w < 5:
         val = i[w]
         for x in i:
            if x == 0:
               continue
            if i.index(x) == w:
               continue
            elif x == val:
               return False
         w += 1
   return True

'''
Validate_rows1 was just another way of validating using the sort function, but we didn't end up using it

def validate_rows1(grid):
   for i in grid:
      sub_grid = []
      for x in i:
         if x == 0:
            continue
         else:
            sub_grid.append(x)
      sub_grid.sort()
      val = -1
      for z in sub_grid:
         if val == z:
            return False
         val = z   
   return True
'''

'''
Pseudocode for validate columns function:
Transpose the grid so that it checks the columns instead of the rows
Set 'val' equal to the value of the first index of the sublist
Run through every number in the sublist
If it is 0, move to the next value as 0's are exempt
Skip the sublist value if it matches the same index as 'val'
If the sublist value is the same as 'val', return False
If none of the sublist values match 'val', increment the index of 'val' by 1
Repeat the above steps for every index of the sublist
If none of the values in the sublist are equal (except for 0's), return True
'''

#This function checks if every value in each column are different (except 0)
#list->bool
def validate_cols(grid):
   t_grid = transpose(grid)
   for i in t_grid:
      w = 0
      while w < 5:
         val = i[w]
         for x in i:
            if x == 0:
               continue
            if i.index(x) == w:
               continue
            elif x == val:
               return False
         w += 1
   return True

'''
Pseudocode for validate cages:
For every cage respresented by a sub list, set the sum of the cage equal to 'sum'
For each value in the sub list that is not the sum, find the corresponding value in the grid
Add each value from the grid to another variable called 'sum1'
If the given sum of the cage ('sum') is less than the sum of the cage from the grid ('sum1'), return False
Otherwise return True
'''

#This function checks if each cage sum is less than or equal to the indicated sum per cage
#list,list->bool
def validate_cages(grid, cages):
   for i in range(1, cages[0][0]+1):
      sum1 = 0
      sum = cages[i][0]
      for z in range(1,len(cages[i])):
         sum1 += grid[cages[i][z]//5][cages[i][z]-(5*(cages[i][z]//5))]
      if sum < sum1:
         return False
   return True

         

'''
Pseudocode for validate all
If all the validate functions return True, return True
If any of the validate funcitons return False, return False
'''

#This function checks if all the previous validations are true
#list,list->bool
def validate_all(grid, cages):
   rows = validate_rows(grid)
   cols = validate_cols(grid)
   cages = validate_cages(grid, cages)
   if rows == True and cols == True and cages == True:
      return True
   else:
      return False

'''
Pseudocode for inputter:
Set an empty list equal to temp
Set an empty list equal to cages
Set a variable named grid_input to readlines of the input
For each line of the input, split it into a sublist
Append each sublist to the temp cage
Change each value of each sublist into an integer value
Append each sublist to the cages list
Return the cages list
'''

#This function inputs the file and puts the values in a nested list to create the cages
#->list
def inputter():
   temp = []
   cages = []
   grid_input = sys.stdin.readlines()
   for eachline in grid_input:
      line = eachline.split()
      temp.append(line)
   for w in temp:
      temp2 = [int(t) for t in w]
      cages.append(temp2)
   return cages






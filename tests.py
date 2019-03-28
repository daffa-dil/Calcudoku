#Calcudoku Test Cases
#
#Names: Brian Beggs and Rohith Dara
#Instructor: S. Einakian
#Section: 01


import unittest
from calcudoku_funcs import *


class TestCases(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_transpose(self):
      grid = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
      self.assertListAlmostEqual(transpose(grid), [[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24],[5,10,15,20,25]])
      grid = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
      self.assertListAlmostEqual(transpose(grid), [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]])
      grid = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]
      self.assertListAlmostEqual(transpose(grid), [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]])

   def test_validate_rows(self):
   	grid = [[0,0,0,0,0],[0,0,0,0,0]]
   	self.assertEqual(validate_rows(grid), True)
   	grid = [[5,3,4,1,2],[4,2,3,1,5]]
   	self.assertEqual(validate_rows(grid), True)
   	grid = [[1,2,3,4,1],[1,2,3,4,5]]
   	self.assertEqual(validate_rows(grid), False)

   def test_validate_cols(self):
   	grid = [[1,2,3,4,5],[2,3,4,5,1],[0,0,0,0,0],[6,7,8,9,10],[4,4,2,1,2]]
   	self.assertEqual(validate_cols(grid), True)
   	grid = [[1,2,3,4,5],[2,3,4,5,5],[4,5,7,8,9],[10,11,12,13,14],[12,13,14,15,16]]
   	self.assertEqual(validate_cols(grid), False)
   	grid = [[1,2,2,2,5],[2,3,0,0,1],[4,4,4,4,4],[5,5,5,5,0],[3,6,7,8,9]]
   	self.assertEqual(validate_cols(grid), True)

   def test_validate_cages(self):
      grid = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,5],[16,17,18,19,20],[21,22,23,24,25]]
      cages = [[5],[55,0,5,10,15,20],[60,1,6,11,16,21],[65,2,7,12,17,22],[70,3,8,13,18,23],[75,4,9,14,19,24]]
      self.assertEqual(validate_cages(grid, cages), True)
      grid = [[1,2,3,4,5],[6,7,8,9,10]]
      cages = [[1],[55,0,1,2,3,4,5,6,7,8,9]]
      self.assertEqual(validate_cages(grid, cages), True)
      grid = [[1,2,3,4,5],[1,2,3,4,5]]
      cages = [[2],[10,0,1,2,3,5,6],[10,4,7,8,9]]
      self.assertEqual(validate_cages(grid, cages), False)

   def test_validate_all(self):
      grid = [[0,0,0,0,0],[5, 1, 3, 4, 2],[2, 4, 1, 5, 3],[1, 2, 4, 3, 5],[4, 3, 5, 2, 1]]
      cages = [[9],[9, 0, 5, 6],[7, 1, 2],[10, 3, 8, 13],[14, 4, 9, 14, 19],[3, 7],[8, 10, 11, 16],[13, 12, 17, 21, 22],[5, 15, 20],[6, 18, 23, 24]]
      self.assertEqual(validate_all(grid, cages), True)
      grid = [[3, 5, 2, 1, 4],[5, 1, 3, 4, 2],[2, 4, 1, 5, 3],[1, 2, 4, 3, 5],[4, 3, 5, 2, 1]]
      cages = [[9],[8, 0, 5, 6],[7, 1, 2],[10, 3, 8, 13],[14, 4, 9, 14, 19],[3, 7],[8, 10, 11, 16],[13, 12, 17, 21, 22],[5, 15, 20],[6, 18, 23, 24]]
      self.assertEqual(validate_all(grid, cages), False)
      grid = [[3, 5, 2, 1, 4],[5, 1, 3, 4, 2],[2, 10, 1, 5, 3],[1, 2, 4, 3, 5],[4, 3, 5, 2, 1]]
      cages = [[9],[9, 0, 5, 6],[7, 1, 2],[10, 3, 8, 13],[14, 4, 9, 14, 19],[3, 7],[8, 10, 11, 16],[13, 12, 17, 21, 22],[5, 15, 20],[6, 18, 23, 24]]
      self.assertEqual(validate_all(grid, cages), False)

   '''No test cases for inputter because there is no parameter'''

if __name__=='__main__':
   unittest.main()




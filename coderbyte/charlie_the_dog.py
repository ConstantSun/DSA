#  For this challenge you will be helping a dog collect all the food in a grid.
# 
# have the function CharlietheDog(strArr) read the array of strings stored in strArr which will be a 4x4 matrix 
# of the characters 'C', 'H', 'F', 'O', 
# where C represents Charlie the dog, 
# H represents its home, 
# F represents dog food, 
# and O represents and empty space in the grid. 
# Your goal is to figure out the least amount of moves required to get Charlie to grab each piece of food 
# in the grid by moving up, down, left, or right, and then make it home right after. 
# Charlie cannot move onto the home before all pieces of food have been collected. 
# For example: 
# if strArr is 
# ["FOOF", 
#  "OCOO", 
#  "OOOH", 
#  "FOOO"], then this looks like the following grid:

# For the input above, the least amount of steps where the dog can reach each piece of food, 
# and then return home is 11 steps, so your program should return the number 11. 
# 
# The grid will always contain between 1 and 8 pieces of food.


# bruteforce all possible moves 
# food: 0,1,2,3,4,5
# -> 013245, 014235,... all permutations

from itertools import permutations

class Solution:
    def leastAmountOfSteps(self, strArr: list):
        food_loc = []
        hi, hj = 0,0
        ci, cj = 0,0
        for i in range(4):
            for j in range(4):
                match strArr[i][j]:
                    case 'H':
                        hi, hj = i,j
                    case 'F':
                        food_loc.append([i, j])
                    case 'C':
                        ci, cj = i, j
            
        def get_steps(i:int,j:int, k:int,l:int, is_to_house=False):
            ans = abs(i-k) + abs(j-l)
            if not is_to_house:
                if (i==k==hi and  (l > hj > j or l < hj < j)) or (j==l==hj and (i > hi > k or i < hi < k )):
                    ans += 2
            return ans
        
        no_food = len(food_loc)
        food_permutations = list(permutations(range(no_food)))
        smallest_steps = 1e6
        for path in food_permutations:
            total = 0 # path e.g: 32041
            total += get_steps(ci, cj, food_loc[path[0]][0], food_loc[path[0]][1])         # first steps : Charlie to Food
            total += get_steps(food_loc[path[-1]][0], food_loc[path[-1]][1], hi, hj, True) # last steps  : Food to Home
            for i in range(no_food-1):
                total += get_steps(food_loc[path[i]][0], food_loc[path[i]][1], food_loc[path[i+1]][0], food_loc[path[i+1]][1])
            smallest_steps = min(smallest_steps, total)
        return smallest_steps
            
            
sol = Solution()
strArr =  [
  "FOOF", 
  "OCOO", 
  "OOOH", 
  "FOOO"]       
# 11

print(sol.leastAmountOfSteps(strArr))
        
        
                
            


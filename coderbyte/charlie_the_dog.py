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


class Solution:
    def leastAmountOfSteps(strArr):
        hi, hj = 0,0
        for i in range(4):
            for j in range(4):
                if strArr[i][j] == 'H':
                    hi, hj = i,j
                    break

        def get_cost(i,j, k,l):
            ans = abs(i-k) + abs(j-l)
            if (i==k==hi and  (l > hj > j or l < hj < j)) or (j==l==hj and (i > hi > k or i < hi < k )):
                ans += 2
            return ans
        
        
                
            


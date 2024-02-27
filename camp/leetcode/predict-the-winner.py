class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        mydict = {}
        def choose(left, right, player1):
            if (left, right, player1) in mydict:
                return mydict[(left, right, player1)]
            if left == right:
                return nums[left]
            
            if player1 == True:
                mydict[(left, right, player1)] =  max((nums[left] + choose(left+1, right, not player1)), (nums[right] + choose(left, right-1, not player1)))
            else:
                mydict[(left, right, player1)] = min((-nums[left] + choose(left+1, right, not player1)), (-nums[right] + choose(left, right-1, not player1)))

            return mydict[(left, right, player1)]

        if choose(0, len(nums)-1, True) >= 0:
            return True
        else:
            return False

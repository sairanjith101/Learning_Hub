#User function Template for python3
class Solution:
    def compareFive (ob,N):
        if N > 5:
            return "Greater than 5"
        elif N == 5:
            return "Equal to 5"
        else:
            return "Less than 5"
    
N = 5

obj = Solution()
print(obj.compareFive(N))
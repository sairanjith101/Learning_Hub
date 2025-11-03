class Solution:
    def isDigitSumPalindrome(self, n):
        num_str = str(n)
        digit_num = []
        for digit in num_str:
            digit_num.append(int(digit))

        sum_digit_num = sum(digit_num)

        sum_str = str(sum_digit_num)

        if sum_str == sum_str[::-1]:
            return 1 
        else:
            return 0 

n = 98

obj = Solution()
print(obj.isDigitSumPalindrome(n))


# option 2

class Solution:
    def findPalindrome(self,n):
        reverse_num = n[::-1]
        if reverse_num == n:
            return 1
        return 0

n = (input("Enter a value: "))
sol = Solution()
print(sol.findPalindrome(n))
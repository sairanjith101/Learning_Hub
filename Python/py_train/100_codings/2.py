class Solution:
    def palindrome(self, str):
        box = []
        for i in str:
            if i.isalnum():
                box.append(i.lower())
        clean = ''.join(box)
        return clean == clean[::-1]
            
# str = "A man, a plan, a canal: Panama"
str = "hello"
sol = Solution()
print(sol.palindrome(str))
class Solution:
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Division by zero error"
        finally:
            print("Operation complete")
            
sol = Solution()
print(sol.divide(10, 0))  # Output: Division by zero error

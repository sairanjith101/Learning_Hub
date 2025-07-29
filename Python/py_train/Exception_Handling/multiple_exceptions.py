class Solution:
    def mul_exception(self, a, b):
        try:
            a = float(a)
            b = float(b)
            return a / b
        except ZeroDivisionError:
            return "Division by zero error"
        except ValueError:
            return "Invalid input: Please enter numbers only"
        finally:
            print("Calculation attempt complete")

a = input("Enter a value A: ")
b = input("Enter a value B: ")
sol = Solution()
print(sol.mul_exception(a, b))

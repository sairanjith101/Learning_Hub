class Solution:
    def mul_exception(self, a, b):
        try:
            a = float(a)
            b = float(b)
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        except ValueError:
            return "Error: Invalid input. Please enter numeric values only."
        finally:
            print("Calculation attempt complete.")

# User input
a = input("Enter value A: ")
b = input("Enter value B: ")
sol = Solution()
print(sol.mul_exception(a, b))

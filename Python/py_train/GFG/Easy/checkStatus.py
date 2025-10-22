class Solution:
    def checkStatus(self, a, b, flag):
        if (a > 0) and (b < 0) or (a < 0) and (b > 0) and not flag:
            return True
        elif a and b < 0 and flag:
            return True
        elif a and b > 0 and flag:
            return False

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
flag_input = input("Enter flag (True/False): ").strip()

flag = True if flag_input.lower() == "true" else False

sol = Solution()
print(sol.checkStatus(a,b,flag))
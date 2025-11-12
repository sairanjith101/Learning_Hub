# case 1

# class Solution:
#     def Login_System(self, username, password):
#         user_db = {}
#         if username:
#             user_db[username] = 1
#         elif password:
#             user_db[username] = password
#         return user_db

# username = input("Enter a username: ")
# password = input("Enter a password: ")
# sol = Solution()
# print(sol.Login_System(username, password))

# case 2

class Solution:
    def Login_System(self, user_db, username, password):
        if username not in user_db:
            return False
        return user_db[username] == password

user_db = {"alice": "password123", "bob": "qwerty"}
username = "alice"
password = "password123"
sol = Solution()
print(sol.Login_System(user_db, username, password))
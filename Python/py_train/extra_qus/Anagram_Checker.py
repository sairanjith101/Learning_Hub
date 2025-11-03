# s = "anagram"
# t = "nagaram"

# s = "rat"
# t = "car"

# s = "listen"
# t = "silent"

# s = "hello"
# t = "billion"

# s = "aabbcc"
# t = "bbaacc"

def findanagram(s, t):
    # Check if lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Count occurrences of each character in both strings
    count_s = {}
    count_t = {}
    
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    
    # Compare character counts
    return count_s == count_t

# Test cases
s = "anagram"
t = "nagaram"
print(findanagram(s, t))  # Output: True




# Option 2

# def anagram_checker(s,t):

#     if len(s) != len(t):
#         return False
    
#     count_s = {}
#     count_t = {}

#     for char in s:
#         if char not in count_s:
#             count_s[char] = 1
#         else:
#             count_s[char] += 1

#     for char in t:
#         if char not in count_t:
#             count_t[char] = 1
#         else:
#             count_t[char] += 1

#     return count_s == count_t

# s = "anagram"
# t = "nagaram"

# print(anagram_checker(s,t))

# option 3
'''def findqus(s,t):
    s = sorted(s)
    t = sorted(t)

    if s == t:
        return True
    return False

print(findqus(s,t))'''

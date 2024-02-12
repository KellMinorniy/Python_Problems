def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char,  0) +  1

    for char in str2:
        if char not in char_count or char_count[char] ==  0:
            return False
        char_count[char] -=  1

    return all(value ==  0 for value in char_count.values())

str1 = input()
str2 = input()

if is_anagram(str1, str2):
    print("YES")
else:
    print("NO")
def minion_game(s):
    vowels = 'AEIOU'
    kevin_score =  0
    stuart_score =  0

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if substring[0] in vowels:
                kevin_score +=  1
            else:
                stuart_score +=  1

    if kevin_score > stuart_score:
        return f"Kevin {kevin_score}"
    elif stuart_score > kevin_score:
        return f"Stuart {stuart_score}"
    else:
        return "Draw"

s = "BANANA"
print(minion_game(s))
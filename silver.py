n = int(input())
scores = list(map(int, input().split()))
sorted_scores = sorted(scores, reverse=True)

print(sorted_scores[1])
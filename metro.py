N = int(input())
passenger_times = []
for _ in range(N):
    entry, exit = map(int, input().split())
    passenger_times.append((entry, exit))

T = int(input())
current_passengers = sum(entry <= T <= exit for entry, exit in passenger_times)
print(current_passengers)
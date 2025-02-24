N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
result = 0
for i in range(N):
    if i+1 != arr[i]:
        result += abs(i+1 - arr[i])
print(result)
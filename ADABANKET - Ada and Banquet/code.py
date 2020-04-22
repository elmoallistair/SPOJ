# Written: 22-Apr-2020
# https://www.spoj.com/problems/ADABANKET/

N = int(input())
result = 999
for i in range(N):
    A = input()
    total = min(result, A.count('1'))

print(total * 2)
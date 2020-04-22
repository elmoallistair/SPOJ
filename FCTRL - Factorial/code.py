# Written: 28-Mar-2020
# https://www.spoj.com/problems/FCTRL/

def solution(n):
    count = 0
    i = 5
    while (n / i >= 1):
        count += int(n / i)
        i *= 5

    return int(count)

if __name__ == '__main__':
    t =  int(input())
    for i in range(t):
      num = int(input())
      solution(num)

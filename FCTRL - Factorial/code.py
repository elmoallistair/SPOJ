# Written: 28-Mar-2020
# https://www.spoj.com/problems/FCTRL/

def fctrl(n):
    count = 0
    pow = 5
    while (n / pow >= 1):
        count += int(n / pow)
        pow *= 5

    print(count)


t =  int(input())
for i in range(t):
    n = int(input())
    fctrl(n)
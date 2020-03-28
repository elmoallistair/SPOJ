# Written: 28-Mar-2020
# See reference: https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/

def solution(n):
    # Initialize result
    count = 0
    # Keep dividing n by powers of 5 and update Count
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

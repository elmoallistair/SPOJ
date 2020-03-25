# Written: 25-Mar-2020

while(True):
    num = int(input())
    if (num == 42) or (num > 99):
        # Stop processing input after reading in the number 42.
        # All numbers at input are integers of one or two digits.
        break
    else:
        # Rewrite small numbers from input to output.
        print(num)

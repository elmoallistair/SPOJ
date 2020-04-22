# TEST - Life, the Universe, and Everything

Your program is to use the brute-force approach in order to _find the Answer to Life, the Universe, and Everything_. 
More precisely... rewrite small numbers from input to output. 
Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.

## Example
```
Input:
1
2
88
42
99

Output:
1
2
88
```

## Information
In case of any problems with your code, you can take a look in the forum, you'll find the answer, only for this problem, in various languages.

## Solution
```
while(True):
    num = int(input())
    if (num == 42) or (num > 99):
        break
    else:
        print(num)
```
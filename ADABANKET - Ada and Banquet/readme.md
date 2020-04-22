# ADABANKET - Ada and Banquet

Ada the Ladybug is planning two banquets. It is not an easy process since she has many friends. At first, she had a plan to invite all of her friends but the banquet hall is not big enough. Ada wants to make two blankets and invite all friends to only one of them (also note that the number of invited friends to one banquet can't be equal to **N** due to capacity).

Each friend knows some other friends (and this property is always symetrical). A friend will get one dissatisfaction for each of her friends who will not be invited to same banquet. Can you find the minimal total dissatisfaction?

## Input

The first line contains an integer **2 ≤ N ≤ 900**, the number of friends

Each of next **N** lines contain N integers **A<sub>i,j<sub>** (either **0** or **1**), where **1** means the **i<sup>th</sup>** friend is friend of. **j<sup>th</sup>**.

Note, that the matrix will be symmetrical.

Insect is not friend with himself (well .. at least in the representation).

Important note (after new studies) is, that as brain connections of insect are not so complicated as those of humans, so the process of making friends is slightly different. Two insects have exactly 10% chance of being friends, so also the adjancecy matrix will be generated (very)pseudo-randomly with 10% chance for each edge. Anyway it will be also asured, that the friendship graph will be connected.
Output

Output the minimum total dissatisfaction.

### Example Input
```
2
0 1
1 0
```

### Example Output
```
2
```

### Example Input
```
5
0 1 0 0 1
1 0 0 1 0
0 0 0 1 0
0 1 1 0 0
1 0 0 0 0
```

### Example Output
``
2
```

### Example Input
```
10
0 0 0 0 0 0 1 1 0 1
0 0 0 0 0 1 0 0 1 0
0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 1
0 1 0 0 0 0 0 0 0 0
1 0 0 1 0 0 0 0 0 0
1 0 1 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 1
1 0 0 0 1 0 0 0 1 0
```

### Example Output
```
2
```

## Solution
```
N = int(input())
result = 999
for i in range(N):
    A = input()
    total = min(result, A.count('1'))

print(total * 2)
```
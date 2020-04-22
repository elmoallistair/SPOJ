# ONP - Transform the Expression
Transform the algebraic expression with brackets into RPN form (Reverse Polish Notation). 
Two-argument operators: `+, -, *, /, ^` (priority from the lowest to the highest), brackets ( ). 
Operands: only letters: `a,b,...,z.` Assume that there is only one RPN form (no expressions like `a*b*c`).

## Input
```
t [the number of expressions <= 100]
expression [length <= 400]
[other expressions]
```
Text grouped in [ ] does not appear in the input file.

## Output
```
The expressions in RPN form, one per line.
```

## Example
```
Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*
```

## Solution
```
t = int(input())

for i in range(t):
    exp = input()
    operators =  list()
    form = ''

    for char in exp:
        if char == '(':
            pass
        elif char == ')':
            if len(operators) != 0:
                form += operators.pop()
        elif 97 <= ord(char) <= 123:X
            form += char
        else:
            operators.append(char)
    print(form)
```
# itertools

## product方法

当循环嵌套太深的时候，可以适用标准库中的product方法来返回变量之间的笛卡尔积。

```python

A = [1,2,3,4,5,6]
B = [a,b,c,d,e,f]
C = [9,8,7,6,5,4]

from itertools import product

for a in A:
    for b in B:
        for c in C:
            print(a,b,c)

for a,b,c in product(A,B,C):
    print(a,b,c)
```
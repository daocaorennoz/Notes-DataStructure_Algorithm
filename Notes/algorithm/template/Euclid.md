# 欧几里德算法/辗转相除法

## 典型模板

### 最大公约数

```python
def gcd(a,b):
	return gcd(b, a% b) if b else a
```

### 最小公倍数
```python
def lcm(a,b):
	res = a * b / gcd(a,b)
    return int(res)
```

### 扩展欧几里德算法


# Paypal笔试题

[TOC]

## 幸存者游戏 Acwing 879

题意：

有n个同学围成一圈，其id依次为1~n（n号挨着1号）。

现在从1号开始报数，第一回合报到m的人就出局，第二回合从出局的下一个人开始报数，报到m2的同学出局。

以此类推，直到最后一个回合报到mn−1的人出局，剩下最后一个同学。

输出这个同学的编号。

数据范围
    
    n≤15,m≤5

示例：

    输入样例：
    5 2
    输出样例：
    5

思路：

这是一个模拟题，数据范围不大，很容易联想到约瑟夫环问题，但这里并不是，我们只需要模拟就可以。

按照给定的n值来初始化数组，然后用p来表示探索者的位置，k原本来表示剩下的长度模上需要模的m的次方，但这里可以进行优化，$k = k * m \% r$，用k来表示模后的位置m，

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 16;

bool st[N];

int main(){
    int n,m;
    cin >> n >> m;
    int p = 1;
    for (int i = 1, r = n ; i<=n; i++,r--){
        int k = 1;
        for (int j = 1;j<=i;j++) k = k *m % r;
        if (k ==0) k = r;
        while (true) {
            if (!st[p]){
                k--;
                if (!k){
                    st[p] = true;
                    break;
                }
            }
            p++;
            if (p>n) p = 1;
        }
    }
    cout << p << endl;
    return 0;
}
// p为探索者，k为每轮取完模之后的余数，p每次都往后移，k只有遇到没删除过的才会往后移
```

```python
inp = list(map(int,input().split()))
n, m = inp[0], inp[1]
N = 16
def helper(n,m):
    st = [0] * N
    p = 1
    r = n
    i = 1
    while i <=n:
        k = 1
        for j in range(1,i+1):
            k = k* m % r
        if k == 0: k = r
        while True:
            if not st[p]:
                k-=1
                if not k:
                    st[p] = 1
                    # print(p)
                    break
            p+=1
            if p > n:
                p = 1
            # print(p)
        i +=1
        r -=1   
    return p

print(helper(n,m))
```

## 整理书架 Acwing 881

题意：图书管理员小P每天要整理书架，一个书架有N排，每一排书架上能摆放k本书，每本书上都有索引的数字编号，例如1,5,7等等。

小P喜欢从数字编号排列最整齐的书架开始整理，因为这样的话这排书架上的书就不用整理，按照整齐程度整理，最后整理最不整齐的那排书架。

那么能否请机智的你帮助小P找出整理书架的顺序呢？

整齐程度的定义：每排书架中书的编号存在的逆序对越少，这排书架就越整齐，一排书架中若书的编号完全升序即为最整洁。

逆序对的定义：在一个数组A中，在i < j的情况下，有A[i] > A[j]，则(i,j)就称为数组A中的一个逆序对。

输入格式
第一行输入N，表示书架排数。

第二行输入k，表示每排书架上书的数量。

之后的N*k的数组表示每本书的数字编号。

输出格式
输出按照整齐程度，对各排书架重新排序后得到的新N*k的数组。

输出共一行，具体形式参考输出样例。

注意，逆序数相同则按书架原有顺序整理。

数据范围

    1≤N,k≤200,
    1≤数字编号≤10000

输入样例：

    4
    8
    0 1 2 3 4 5 6 7
    11 6 5 7 3 2 2 0
    2 3 6 1 9 3 5 4
    0 2 4 5 3 10 6 7

输出样例：

    [[0, 1, 2, 3, 4, 5, 6, 7], [0, 2, 4, 5, 3, 10, 6, 7], [2, 3, 6, 1, 9, 3, 5, 4], [11, 6, 5, 7, 3, 2, 2, 0]]

思路：

    可以分为两部分，找到每一组序列中的逆序对个数，然后按照逆序对的大小输出数组，但python和cpp的实现方法不一样。

python中用一个字典来存每一行的index对应的逆序对的个数，然后将其按照逆序对个数进行升序排列，然后按照标准输出
```python
n = int(input())
m = int(input())
a= []
cnt = {}
for i in range(n):
    a.append(list(map(int,input().split())))
    cnt[i]=0
for i in range(n):
    for j in range(m):
        for k in range(j+1,m):
            if a[i][j] > a[i][k]:
                cnt[i]+=1

cnt = sorted(cnt.items(),key = lambda d:d[1])

print('[',end='')
for i in range(n):
    if i !=n-1:
        print(a[cnt[i][0]],end = ', ')
    else:
        print(a[cnt[i][0]],end='')
print(']',end='')
```

cpp中使用index数组+cnt数组来保存每一行的逆序对的个数，然后自定义比较方式，使用stable_sort对index进行排序，然后按照标准输出
```cpp
#include <iostream>
#include <algorithm>

using namespace std;


const int N = 210;
int n,m;
int a[N][N],cnt[N];
int index[N];

bool cmp(int a,int b){
    return cnt[a] < cnt[b];
}

int main() {
    cin >> n>> m;
    for(int i = 0;i<n;i++){
        for (int j = 0;j < m;j++) cin >> a[i][j];
        for (int j = 0;j < m;j++)
            for (int k= j+1;k < m;k++)
            if (a[i][j] > a[i][k])
                cnt[i] ++;
        index[i] = i;
        // cout << cnt[i] <<endl;
    }
    
    stable_sort(index,index+n,cmp);
    
    cout << '[';
    for (int i = 0;i < n ;i++){
        cout << '[';
        for (int j = 0;j <m;j++){
            cout << a[index[i]][j];
            if (j != m-1) cout << ", ";
        }
        cout << ']';
        if (i !=n-1) cout << ", ";
    }
    cout << ']';
    
    return 0;
}
```

## 最大俯冲高度 Acwing 882

题意：
近日，埃航空难的新闻牵动了无数人的心。

据悉，空难很可能是由于波音737MAX飞机的失速保护系统错误触发所致。

在飞机进行高空飞行时，驾驶辅助系统如果检测到飞机失速，无法维持足够的飞行升力，会压低机头进行俯冲，以重新获得速度，进而获取足够的飞行升力，维持飞行高度。

但是在飞机进行低空飞行时，触发俯冲机制极有可能在飞机还未获得足够飞行速度并上升之前已经撞击地面。

鉴于半年内的两起事故，波音公司决定在低于一定高度时屏蔽自动俯冲机制，现提供K架飞机用于测试最低可俯冲高度，设定需要测试的海拔范围为1~H（单位米）（注意：测试高度只从整数中选取），请问最不理想情况下，至少需要多少次才能求出飞机的最低可俯冲高度？

输入格式

    输入为整数K, H，用空格分隔。

    K代表用于测试的飞机数量，H代表需要测试的高度范围为1~H米（包含H）。

输出格式

    输出整数N，代表最坏情况下需要测试的次数。

数据范围

    1≤K≤20
    1≤H≤1000

输入样例1：
    
    1 1000

输出样例1：

    1000

输入样例2:
    
    15 1000

输出样例2：
    
    10

样例解释

    在样例#1中，只有一架飞机用来测试的情况下，从最高高度1000米，逐次减1m进行测试，直到飞机坠毁。
    在样例#2中，飞机数量足够多，每次均使用二分法进行测试。

思路：

该题出处在于谷歌的一个面试题：大致为给定m个鸡蛋，n层楼，要求出最坏情况下，得出测试鸡蛋落下不会碎掉的最高楼层的最少次数。

    用DP来做，$f[i][j]$代表i层楼j个鸡蛋再最坏情况下的最少测试次数
    鸡蛋有两个性质：
        1. 鸡蛋只有两个状态，打碎或者没碎
        2. 整个状态时单调的，在第k层打破了，第k+1层一定会打破
    所以转移方程为：

鸡蛋从第k层被扔下的情况：
鸡蛋被打破：$f[i][j] = 1 + f[k-1][j-1]$
鸡蛋没被打破：$f[i][j] = 1 + f[i-k][j]$

所以总的转移方程为(k从1枚举到i)：
$$
    f[i][j] = min(f[i][j], 1+ max(f[k-1][j-1],f[i-k][j]))
$$

状态边界情况的初始化：
$\forall i, f[i][1] = i$
$\forall i, f[1][i] = 1$

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 1010, M = 21;

int n,m;
int f[N][M];

int main(){
    cin >> m >> n;
    for (int i = 1; i <= n; i++) f[i][1] = i;
    for (int i = 1; i <= m; i++) f[1][i] = 1;
    
    for (int i = 2;i <=n; i++)
        for (int j = 2; j <= m;j++){
            f[i][j] = f[i][j-1];
            for (int k= 1;k <=i;k++)
                f[i][j] = min(f[i][j],1 + max(f[k-1][j-1],f[i-k][j]));
    }
    
    cout << f[n][m] << endl;
    return 0;
}
```

```python
a = list(map(int,input().split()))
m, n = a[0], a[1]
N = 1010
M = 21
f = [[0] * M for i in range(N)]
for i in range(1,m+1):
    f[1][i] = 1
for i in range(1,n+1):
    f[i][1] = i
# print(f)
for i in range(2,n+1):
    for j in range(2,m+1):
        f[i][j] = f[i][j-1]
        for k in range(1,i+1):
            f[i][j] = min(f[i][j],1 + max(f[k-1][j-1],f[i-k][j]))
print(f[n][m])
```
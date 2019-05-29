# DFS和BFS

[TOC]

## DFS与BFS的区别

DFS全称为深度优先搜索，其特点为一条路走到黑，不需要自行维护一个队列。
BFS全称为广度优先搜索，其特点是一次搜索一层，适合解决具有最小性的问题。

DFS

- 会引起爆栈，例如c++中的调用栈为4M，所以大概调用10万多次，所以递归层数过多，会引起爆栈
- 不具备解决最小性问题的特点
- 代码实现简单，不需要自行维护一个队列

BFS

- 不会引起爆栈
- 便于解决最小性问题
- 需要自行维护一个队列
- 很多寻路算法都由此演化而来。


## DFS的例子

- LeetCode 784. Letter Case Permutation Easy
  
  ```python
  # Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string. Return a list of all possible strings we could create.
  #Examples:Input: S = "a1b2" Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
  # 技巧：将一个字母大小写变换，可以使用Ascall码来变换，数字在字母之前，小写字母在大写字母之后，大写字母和小写字母只在二进制的第五位有区别，所以可以使用异或第五位的操作来变换。A=65，a=97
  思路：从前往后遍历，遇到字母则展开分支，一个为小写，一个变大写。则时间复杂度为2^n，n为字母个数。用u来计数遍历次数，当遍历次数达到字符串的长度，则返回结果。
  class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(S,u):
            if u == len(S):
                ans.append(S)
                return
            dfs(S,u+1)
            if S[u]>='A':
                S=S[0:u]+chr(ord(S[u])^32)+S[u+1:]
                dfs(S,u+1)

        ans=[]
        dfs(S,0)
        return ans

  ```

- LeetCode 77. Combinations Medium
  
  ```python
  # Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
  # Input: n = 4, k = 2
  # Output:[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4],]
  收获：path和path[:]是两个不一样的东西，如果单纯将path append进去，ans将为空，所以需要将path中存的值放入ans中。path为浅拷贝，path[:]为深拷贝。
  思路：求组合数，做到不重不漏，指定开始坐标，用k来计数剩余应该取的数字个数，k为0则返回结果。
  class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        self.dfs(ans,n,k,1,[])
        return ans
    
    def dfs(self,ans,n,k,start,path):
        if k==0 and path[:] not in ans:
            ans.append(path[:])
            return 
        for i in range(start,n+1):
            path.append(i)
            self.dfs(ans,n,k-1,i+1,path)
            path.pop()
            
  ```

- LeetCode 257. Binary Tree Paths Easy
  
  ```python
  # Given a binary tree, return all root-to-leaf paths.
  # Example:
  # Input:

   1
  /  \
  2   3
  \
  5

  Output: ["1->2->5", "1->3"]

  Explanation: All root-to-leaf paths are: 1->2->5, 1->3
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, x):
  #         self.val = x
  #         self.left = None
  #         self.right = None
  收获：涉及到多个dfs的递归的时候，需要注意局部变量的变化。
  思路：从根节点开始遍历，按左右子树开始分叉，当当前节点为叶子节点时，返回结果。
    class Solution:
        def binaryTreePaths(self, root: TreeNode) -> List[str]:
            ans=[]
            if not root:
                return ans
            self.dfs(ans,root,str(root.val))
            return ans
        def dfs(self,ans,node,path):
            if node.left:
                self.dfs(ans,node.left,path+'->'+str(node.left.val))
            if node.right:
                self.dfs(ans,node.right,path+'->'+str(node.right.val))
            if not node.left and not node.right:
                ans.append(path)
                return
  ```
  
- LeetCode 93. Restore IP Addresses Medium
  
  ```python
    # Given a string containing only digits, restore it by returning all possible valid IP address combinations.
    # Input: "25525511135"
    # Output: ["255.255.11.135", "255.255.111.35"]
    收获：指示标识需要跟下一步dfs的入口相对应，该题中体现在remain和i的匹配中。
    思路：一个合法的ip地址每个字段最多为三位数字，在0到255之间，所以从前往后切割，用i来记录当前分割的位置，用part来记录当前ip串中的字段个数，用done来记录已经在字段中的串，用remain来记录为分割的串。
    class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.dfs(ans,None,s,0)
        return ans
    def dfs(self,ans,done,remain,part):
        if part == 4 and remain=='':
            ans.append(done)
            return
        if part>4:
            return
        for i in range(1,min(3,len(remain))+1):
            sub_str=remain[:i]
            if (int(sub_str)==0 and i==1) or (sub_str[0]!='0' and int(sub_str)<256):
                new_done=sub_str if part ==0 else done+'.'+sub_str
                self.dfs(ans,new_done,remain[i:],part+1)
            else:
                break
  ```

- LeetCode 95. Unique Binary Search Trees II Medium

    ```python
    #Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
    Input: 3
    Output:
    [
    [1,null,3,2],
    [3,2,null,1],
    [3,1,null,null,2],
    [2,1,3],
    [1,null,2,null,3]
    ]

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    知识点：二叉搜索树的构造特点，根节点的左子树上的值全部比根节点小，右子树上的值全部比根节点大。
    思路：目标为构造一个取值范围在[1，n]之间的二叉搜索树，于是我们遍历从[1.n]之间的每个值val来做根节点，然后将[1,val-1]和[val+1,n]分别构造左子树和右子树，当l>r时，循环构造停止。
    class Solution:
        def generateTrees(self, n: int) -> List[TreeNode]:
            if not n: 
                return []
            else:
                return self.dfs(1,n)
        def dfs(self,l,r):
            res = []
            if l>r:
                return [None]
            for val in range(l,r+1):
                left=self.dfs(l,val-1)
                right=self.dfs(val+1,r)
                for i in left:
                    for j in right:
                        root=TreeNode(val)
                        root.left=i
                        root.right=j
                        res.append(root)
            return res
    ```

- LeetCode 394. Decode String Medium
  
  ```python
  # Given an encoded string, return it's decoded string.
  # The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
  # You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
  # Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
  s = "3[a]2[bc]", return "aaabcbc".
  s = "3[a2[c]]", return "accaccacc".
  s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
  思路：使用递归的思想，用cur来存会被翻倍的字符串，用stack来存[times,done],times为翻倍的次数，done为已完成的部分。
  从前往后遍历字符串s，如果遇到的是数字，就一直累积，用repeat来存翻倍的次数，如果遇到的是'['，那么将累积的次数和已经完成的部分存入stack，如果遇到的是字符，用cur来接纳字符，如果遇到的是']'，则从stack中弹出最后的元素，用已经完成的部分连接cur*翻倍的次数，最后返回cur字符串。

  class Solution:
    def decodeString(self, s: str) -> str:
        cur=''
        repeat=0
        stack=[]
        for char in s:
            # print(char)
            if char.isdigit()==True:
                repeat=repeat*10+int(char)
            elif char=='[':
                stack.append([repeat,cur])
                repeat=0
                cur=''
            elif char==']':
                temp=stack.pop()
                cur=temp[1]+temp[0]*cur
                repeat=0
            else:
                cur+=char
            # print(char)
            # print(stack)
            # print(cur)
        return cur
  ```
  
- LeetCode 341. Flatten Nested List Iterator Medium

```python
# Given a nested list of integers, implement an iterator to flatten it.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.index=-1
        self.flattenList=self.flatten(nestedList)
        self.size=len(self.flattenList)

    def flatten(self,unflatten):
        res=[]
        for i in unflatten:
            if i.isInteger():
                res.append(i.getInteger())
            else:
                res.extend(self.flatten(i.getList()))
        return res
    
    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            self.index+=1
            return self.flattenList[self.index]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index<self.size-1:
            return True
        else:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
收获：递归地将list中的每一个迭代子遍历
```

- LeetCode 756. Pyramid Transition Matrix Medium

```python
# We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.

# For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`. We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

# We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

# Return true if we can build the pyramid all the way to the top, otherwise false.
Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
思路：每一层只跟与之对应的bottom有关，可以利用这一点进行递归，首先构造rule的条件集合，再以当前bottom为入口，进行递归，递归出口为到达金字塔顶端。
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        allow={}
        for i in allowed:
            k=(i[0],i[1])
            if k in allow:
                allow[k].add(i[2])
            else:
                allow[k]={i[2]}
        # print(allow)
        return self.dfs(bottom,'',0,allow)
    
    def dfs(self,bottom,cur,idx,allow):
        # print(bottom)
        # print(cur,idx)
        if len(bottom)==1:
            print('Yes')
            return True
        if idx+1==len(bottom):
            return self.dfs(cur,'',0,allow)
        entry=(bottom[idx],bottom[idx+1])
        if entry not in allow:
            return False
        for c in allow[entry]:
            if self.dfs(bottom,cur+c,idx+1,allow):
                return True
        return False
```

- LeetCode 79. Word Search Medium

```python
# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

思路：遍历board中的每一个可能的起点，然后按顺序四个方向扩展，找到满足的字串就返回True，
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,word,0,i,j):
                    return True
        return False
    
    def dfs(self,board,word,u,x,y):
        if board[x][y] != word[u]:
            return False
        if u == len(word)-1:
            return True
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        t=board[x][y]
        board[x][y]='*'
        for i in range(4):
            a=x+dx[i]
            b=y+dy[i]
            if 0 <= a < len(board) and  0 <= b < len(board[0]):
                if self.dfs(board,word,u+1,a,b):
                    return True 
        board[x][y]=t
        return False

```

- LeetCode 464. Can I Win Medium

## BFS

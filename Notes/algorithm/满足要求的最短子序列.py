# n,m=map(int,input().strip().split())
# l=map(int,input().strip().split())
# n=12
# m=5
# # print('{}{}'.format(n,m))
# # print(l)
# l=[2,5,3,1,3,2,4,1,0,5,4,3]
# result=[]
# d={}
# for item in l:
# 	sig=1
# 	result.append(item)
# 	if result.count(result[0])==2:
# 		result.remove(result[0])
# 	for i in range(0,m+1):
# 		d[i]=result.count(i)
# 		if i>0:
# 			sig*=d[i]
# 	if sig>0:
# 		print(len(result))
# 		break
# from itertools import accumulate
# import operator
# # n,s=map(int,input().split())
# n=100
# s=48
# mod=10**9+7
# l=[i for i in range(n+1) if i!=0]
# l_result=list(accumulate(l,operator.mul))
# # print(l_result)
# l_n=l_result[n-1]
# # print(l_n)
# l_s=l_result[s-1]
# # print(l_s)
# l_r=l_result[n-s-1]
# # print(l_r)
# result=(2**(n-s))*(l_n/(l_s*l_r))%mod
# print(int(result))
n,m=map(int,input().split())
ball=list(map(int,input().split()))
colors=[0]*(m+1)
res=n+1
count=0
start=0
for i in range(n):
	if ball[i] and colors[ball[i]]==0:
		count+=1
	colors[ball[i]]+=1
	if count==m:
		while ball[start]==0 or colors[ball[start]]>1:
			colors[ball[start]]-=1
			start+=1
		res=min(res,i-start+1)
print(res)








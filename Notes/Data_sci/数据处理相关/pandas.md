# 数据探索操作

## 获得dataframe各列之间的协方差系数，并可视化

### dataframe.corr()
计算dataframe中各列的皮尔逊系数（pearson），计算公式为：

$$\rho(x,y)=\frac{cov(X,Y)}{\sigma_X\sigma_Y}=\frac{E((X-\mu_X)(Y-\mu_Y))}{\sigma_X\sigma_Y}$$

用来表示两个变量之间的相关程度，取值在（-1，1）之间，其中
- 0.8-1.0     极强相关
- 0.6-0.8     强相关
- 0.4-0.6     中等程度相关
- 0.2-0.4     弱相关
- 0.0-0.2     极弱相关或无相关

### np.zeros_like(dataframe)

### np.triu_indices(dataframe)

返回的是函数的上三角矩阵

```python
inmask = np.zeros_like(dataframe)
indices = np.tril_indices_from(dataframe)
mask[indices]= 1
```
获得了一个上三角的全1矩阵，然后配合sns中的heatmap得到相关系数的可视化矩阵。




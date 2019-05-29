
## 数据表之间的合并 join操作

### 内连接 inner join

```sql
select *** from table1 t1 inner join table2 t2 on t1.id = t2.id
```

返回的是table1和table2 中共有的记录，默认的join即为inner join

### 外连接之左外连接 left join（left outer join）

```sql
select *** from table1 t1 left join table2 t2 on t1.id = t2.id
```

left join 是left outer join的缩写，返回的是左表table1中所有的记录，右表中没有对应的记录的部分返回NULL

### 外连接之右外连接 right join （right outer join）

```sql
select *** from table1 t1 right join table2 t2 on t1.id = t2.id
```

right join 是right outer join的缩写，返回的是右表table2中的所有的记录，左表中没有对应的记录的部分返回NULL

### 全连接 full join （full outer join）

```sql
select *** from table1 t1 full join table2 t2 on t1.id = t2.id
```

full join 是left join和right join 的并集

### 笛卡尔积 cross join

```sql
select *** from table t1 cross join table t2 on t1.id = t2.id
```

返回的是t1和t2的笛卡尔积。

### 自然连接 natural join

```sql
select *** from table1 t1 natural join table2 t2 on t1.id = t2.id
```

natural join必须两表中具有相同的连接元素，此方法没什么实际意义。

## limit和offset联合进行取第几大或者第几小的元素

limit表示选几行，offset表示从第几行开始选（默认从0开始）。

distinct 表示去重
order by 中 desc 表示降序排列，默认升序

例子：选出薪资第二大的薪资。没有返回NULL

```sql
select ifnull(
    select distinct(Salary) from Employee 
    order by Salary desc limit 1 offset 1,null) as SecondHighSalary
```

## 

例子：选出薪资第N大的薪资。没有返回NULL

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set N = N-1;
  RETURN (
      # Write your MySQL query statement below.
      ifnull((select distinct Salary from Employee order by Salary desc limit 1 offset N),null)
  );
END
```

## 四大排名函数 

- row_number()

- rank()

- dense_rank()

- ntile()

模拟dense_rank()，因为mysql中没有这个函数，所以需要模拟。
```sql
# Write your MySQL query statement below
select Score,CAST(RANK AS UNSIGNED) Rank 
from
(select Score,
     case when @preScore = Score then @curerank
     else @curerank := @curerank + 1
     end as RANK,@preScore := Score 
from Scores s,(select @curerank := 0,@preScore := NULL) r
order by Score desc) temp
```

对于每一个分数，将score去重按从大到小排列，选出有多少>=score的作为其排名。
```sql
select Score,
(select count(distinct(Score)) from Scores where Score >= s.Score) Rank 
from Scores s order by Score desc;
```
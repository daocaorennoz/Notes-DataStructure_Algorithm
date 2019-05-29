# python-pickle以添加方式进行文件读取
[TOC]
## pickle介绍
模块pickle实现了对数据进行序列化存储和反序列化读取。可以通过pickle的序列化操作将程序中运行的对象信息保存到文件，永久存储;而pickle的反序列化操作可以从文件中创建上一次程序保存的对象。还有用C实现的cPickle模块
基本的接口：
- pickle.dump(obj,file,protocol):obj为待存的对象，file为存的文件，protocol为序列化使用的协议版本：（default）0：ASCLL协议;1：老式的二进制协议;2：2.3版本之后引入的新版二进制协议（较之老版更加高效）
- pickle.load(file)从file中读取字符串，并返回重构为原先的python数据对象

## pickle以追加方式读取
pickle每次存的时候，序列化生成的字符串有独立头尾，相应的取得时候每次pickle.load()会按顺序读取一个完整的结果，所以再次load会取到第二次调用dump的对象。当我们不知道文件中有多少对象可供pickle的时候，可以用while循环反复load文件对象，直到抛出异常。
###存入文件

```python
    with open(filename,'ab') as f:
        pickle.dump(第一个待存对象,f)
        pickle.dump(第二个待存对象,f)
    ...
```
###读取文件
```python
	with open(filename,'rb') as f:
		while(True):
        	取对象=pickle.load(f)
        ecxept EOFError:
        	break
```

# The use of package collections

## defaultdict
给 defaultdict 传的参数是一个工厂函数，用于确定当 key 不存在的时候，给该 key 赋予的默认值。

遍历 defaultdict 的 key 与 value 可以用 items()；
不使用 items 的时候只能获取到 key。
int 类型可以作为 defaultdict 的 key。
```
>>> from collections import defaultdict 
>>> d = defaultdict(int) 
>>>    
>>> L = [1, 2, 3, 4, 2, 4, 1, 2] 
>>> for i in L:
...     d[i] += 1
... 
>>> print(d)
defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})
>>> for k,v in d:
...     print(k,v)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot unpack non-iterable int object
>>> for item in d:
...     print(item)
... 
1
2
3
4
>>> for item in d:
...     print(d[item])
... 
2
3
1
2
>>> for k,v in d.items():
...     print(k,v)
... 
1 2
2 3
3 1
4 2
>>> print(d[0])
0
>>> print(d[1])
2
>>> print(d[4])
2
>>> print(type(d[4]))
<class 'int'>
>>> 


```
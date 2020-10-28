### 垃圾回收(garbage collection)

Python中的垃圾回收是以引用计数为主，分代收集为辅。引用计数的缺陷是循环引用的问题。
在Python中，如果一个对象的引用数为0，Python虚拟机就会回收这个对象的内存。

### 标记-清除
标记清除就是用来解决循环引用的问题的只有容器对象才会出现引用循环，比如列表、字典、类、元组。
首先，为了追踪容器对象，需要每个容器对象维护两个额外的指针，
用来将容器对象组成一个链表，指针分别指向前后两个容器对象，方便插入和删除操作。试想一下，现在有两种情况：


- [reference of juejin](https://juejin.im/post/5b34b117f265da59a50b2fbe),
- [reference of python doc](https://docs.python.org/zh-cn/3.7/library/gc.html)

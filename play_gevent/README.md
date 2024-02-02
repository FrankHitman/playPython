# Gevent
gevent，它是一个并发网络库。
它的协程是基于greenlet的，并基于libev实现快速事件循环
（Linux上是epoll，FreeBSD上是kqueue，Mac OS X上是select）。
有了gevent，协程的使用将无比简单，你根本无须像greenlet一样显式的切换，
每当一个协程阻塞时，程序将自动调度，gevent处理了所有的底层细节。

## References
[reference](http://www.bjhee.com/gevent.html)

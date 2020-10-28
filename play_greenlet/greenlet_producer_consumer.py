from greenlet import greenlet


def consumer():
    last = ''
    while True:
        print "consumer send last", last
        receival = pro.switch(last)
        print "consumer get receival ", receival
        if receival is not None:
            print 'Consume %s' % receival
            last = receival


def producer(n):
    con.switch()
    x = 0
    while x < n:
        x += 1
        print 'Produce %s' % x
        print "producer send x*2 ", x*2
        last = con.switch(x*2)  # x as a return value to consumer's receival=pro.switch(last)
        print "producer get last ", last


pro = greenlet(producer)
con = greenlet(consumer)
pro.switch(5)


# consumer send last
# Produce 1
# producer send x*2  2
# consumer get receival  2
# Consume 2
# consumer send last 2
# producer get last  2
# Produce 2
# producer send x*2  4
# consumer get receival  4
# Consume 4
# consumer send last 4
# producer get last  4
# Produce 3
# producer send x*2  6
# consumer get receival  6
# Consume 6
# consumer send last 6
# producer get last  6
# Produce 4
# producer send x*2  8
# consumer get receival  8
# Consume 8
# consumer send last 8
# producer get last  8
# Produce 5
# producer send x*2  10
# consumer get receival  10
# Consume 10
# consumer send last 10
# producer get last  10

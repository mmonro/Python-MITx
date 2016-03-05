def genPrimes():
    p = []
    x = 1
    while True:
        check = 1
        x += 1
        for i in p:
            if x % i == 0:
                check = 0
                break
        if check == 1:
            p.append(x)
            yield x
            
            
a = genPrimes()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()

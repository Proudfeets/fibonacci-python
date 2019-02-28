def fibonacci(w):
    a = 0
    b = 1
    while a + b <=w:
        if b == 0:
            a = 0
            b = 1
            c = a + b
            a = b
            b = c
            print c
        else:
            c = a + b
            a = b
            b = c
            print c
    print "End"


print fibonacci(100)

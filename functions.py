def sum(*num):
    s=0
    for n in num:
        s=s+n
    return s

def sub(*num):
    s=num[0]
    for n in num[1:]:
        s=s-n
    return s

def mol(*num):
    s=1
    for n in num:
        s=s*n
    return s

def div(*num):
    s=num[0]
    for n in num[1:]:
        s=s/n
    return s

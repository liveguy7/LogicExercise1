import sys

def carryOpp(x,y):
    ctr = 0
    if(x == 0 and y == 0):
        return 0
    z = 0

    for i in reversed(range(10)):
        z = x % 10 + y % 10 + z
        if(z > 9):
            z = 1
        else:
            z = 0
        ctr = ctr + z
        x //= 10
        y //= 10

    if(ctr == 0):
        return "No Carry Operation"
    elif(ctr == 1):
        return ctr
    else:
        return ctr

print(carryOpp(786,457))
print(carryOpp(5,6))

def revNum(n):
    s = 0
    while(True):
        k = str(n)
        if(k == k[::-1]):
            break
        else:
            m = int(k[::-1])
            n = n + m
            s = s + 1
    return n

print(revNum(1234))
print(revNum(1473))

def ngcd(x,y):
    i = 1
    while(i <= x and i <= y):
        if(x % i == 0 and y % i == 0):
            gcd = i
        i = i + 1
    return gcd

def numComm(x,y):
    n = ngcd(x,y)
    result = 0
    z = int(n ** 0.5)
    i = 1
    while(i <= z):
        if(n % i == 0):
            result = result + 2
            if(i == n/i):
                result = result - 1
        i = i + 1
    return result

print(numComm(2,4))
print(numComm(2,8))
print(numComm(12,24))


tn = input("Input Third: ")
tn = int(tn)
tltn = input("Input Last: ")
tltn = int(tltn)
sn = input("Sum: ")
sn = int(sn)

n = int(2 * sn / (tn + tltn))
print(n)

if(n - 5 == 0):
    d = (sn - 3 * tn) // 6
else:
    d = (tltn - tn) / (n - 5)

a = tn - 2 * d
j = 0

for j in range(n-1):
    print(int(a), end=' ')
    a = a + d

print(int(a), end=' ')




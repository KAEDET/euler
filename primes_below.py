import math

def primes_below_sqrt_n(n):
    l = []
    primes = []
    sqrt_n = int(math.sqrt(n))
#    print(sqrt_n)
    for i in range(sqrt_n + 1):
        l.append([True,i])
    l[0] = [False,0]
    l[1] = [False,1]
    
    for j in range(sqrt_n + 1):
        if l[j][0] == True:
            primes.append(l[j][1])
            k = 0
            while k*j <sqrt_n:
                l[k*j][0] = False
                k +=1
#        print(l)
    return primes

def phi_func(n,l):
    d_l = []
    num = n
    sq_n = int(math.sqrt(n))

    while num > 1:
        for i in l:
            if num%i == 0:
                d_l.append(i)
                num = num//i
                break
            if i > sq_n or i == l[-1]:
                d_l.append(num)
                num = 1
                break
#    print(d_l)
    
    d_l_l = [[d_l[0],0]]
    for j in d_l:
        if j != d_l_l[-1][0]:
            d_l_l.append([j,1])
        else:
            d_l_l[-1][1] += 1
#    print(d_l_l)
            
    
    sol = 1
    for p,k in d_l_l:
        sol *= p**(k-1)*(p-1)
    
    return sol
    
            
                
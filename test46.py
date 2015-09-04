def primes_and_comp_below(n):
    

    l_p = [2]
    l_c = []
    for i in range(3,n):
        flag = True
        for j in l_p:
            if i%j == 0:
                flag = False
                if i%2 != 0:
                    l_c.append(i)
                break
        if flag:
            l_p.append(i)
#    for i in l:
#        print(i)
    return l_p,l_c

def odd_below(n):
    l = [2*n+1 for n in range((n+1)//2)]
    return l


    

def determ_below(n):
    l_p, l_o = primes_and_comp_below(n)
    
    #l_sol = []
    
    pp = 0
        
    for i in l_o:
        while l_p[pp] < i:
            pp+=1
        
        flag = True
        for j in l_p[:pp]:
            x = (i-j)//2
            
            if flag == False:
                break
            else:
                for k in range(n):
                    y = x-k**2
                    if y < 0:
                        break
                    elif y == 0:
#                        print([i,j,k])
                        flag=False
                        break
        
        if flag == True:
            return i
            #l_sol.append(i)
            #break
#    return l_p,l_o,l_sol
#    return l_sol

                    
        
    
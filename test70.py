import eulerlib

import sys
import itertools
import primes_below as pb


N = int(sys.argv[1])

#D = eulerlib.numtheory.Divisors(N)
sol = []
string_0 = "0123456789"
x = pb.primes_below_sqrt_n(N)

for i in range(10,N):
    string_i = str(i)
#    print(x)
    string_phi = str(pb.phi_func(i,x))
#    string_phi = str(int(D.phi(i)))
    score_i = [0 for i in range(10)]
    score_phi = [0 for i in range(10)]
#    print((string_i,string_phi))
    for j in string_i:
        for k in string_0:
            if j == k:
                score_i[int(k)] += 1
    for j in string_phi:
        for k in string_0:
            if j == k:
                score_phi[int(k)] += 1
                
    if score_i == score_phi:
        sol.append((string_i,string_phi))
min_v=3.0
min_sol = []
for p,q in sol:
    int_p = int(p)
    int_q = int(q)
    x = int_p/int_q
    if min_v > x:
        min_v = x
        min_sol = [int_p,int_q]

    
#    string_phi = tuple(str(int(D.phi(i))))
#    for j in itertools.permutations(string_i):
#        if string_phi == j:
#            sol.append((i,int(D.phi(i))))
print(sol,min_v,min_sol)
def len_cycle(n):
    result = [n,0]
    num = 10
    num_list = []
    sol = []
    count = 0
    flag = True
    while flag:
        sol.append(num//n)
        count += 1
        y = num%n
        j = 0
        for i in num_list:
            j += 1
            if y == i:
                flag = False
                result[1] = count - j
        num_list.append(num%n)
        num = y
        num = num * 10
                    
    return {"result":result, "sol":sol}

def result_(n):
    l = len_cycle(n)
    return l["result"]
    

def solution(n):
    max_ = 0
    max_v = 0
    i = 0
    while i < n:
        i += 1
        if max_ < result_(i)[1]:
            max_ = result_(i)[1]
            max_v = i
            print(max_)
    return max_, max_v
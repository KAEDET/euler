def num(l_0):
    l = []
    p_1 = []
    p_2 = []
    for i in l_0:
        p_1 = ""
        p_2 = ""
#        print(i)
        for j in range(5):
            p_1 += i[0][3*j]
            p_2 += i[1][3*j]
            p_1 = sorted(p_1)
            p_2 = sorted(p_2)
        l.append([p_1,p_2])

    return l

def hands():
    l = []
    with open("test54.txt") as f:
        for i in f.readlines():
            l.append([i[:15],i[15:]])
    return l


def num_score(hand,num):
    score = {"H":0,"One":0,"Two":0,"Three":0,"ST":0,"F":0,"FuH":0,"Four":0,"SF":0,"RSF":0} 
    t = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    t_num = {i:0 for i in t}
    num_sc = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14}

    
    for j in num:
        for k in t:
            if j == k:
                t_num[k] += 1
    #Fの判定
    if hand[1]==hand[4]==hand[7]==hand[10]==hand[13]:
        for i in t:
            if t_num[i] >= 1:
                score["F"] += 2**num_sc[i]
    
    #STの判定
    x = 0
    stsc = 0
    for i in t:
        if  x == t_num[i] == 1:
            stsc += 1
        x = t_num[i]
    if stsc == 4:
        for i in t:
            if t_num[i] >= 1:
                score["ST"] += 2**num_sc[i]
    #SFとRSTの判定
    if score["ST"] != 0 and score["F"] != 0:
        for i in t:
            if t_num[i] >= 1:
                score["SF"] += 2**num_sc[i]
        if t_num["A"] >=1:
            for i in t:
                if t_num[i] >= 1:
                    score["RSF"] += 2**num_sc[i]
    
    #pairの判定
    pr2 = []
    pr3 = []
    pr4 = []
    
    for i in t:
        if t_num[i] == 2:
            pr2.append(i)
        if t_num[i] == 3:
            pr3.append(i)
        if t_num[i] == 4:
            pr4.append(i)
            
    for i in pr4:
        score["Four"] += 2**num_sc[i]
    for i in pr3:
        score["Three"] += 2**num_sc[i]
    for i in pr2:
        score["One"] += 2**num_sc[i]
        
    if len(pr2) == 1 and len(pr3) == 1:
        score["FuH"] += 1
    if len(pr2) == 2:
        for i in pr2:
            score["Two"] += 2**num_sc[i]
    for i in t:
        if t_num[i] >= 1:
            score["H"] += 2**num_sc[i]
                
    return score

#main
yaku = ["RSF","SF","Four","FuH","F","ST","Three","Two","One","H"]
hand = hands()
nums = num(hand)
win_1 = 0
for i in range(1000):
    score_1 = num_score(hand[i][0],nums[i][0])
    score_2 = num_score(hand[i][1],nums[i][1])
    print([score_1,score_2])
    for j in yaku:
        if score_1[j] > score_2[j]:
            win_1 += 1
            break
        if score_1[j] < score_2[j]:
            break
print(win_1)

        
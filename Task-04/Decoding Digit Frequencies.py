def freq(S):
    fr = {i:0 for i in range(10)}
    for i in S:
        if i.isdigit():  
            fr[int(i)] += 1  
    return fr

S = input()
fr = freq(S)
for f in range(10):
    print(fr[f], end=" ")
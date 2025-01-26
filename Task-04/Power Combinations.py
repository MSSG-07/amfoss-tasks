def count_pow(X, N):
    powers = []
    num = 1
    while True:
        Pow = num ** N
        if Pow > X:
            break
        powers.append(Pow)
        num += 1
        
    L = [0] * (X + 1)
    L[0] = 1
    for r in powers:
        for j in range(X, r - 1, -1):
            L[j] += L[j - r]
    return L[X]

X = int(input())
N = int(input())
res = count_pow(X, N)
print(res) 
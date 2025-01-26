n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

missing_numbers = []
for num in B :
    if B.count(num) > A.count(num):
        missing_numbers.append(num)

missing_numbers = list(set(missing_numbers))
missing_numbers.sort() 

print(' '.join(map(str, missing_numbers)))
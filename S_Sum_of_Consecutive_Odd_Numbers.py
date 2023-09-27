def sum_odd_numbers(x, y):
    total = 0
    for num in range(x+1, y):
        if num % 2 != 0: 
            total += num
    return total

t = int(input())

while t!=0:
    a,b = input().split()
    a = int(a)
    b = int(b)

    mx = max(a,b)
    mn = min(a,b)
    res = sum_odd_numbers(mn,mx)
    print(res)
    t-=1
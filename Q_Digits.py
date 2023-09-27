# t = int(input())

# for i in range(1, t + 1):
#     n = int(input())
#     while n != 0:
#         print(n % 10, end=' ')
#         n = n // 10
        
#     print()

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    while True:
        print(n % 10, end=' ')
        n = n // 10
        if n==0:
            break
    print()
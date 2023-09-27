# def fib(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


# n = int(input())


# fib_sequence = [fib(i) for i in range(1, n + 1)]
# print(*fib_sequence)


# Function to generate Fibonacci sequence iteratively
def generate_fibonacci(N):
    fib_sequence = [0, 1]
    while len(fib_sequence) < N:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence[:N]

# Input
N = int(input())

# Output
fib_sequence = generate_fibonacci(N)
print(*fib_sequence)


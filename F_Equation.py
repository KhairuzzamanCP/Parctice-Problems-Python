# Function to calculate the equation result
def calculate_equation_result(X, N):
    result = 0
    for i in range(2, N + 1, 2):
        result += X ** i
        
    return result

# Input
X, N = map(int, input().split())

# Output
S = calculate_equation_result(X, N)
print(S)

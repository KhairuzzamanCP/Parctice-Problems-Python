# Input
K, S = map(int, input().split())

# Initialize a variable to count the solutions
count = 0

# Iterate through possible values of X
for X in range(K + 1):
    # Iterate through possible values of Y
    for Y in range(K + 1):
        # Calculate Z
        Z = S - X - Y
        
        # Check if X, Y, and Z are within the valid range
        if 0 <= Z <= K:
            count += 1

# Output the count of valid solutions
print(count)

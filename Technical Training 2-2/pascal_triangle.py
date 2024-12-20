# Initialize the triangle
numRows = 5
result = []

for i in range(numRows):
    # Create a new row with 1 at the beginning and end
    row = [1] * (i + 1)
    # Fill in the middle elements (if any) by summing the two numbers above
    for j in range(1, i):
        row[j] = result[i - 1][j - 1] + result[i - 1][j]
    # Append the row to the triangle
    result.append(row)

print(result)
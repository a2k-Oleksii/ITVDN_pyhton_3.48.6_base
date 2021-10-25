matrix = [[j+i for j in range(8) for i in range(3)]]
print(matrix)

print("------------------------------------")

flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)

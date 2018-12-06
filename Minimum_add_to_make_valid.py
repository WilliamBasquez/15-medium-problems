def minAddToMakeValid(str1):
	compare = "()"
	rows = len(str1)+1
	cols = len(compare)+1
	matrix = []

	equal = 1
	for i in range(len(str1)-1):
		if str1[i] == str1[i+1]:
			equal+=1

	if equal == len(str1):
		return len(str1)

	for i in range(rows):
		matrix.append([0] * cols)
		matrix[i][0] = i

	for j in range(cols):
		matrix[0][j] = j

	for k in range(1,rows):
		for l in range(1, cols):
			if str1[k-1] != compare[l-1]:
				matrix[k][l] = min(matrix[k-1][l-1], matrix[k-1][l], matrix[k][l-1])+1
			else:
				matrix[k][l] = matrix[k-1][l-1]

	return matrix[len(matrix)-1][len(matrix[0])-1]

def main():
	print(minAddToMakeValid("()))(("))

main()
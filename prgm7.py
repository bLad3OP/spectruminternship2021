def find3Numbers(A, arr_size, add):
	for i in range( 0, arr_size-2):
		for j in range(i + 1, arr_size-1):
			for k in range(j + 1, arr_size):
				if A[i] + A[j] + A[k] == add:
					print("Triplet is", A[i],", ", A[j], ", ", A[k])
					return False
	return False

A = list(map(int,input().split()))
s = int(input())
arr_size = len(A)
res = find3Numbers(A, arr_size, s)
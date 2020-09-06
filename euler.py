def mat(m , size , n):
	maxval = 0
	for i in range(size - n + 1):
		for j in range(size - n + 1):
			a = []
			for k in range(4):
				sublist = m[i+k][j:j+4]
				a.extend([sublist])
			rdiasum = 0
			ldiasum = 0
			for l in range(len(a)):
				colsum = 0
				rowsum = 0
				rdiasum = rdiasum + a[l][l]
				ldiasum = ldiasum + a[l][3-l]
				for o in range(len(a)):
					rowsum = rowsum + a[l][o]
					colsum = colsum + a[o][l]
				if rowsum > maxval:
					maxval = rowsum
					out = a[l]
				if colsum > maxval:
					maxval = colsum
					out = [a[0][l] , a[1][l] , a[2][l] , a[3][l]]
			if rdiasum > maxval:
				maxval = rdiasum
				out = [a[0][0] , a[1][1] , a[2][2] , a[3][3]]
			if ldiasum > maxval:
				maxval = ldiasum
				out = [a[0][3],a[1][2],a[2][1],a[3][0]]
	val = 1
	for i in out:
		val = val*i
	return(val , out)

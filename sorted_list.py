ls = [1, 2, 3, 6, 8, 9, 10]

def is_sorted(ls):
	for i in range(len(ls) - 1):
		if ls[i] > ls[i + 1]:
			return False
	return True

print(is_sorted(ls))

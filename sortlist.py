ls1 = [1, 2, 3, 4, 5, 6, 7, 8]
ls2 = [0, 1, 3, 5, 6, 7, 8 ]
def merge(ls1,ls2):
	sorted_list = ls1 + ls2
	for i in range(len(sorted_list) - 1, -1, -1):
		for j in range(len(sorted_list) - 1, -1, -1):
			if sorted_list[i] > sorted_list[j]:
				sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
	
				
	return sorted_list

print(merge(ls1, ls2))


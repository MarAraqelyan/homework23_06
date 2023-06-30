while True:
	n = int(input("Enter a positive number that is less than 1015:"))
	if n >= 0 and n <= 1015:
		break
ls = []
number = []

def int_str(a):

	div10 = ['', '', 'hundred', 'thousand']
	tens = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	tenits = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

	if n == 0:
		print('zero')
		return
	while(a > 0):
		i = a % 10
		ls.append(i)
		a = a // 10
		
	for i in range(len(ls) - 1, -1, -1):
		if ls[i] == 0:
			continue

		if i == 1:
			if ls[i] == 1:
				number.append(tenits[ls[i - 1]])
				break
			elif ls[i -1] == 0:
					number.append(tens[ls[i]])
					break
			else:
				number.append(tens[ls[i]] + ' -')
		else:
			number.append(units[ls[i]])
			number.append(div10[i])
	print(*number)
int_str(n) 

 

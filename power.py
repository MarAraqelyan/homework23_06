def power_of(n):
	def power(num):
		power = pow(num,n)
		return power
	return power

n = int(input("Enter the n:"))
num = int(input("Enter the number:"))

print(power_of(n)(num))

x = int(input("Enter the x:"))
factor = 2
def outer_function(x):
	def inner_function(factor):
		x *= factor
	print(inner_function(factor))

outer_function(x)
		

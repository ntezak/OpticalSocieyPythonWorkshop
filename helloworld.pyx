# Pure Python function
def hi():
	print "Hello World!"

# Numeric function, but all Python
def fib(n):
	a, b = 1, 1
	for i in range(n):
		c = a + b
		b = a
		a = c
	return a
	
# Numeric function, but all Python
def fib_c(int n):
	cdef int a = 1, b = 1, c, i
	for i in range(n):
		c = a + b
		b = a
		a = c
	return a
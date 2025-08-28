def	xor_func(x, s):
	return(x ^ s)

x = int(input("Enter x: "))
s = int(input("Enter s: "))
print(x, "xor", s, "=", xor_func(x, s))
print(bin(x), "xor", bin(s), "=", bin(xor_func(x, s)))

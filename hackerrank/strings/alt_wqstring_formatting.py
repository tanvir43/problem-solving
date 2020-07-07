def f(n):
return "\n".join(["{0} {1} {2} {3}".format(i, oct(i)[2:], hex(i)[2:], bin(i)[2:])] for i in range(1, n-1))

print(f(10))

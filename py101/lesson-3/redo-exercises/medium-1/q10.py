# In Python, every object has a unique identifier that can be accessed using
# the id() function. This function returns the identity of an object,
# which is guaranteed to be unique for the object's lifetime. For certain
# basic immutable data types like short strings or integers, Python might
# reuse the memory address for objects with the same value. This is known
# as "interning".

# Given the following code, predict the output:



a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# SOLUTION
# the outpuyt is TRue, since a is initailized with integer 42, b is also initialzied with same integer,
# so puythoin will reuse that memory space (id). c is then iunitialized and points to the same integer 42 that a points to,
g = lambda x:x+3

"""
def wow(f):
    def boom(g):
        return f(g)
    return boom
"""

wow = lambda f: lambda g: f(g) # the two definations of wow are same
f = wow(g)

f(2)#5

g= lambda x:x*x
f(3)#6  the change of g doesn't affect the value of f
wow(g)(3) #9 the change of g  affects the value of wow(g)(3)


a = lambda: 5
b = lambda: lambda x: 3
c = lambda x, y: x + y
d = lambda x: c(a(), b()(x))

d(2)#8

b = lambda: lambda x: x
d(2)#7 the change of b affects the value of d


# so the inputs of a function can be changed while the inner structure of a function cannot
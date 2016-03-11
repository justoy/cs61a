#tricky Q1
g = lambda x:x+3

"""
def wow(f):
    def boom(g):
        return f(g)
    return boom
"""

wow = lambda f: lambda g: f(g) # the two definations of wow are same
f = wow(g)#f=wow(g)->lambda z:g(z)->lambda z:z+3

f(2)#5

g= lambda x:x*x
f(3)#6  the change of g doesn't affect the value of f, 
    #because g = lambda x:x+3 is part of the inner structure of f
wow(g)(3) #9 the change of g  affects the value of wow(g)(3)


a = lambda: 5
b = lambda: lambda x: 3
c = lambda x, y: x + y
d = lambda x: c(a(), b()(x))

d(2)#8

b = lambda: lambda x: x
d(2)#7 the change of b affects the value of d, 
      #because b is the input of d not the inner structure

#trick Q2
def troy():
    abed = 0
    while abed < 10:
        britta = lambda: abed
        print("abed : %d, britta(): %d"%(abed,britta()))
        abed += 1
    abed = 20
    print(britta())
    return britta

jeff = troy()
#abed : 0, britta(): 0
#abed : 1, britta(): 1
#abed : 2, britta(): 2
#abed : 3, britta(): 3
#abed : 4, britta(): 4
#abed : 5, britta(): 5
#abed : 6, britta(): 6
#abed : 7, britta(): 7
#abed : 8, britta(): 8
#abed : 9, britta(): 9
#20

shirley = lambda : jeff
pierce = shirley()
pierce()
#20

#so the free variable in lambda is bound to the environment
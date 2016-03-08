def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    "*** YOUR CODE HERE ***"
    def h(x):
        if x < b:
            return f(x)
        else:
            return g(x)
    return h

def repeated(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)#5+1+1+1
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1,
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    """
    "*** YOUR CODE HERE ***"
    g=f
    while(n>1):
        n=n-1
        g=compose1(f,g)
    return g

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

###################
# Church Numerals #
###################

def zero(f): 
    return lambda x: x
#zero(f)(x)=x ->zero(1)(1)=1,zero(2)(1)=1,zero(2)(3)=3

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):#successor(zero)=f(zero(f)(x))=f(x)
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(x)
#one(f)(x)=f(x)

def two(f):#successor(one) = f(one(f)(x))=f(f(x))
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(f(x))
#two(f)(x)=f(f(x))

three = successor(two)

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"
    return n(increment)(0) 
# church_to_int(zero)=zero(increment)(0)=0
# church_to_int(one) = one(increment)(0)=increment(0)=1
# ...


def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"
    return lambda f:lambda x: m(f)(n(f)(x))
    # church_to_int(add_church(m,n))->lambda f:lambda x: m(f)(n(f)(x))(increment)(0)->lambda x: m(increment)(n(increment)(x))(0)->m(increment)(n(increment)(0))->m(increment)(number_n)->number_n+m*1
    # church_to_int(add_church(one, zero)) ->one(increment)(zero(increment)(0))->one(increment)(0)->increment(0)->1

def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"
    return lambda f: m(n(f))
    # church_to_int(mul_church(m,n))->lambda f:(m(n(f)))(increment)(0)->m(n(increment))(0): every layer applys increment n times, and there are m leyers, so m*n increments in total
    # church_to_int(mul_church(one,zero))->one(zero(increment))(0)->one(lambda x: x)(0)->(lambda x:x) (0)->0
    # church_to_int(mul_church(one,two))->one(two(increment))(0)->one(lambda x: increment(increment(x)))(0)->(lambda x: increment(increment(x)))(0)->2

def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    return n(m)
    # church_to_int(pow_church(m,n)) -> n(m)(increment)(0)->expand the n: (lambda x: m(...m(m(x))...)(increment)(0)->number_m**number_n
    # church_to_int(pow_church(one,zero)) -> one(zero)(increment)(0) -> one(lambda x: x)(increment)(0) ->(lambda x: x)(increment)(0)->increment(0)->1
    #church_to_int(pow_church(two,three))-> two(three)(increment)(0)->(lambda x: three(three(x)))(increment)(0)->9


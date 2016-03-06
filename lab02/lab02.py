"""Required questions for lab 2"""

## Boolean Operators ##

# Q6
def both_positive(x, y):
    """
    Returns True if both x and y are positive.
    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    "*** YOUR CODE HERE ***"
    return x >0 and y > 0

## while Loops ##

# Q9
def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    for factor in range(n+1,0,-1):
        if(n%factor==0):
            print(factor)
# Q10
def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    """
    "*** YOUR CODE HERE ***"
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fib1=0
        fib2=1
        i=2
        while(i<=n):
            tmp=fib1
            fib1=fib2
            fib2 = fib1 + fib2
        return fib2

"""
this file contains some custom modules
    fib

"""


def fib(nterms):
    """fib(n)--> return first n terms of fibonacci series
    >>>fib(5)
    0, 1, 1, 2, 3
    
    """
    start = 0
    end = 1
    print(start,end,sep=", ",end=", ")
    for var in range(nterms-2):
        start,end=end,start+end
        print(end,end=", ")
if __name__ == "__main__" :
    nterms = int(input("Enter numbr of terms : "))
    fib(nterms)

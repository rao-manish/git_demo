"""
add module is used add two number
"""
def add(x,y):
    """
    add(x,y) -> x + y
    example :
    >>>add(4,5)
    9
    """
    return x+y

if __name__ == "__main__" :
    x,y = map(int,input("x,y : ").split(","))
    print(f"{x} + {y} = {x+y}")

"""
**Task**
Given an integer, n, perform the following conditional actions:

* If n is odd, print `Weird`
* If n is even and in the inclusive range of 2 to 5, print `Not Weird`
* If n is even and in the inclusive range of 6 to 20, print `Weird`
* If n is even and greater than 20, print `Not Weird`
"""

def odd(n):
    return True if n%2!=0 else False
# def even(n):
#     return True if n%2==0 else False

if __name__ == '__main__':
    n = int(input().strip())
    # print("Weird") if odd(n) else (print("Not Weird") if n in range(2,6) else (print("Weird") if n in range(6,21) else (print("Not Weird") if n>20 else print('') )))
    # another
    n = int(input().strip())
    if n%2!=0:
        print('Weird')
    elif (2<=n<=5): # n in range(2,6)
        print('Not Weird')
    elif (6<=n<=20): # n in range(6,21)
        print('Weird')
    elif n>20:
        print('Not Weird')
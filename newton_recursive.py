def newton_sqrt(a):
    """Calculate the square root of a number using Newton's method."""
    # Guard statements to handle edge cases
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    elif a == 0:
        return 0

    # Define the tolerance level for convergence
    epsilon = 0.0001 
    # Base 
    x = a / 2.0

    newton_calculation(a) 
    if abs(x * x - a) > epsilon and loops < 1000:

    


#this will do the sqrt calculations on a single value for a meaning I can call the function over and over instead of using a while loop
def newton_calculation(a, loops=0):
    x = (x + (a/x)) / 2
    loops += 1
    return x and loops

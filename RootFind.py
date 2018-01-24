
'''''''''''''''''''''

    The function findRoot(f,a,b,eps) will locate a root of f
    that is bracketed by [a,b] up to an accuracy of eps.

    findRoot uses the bisection method to approach the root
    (up to 3 digit accuracy) then uses Newton's method to
    achieve the remaining degrees of accuracy. If the function's
    derivative is not passed to findRoot, the function finds
    a root entirely with bisection.

    However, if speed is a concern, passing f_prime is recommended
    because Newton's method has a quadratic rate of convergence
    while bisection has a linear rate of convergence.

    The minimum value for epsilon is 10^-6.

    Author:   Connor Harris

'''''''''''''''''''''


def bisection(f, a, b, eps):

    if f(a) == 0: return a
    if f(b) == 0: return b

    e_initial = eps * abs(a - b)
    a_initial = a
    mid = a

    while abs(f(mid)) > abs(f(a_initial))*eps:

        mid = (a + b) / 2

        if f(mid) == 0: return mid

        if f(mid)*f(a) > 0:
            a = mid
        else:
            b = mid
    #Close while.
    return mid


def newtonsMethod(f, f_prime, x0, eps):

    if f(x0) == 0: return x0

    x = x0
    x_np1 = x0

    while abs(f(x_np1)) > abs(f(x0))*eps:
        if f_prime(x) == 0:
            return "Error. Newton's method has a 0 derivative! Use findRoot without specifying f_prime to use bisection only."
        x_np1 = x - f(x)/f_prime(x)
        x = x_np1
    return x_np1


def findRoot(f, a, b, eps, f_prime=0):
    if f(a) * f(b) > 0:
        return 'ERROR: findRoot requires a and b to bracket the root.'
    if eps > 10**-6:
        #Minimum accuracy is 10**-6
        eps = 10**-6

    if f_prime == 0:
        #Use bisection.
        print('\nOnly Using bisection')
        return bisection(f, a, b, eps)

    BISECTION_EPS = 10**-3
    #Approach the root with bisection (linear convergence)
    x0  =  bisection(f, a, b, BISECTION_EPS)
    #Complete root finding with a quadratic rate of convergence
    return newtonsMethod(f, f_prime, x0, eps)

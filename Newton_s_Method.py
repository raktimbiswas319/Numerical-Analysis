def newton(fn, dfn, p0, eps, maxit):
    approx = [p0] #create a list of approximations, intial guess p0 or pn-1 (note p0 is approximated without using our algorithm)
    for n in range(maxit):
        p1 = p0 - fn(p0)/dfn(p0) #for first iteration p1 equivalent to pn, n would be number of iterations/ approximations made using our algorithm
        approx.append(p1) #with each iteration we add new approximation to the list
        print(n+1, p1)
        if ((abs(p1-p0) < eps) or (n+1 == maxit)): break #max iterations met or we've found pn s.t. approximation is within our desired degree of precision, no need to start another iteration
        p0=p1 #since newton's method is iterative each approximation pn becomes the starting point pn-1 for our next approximation
    print(*approx)
    n=n+1 #n startsat 0 so to count correct number of iterations we add 1
    return approx, approx[0], approx[n], n

y = lambda x: ((2.5)/(7+x))**2 + ((1.5)/(4+x))**2 + ((0.1)/(0.3+x))**2 - 0.01 #define functions for f(x), f'(x) outside of our method for reusability
dy = lambda x: -(12.5/(7+x)**3 + 4.5/(4+x)**3 + 0.02/(0.3+x)**3)
guess = float(input("Enter initial guess for p0 as a decimal value: "))
#eps = float(input("Enter desired degree of precision as a decimal value: "))
#maxit= int(input("Enter maximum number of iterations: "))
#user inputs can be taken but for simplicity i will pass the parameters myself since it doesn't alter the method itself
#user input for the initial guess is useful to understand how choosing bad points affect results and how the program behaves
lamb = newton(y, dy, guess, 10**-12, 20)

print("List of approximations: ", lamb[0], "\nInitial guess: ", lamb[1], "\nFinal approximation: ", lamb[2], "\nNumber of iterations: ", lamb[3])

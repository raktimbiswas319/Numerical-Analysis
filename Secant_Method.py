def secant(fn, p0, p1, eps, maxit): #p0~pn-1, p1~pn, p2~pn+1
    approx = [p0, p1] #create list of approximations
    for n in range(maxit):
        p2 = p1 - (p1-p0)/(fn(p1)-fn(p0)) * fn(p1)
        print(n+1, p2)
        approx.append(p2)
        if ((abs(p2-p1) < eps) or (n+1==maxit)) : break
        else: 
            p0=p1 #set values for next iteration
            p1=p2
    print(*approx)
    n=n+1 
    return approx, approx[n+1], n #n is the number of approximations made using our algorithm, doesn't account for p0 and p1 indices so we add 1 to n to return final approximation

y = lambda x: ((2.5)/(7+x))**2 + ((1.5)/(4+x))**2 + ((0.1)/(0.3+x))**2 - 0.01
p0 = float(input("Enter decimal value for p0 greater than or equal to zero: "))
p1 = float(input("Enter decimal value for p1 not equal to p0: "))
lamb = secant(y, p0, p1, 10**-12, 20) #lamb will return a list of approximations, final approximation, and number of iterations

print("List of approximations ", lamb[0], "\nFinal approximation: ", lamb[1], "Number of iterations: ", lamb[2] )


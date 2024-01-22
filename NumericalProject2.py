import numpy as np

def divdiff(x, y):
    #m = len(x) let m=n+1, for some reason value of m is set to 1 instead of 21 when the method is called later even though arrays of x and y values are of length 21
    a = np.zeros([21,22]) #create table, deg n polynomial gives n+1 points and n+1 divdiffs
    #first column holds y values aka 0th divdiffs
    #note the last column holds x values so we add a column instead of creating a square matrix, this lets us calculate divdiff in forloop with ease instead
    #if first column contained x values, we would have to offset our j values by 1 in the forloop which is confusing
    a[:,0] = y
    a[:,21] = x
    #print(*a)
    for j in range(1, 21): #nested forloop calculates entries for table by column, we start with 1st divdiff and end with nth divdiff
        for i in range(j,21): #i is equal to or greater than j to fill table along and below the diagonal
            a[i,j] = ((a[i,j-1] - a[i-1,j-1])/(a[i,21] - a[i-j,21]))
    co = np.zeros(21)
    for k in range(0, 21): 
        co[k] = a[k,k] #coefficients are elements of main diagnoal
    print(*a)
    return co #coefficients, if we wanted we could return the table as well but it gets messy and program gets confused when we evaluate

def newpoly(ak, xk, evalpoint):
    n = len(xk)-1
    p = ak[n] 
    for k in range(1,n+1):
        p = ak[n-k] + (evalpoint - xk[n-k])*p #nested form, similar to horners, allows us to generate the polynomial recursively
        print(p)
        #if we consider the nested form, the nth coefficient is buried furthest in the nest so our forloop begins with the highest degree coefficient
        #by the nested form, if we evaluate at x thats relatively close to x0, we will be left with a value close to a0
    return p 

xvals1 = np.zeros((1,21)) #empty arrays of n+1 points initialized, values generated in forloop
yvals1 = np.zeros((1,21))
xvals2 = np.zeros((1,21))
yvals2 = np.zeros((1,21))
func1 = lambda x : 1/(1+25*(x)**2) #creates function outside of forloop to assign y values after uniform x values are generated
func2 = lambda k : np.cos((2*k+1)*np.pi/(42)) #creates function outside of forloop for generating unevenly spaced x values (42=2(n+1) for n=20)

x1 = 0.1
x2 = 0.985
y1 = func1(x1)
y2 = func1(x2)

for k in range(21): #values created and appended to lists
    xk1 = -1 + k*(0.1) #first case of evenly spaced xvalues generated
    np.put(xvals1, [k], [xk1])
    yk1 = func1(xk1) #yvalues corresponding to evenly spaced xvalues
    np.put(yvals1, [k], [yk1])

    xk2 = func2(k) #second case of uneven xvalues generated
    np.put(xvals2, [k], [xk2])
    yk2 = func1(xk2) #yvalues corresponding to unevenly spaced x values
    np.put(yvals2, [k], [yk2])
    #print(k, xk1, xk2, yk1, yk2) verify correct values are created with each iteration
#print(xvals1, xvals2, yvals1, yvals2)
coeff11 = divdiff(xvals1, yvals1)
coeff22 = divdiff(xvals2, yvals2)

eval11 = newpoly(coeff11, xvals1, x1) #evaluation for x=0.1 is the same as for x=0.985, this should not happen, but evaluation seems correct for x=0.985 for both uniform and chebyshev nodes
eval12 = newpoly(coeff11, xvals1, x2) #my method for evaluating the polynomial at any given x value outputs the same value for some reason

eval21 = newpoly(coeff22, xvals2, x1)
eval22 = newpoly(coeff22, xvals2, x2)

err11 = 100*abs((eval11-y1)/y1)
err12 = 100*abs((eval12-y2)/y2)

err21 = 100*abs((eval21-y1)/y1)
err22 = 100*abs((eval22-y2)/y2)

print("for x=", x1, "f(x)=", y1, "\nfor x=", x2, " f(x)=", y2)
print("evenly spaced nodes", xvals1, "\ncoefficients of uniform nodes: \n", coeff11, "\nevaluation at x=",x1, ": ", eval11, "relative error (%) ", err11, "\nevaluation at x=", x2, ": ", eval12, "relative error (%) ", err12)
print("chebyshev nodes", xvals2,"\ncoefficients of chebyshev nodes: \n", coeff22, "\nevaluation at x=", x1, ": ", eval21, "relative error (%) ", err21, "\nevaluation at x=", x2, ": ", eval22, "relative error (%) ", err22)

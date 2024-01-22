a10 = cgA(10)
a100 = cgA(100)
a1000 = cgA(1000)
a2000 = cgA(2000)

ahat10 = cgAhat(10)
ahat100 = cgAhat(100)
ahat1000 = cgAhat(1000)
ahat2000 = cgAhat(2000)

function rnorm = cgA(n)
    A = full(gallery('tridiag',n,-1,2,-1));
    b = zeros(n,1);
    x = zeros(n,1);
    for i=1:n
        if i==1
            b(i) = i + (i^2)/(n+1)^4;
        elseif i==n
            b(i) = 6 + (i^2)/(n+1)^4;
        else
            b(i) = (i^2)/(n+1)^4;
        end
    end
    
    r = b - A*x;
    v = r;
    rinnerold = r'*r; 
    for i=1:n
        t = rinnerold/(v'*A*v);
        x = x + t*v;
        r = r -t*A*v;
        rinnernew = r'*r;
        rnorm = sqrt(rinnernew);
        if rnorm < 1e-8
            i
            break;
        end
        s = (rinnernew/rinnerold);
        v = r + s*v;
        rinnerold = rinnernew;
    end
end

function rnorm = cgAhat(n)
    Ahat = full(gallery('tridiag',n,-1,3,-1));
    b = zeros(n,1);
    x = zeros(n,1);
    for i=1:n
        if i==1
            b(i) = i + (i^2)/(n+1)^4;
        elseif i==n
            b(i) = 6 + (i^2)/(n+1)^4;
        else
            b(i) = (i^2)/(n+1)^4;
        end
    end
    
    r = b - Ahat*x;
    v = r;
    rinnerold = r'*r;
    for i=1:n
        t = rinnerold/(v'*Ahat*v);
        x = x + t*v;
        r = r -t*Ahat*v;
        rinnernew = r'*r;
        rnorm = sqrt(rinnernew);
        if rnorm < 1e-8
            i
            break;
        end
        s = (rinnernew/rinnerold);
        v = r + s*v;
        rinnerold = rinnernew;
    end
end

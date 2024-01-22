    n = 10;
    A = full(gallery('tridiag',n,-1,2,-1));
    b = zeros(n,1);
    for i=1:n
        b(i) = (i^2)/(n+1)^4;
    end
    xkminus1 = zeros(n,1); % initial guess
    xk = xkminus1;
    D = diag(diag(A)); % main diagonal, = M
    N = D - A;
    T = D\N; % iteration matrix, invM*N
    e = 10^-4;
    infnormdx=inf;
    
    it=0;
    while infnormdx > e
        xkminus1=xk;
        dx = D\(b-A*xkminus1); % dx = invD*[b-Ax^(k-1)]
        % or dx = x^(k) - x^(k-1)
        % change in approximation with each iteration
        xk = xk + dx; % x^(k) = x^(k-1) + invD*[b-Ax^(k-1)]
        it = it+1;
        infnormdx = max(abs(dx)); % infinity norm
    end
    r = (b-A*xk); %residual
    infnormr=max(abs(r))
    it
    rho = max(eig(T)) %spectral radius, largest eigen value of T

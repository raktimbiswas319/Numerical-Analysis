n = 10;
A = full(gallery('tridiag',n,-1,2,-1));
b = zeros(n,1);
for i=1:n
    b(i) = (i^2)/(n+1)^4;
end
L = zeros(n);
x = zeros(n,1);
y = zeros(n,1);
for k=1:n
    if k==1
        L(k,k) = sqrt(A(k,k)); % L11
        L(k+1:n,k) = A(k+1:n,k)/L(k,k); % L21 to Ln1 
    else
        Lk1T = L(k,1:k-1)'; % Lk1T
        L(k,k) = sqrt(A(k,k)-Lk1T'*Lk1T); % diagonal
        L(k+1:n,k) = (A(k+1:n,k)-L(k+1:n,1:k-1)*Lk1T)/L(k,k); 
        % fill columns with each iteration
    end
end

LT=L';
%forward sub
for i=1:n
    y(i,1) = (b(i)-L(i,1:i)*y(1:i,1))./L(i,i);
end
%backward sub
x(n,1) = b(n)/(L(n,n)');
for i=n-1:-1:1
    x(i,1) = (b(i)-LT(i,i+1:n)*x(i+1:n,1))./LT(i,i)';
end
%xtrue = L'\(L\b); % x = invLT*invL*b
%x
%y
infnormr = max(abs(b-A*x))
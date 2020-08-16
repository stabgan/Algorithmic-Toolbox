def fib(n): 
  
    # The first two Fibonacci numbers 
    f0 = 0
    f1 = 1
  
    # Base case 
    if (n == 0): 
        return 0
    if (n == 1): 
        return 1
    else: 
  
        # Pisano Period for % 10 is 60 
        rem = n % 60
  
        # Checking the remainder 
        if(rem == 0): 
            return 0
  

        for i in range(rem + 1): 
            f0,f1=f1,(f0+f1)%60
  
        s = f1-1
        return(s) 
  
n = int(input())
m = 1
final = fib(n)-fib(m-1) 
print(final % 10) 
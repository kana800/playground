def obtaining_prime_list(n):
    
    prime = [True for i in range(n+1)]
    p = 2 #the first prime number
    sum = 0
    while (p*p <= n ):
        
        # If prime[p] is not changed, then it is a prime xD
        if (prime[p]==True):
            #updating the multiples of p
            for i in range(p*p,n+1,p):
                prime[i]= False
        p += 1

        for p in range(2,n):
            if prime[p]:
                print(p)
                sum += p
    return sum
print("10",obtaining_prime_list(10))
#print("2mil",obtaining_prime_list(2000000))
#print("sec",obtaining_prime_list(2000001))
#print("asdas",obtaining_prime_list(2000002))

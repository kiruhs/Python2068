name = "Alexander"
city = "Ashdod"
temp = 33

def prime_classic(n): # return True if the number is prime
    flag = False
    if n <= 1:
        return False
    # check for factors
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break
    if flag:
        #print(n, "is not a prime")
        return False
    #print(n, "is a prime")
    return True

def list_of_primes_classic(num): # create a list of all prime numbers until num
    ls = []
    for i in range(num+1):
        if prime_classic(i):
            ls.append(i)
    return ls



# Fast algorithm

def list_of_primes_fast(num): # create a list of all prime numbers until num
    """ This function is creating the list of prime numbers
    from given range and using additional function that
    checking if the number is prime. One parameter get from user and return the list"""
    ls = []
    for i in range(num+1):
        if is_prime(i):
            ls.append(i)
    return ls

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True


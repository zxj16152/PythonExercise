NUMBER_OF_PRIMES = 10000
NUMBER_OF_PRIMES_PRE_LINE = 10
count=0
number=2
print("The first 50 prime numbers are :")
while count<NUMBER_OF_PRIMES:
    isPrime=True

    divisor=2
    while divisor<=number**0.5:
        if number%divisor==0:
            isPrime = False
            break
        divisor+=1
    if isPrime:
        count+=1
        print(format(number,"10d"),end='')
        if count%NUMBER_OF_PRIMES_PRE_LINE==0:
            print()
    number+=1
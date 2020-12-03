#10001st prime
import math
import time
start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
def isPrime(num):
	if num%2 == 0:
		return False
	else:
		for k in range(3,math.ceil(math.sqrt(num)) + 1,2):
			if num%k == 0:
				return False
	return True





primes = []
i = 3;
while len(primes) != 10000:
	if isPrime(i):
		primes.append(i)
	i+=1;

print(primes[-1])
print("--- %s seconds ---" % (time.time() - start_time))
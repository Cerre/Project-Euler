#Largest prime factor
import numpy as np



def main():
	prime_factors = []
	N = 600851475143;
	for i in range(2,int(np.round(np.sqrt(N)))):
		while N%i == 0:
			N = N/i;
			prime_factors.append(i)
	print(prime_factors)



main();


	
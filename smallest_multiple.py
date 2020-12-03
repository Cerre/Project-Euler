#Smallest multiple numbers 1-20
import time

def smallest_multiple(k,number):
	for i in range(2, k+1):
		if number % i != 0:
			return False
	return True


def main():
	start_time = time.time()
	min_value = 1
	for k in range(21):
		min_value = k
		while not smallest_multiple(k, min_value):
			min_value += k
		print(min_value, k)

	print(time.time()-start_time)


main()



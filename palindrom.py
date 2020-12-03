#Largest palindrom, multiplying two 3-digit number
import math as math


found = []
for i in range(100,999):
	for j in range(100,999):
		prod = str(i*j);
		k = 0;
		while prod[k] == prod[len(prod)-1-k]:
			k = k+1;
			if k>=int(len(prod)/2):
				found.append(int(prod))
				break;

			

print(max(found))
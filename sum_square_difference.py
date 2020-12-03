#Sum square difference
import math
sum_tot = 0;
sum_2 =0;

for i in range(1,101):
	sum_tot = sum_tot + i;
	sum_2 = sum_2 + pow(i,2);
print(pow(sum_tot,2)-sum_2);
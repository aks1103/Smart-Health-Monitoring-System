import matplotlib.pyplot as plt
import csv
from collections import defaultdict

f = open('output.txt', 'r')
data = f.readlines()

x = []
y = []

k = 0
flag = 0
print(len(data))


for j in range(0,200000,2000):
	dct = defaultdict(lambda : 0 );
		
	for i in range(j,j+2000):

		if i < len(data):
			dct[data[i].rstrip()]+=1;
			# j+=1
			print("inside"+str(i))
		else:
			flag = 1
			break;
	if flag == 1:
		break
	print(j)
	y.append(max(dct, key=dct.get))
	k+=1
	x.append(k)

plt.plot(x,y, label='Loaded from file!')
axes = plt.gca()
# axes.set_ylim([2500,200000])
# axes.set_ylim([60,200])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Heart bit data')
plt.legend()
plt.show()

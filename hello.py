#print("Hello 2 Again!")





# a=1
# b=2
# c=a+b

#print(c)

d = "Hello Hello!"

#print(d)

num_list = [1, 2, 3, 4]

#print(num_list[1])


for num in num_list:
	print(num)

print(num_list[0])

name_list = ["Jon", "Marry"]

for name in name_list:
 	for num in num_list:
 		print(name + str(num))



another_list = []
for num in num_list:
	another_list.append((num +3)*2)
	print(another_list)

another_list_2 = [(num + 3)*2 for num in num_list]
print(another_list_2)


for num in another_list_2: 
	if (num > 11):
		print("Big Number:" + str(num))
	elif (num < 9):
		print("Small Number:" + str(num))
		print(another_list_2)



def myfunction(country = "Norway"):
	print("My country is " + country)

myfunction( "Nepal")


def fun(x):
	print(x**3)
fun(2)

from numpy import random
import numpy as np


arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))



def myfunction(color):
	print("my favourite color is " + color)

myfunction("Red")


def hero(a):
	print("My best hero is " + a)
hero("Sanjeev")



def myfunction(*x):
	print(x[0])
myfunction("A", "B", "C")


# for num in num_list:
#  	print((num + 3)*2)
#  	

import math

x= math.sqrt(64)

print(x)

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x,y)
plt.show()



x = [1, 2, 3, 4, 5, 6]

y = [5*(p**3) for p in x]

print(y)



def myfunction(plants):
	print("my best plant is " + plants)

myfunction("Oak")


import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()








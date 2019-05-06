import numpy as np

# def isprime(val):
# 	for n in range(2, (val // 2) + 1):
# 		if val % n != 0:
# 			if n == val // 2:
# 				return True
# 			continue
# 		else:
# 			return False
			
# def nextprime(myval):
# 	myval += 2
# 	while isprime(myval) == False:
# 		myval += 2
# 	return myval

# def max_list(list_, max_):
# 	mylist = list_
# 	while max(mylist) < max_:
# 		val_ = mylist[-1]
# 		if nextprime(val_) > max_:
# 			break
# 		else:
# 			mylist.append(nextprime(val_))
# 	return mylist

# prime_list = [1, 3, 5, 7, 11]
# verdict = max_list(prime_list, 2000000)
# print(sum(verdict))

l_odd = np.arange(1, 2000000, 2)
l3 = np.arange(0, 2000000, 3)
l5 = np.arange(0, 2000000, 5)
l7 = np.arange(0, 2000000, 7)
l11 = np.arange(0, 2000000, 11)
l13 = np.arange(0, 2000000, 13)
l17 = np.arange(0, 2000000, 17)
l19 = np.arange(0, 2000000, 19)


# lists = [l3, l5, l7, l11, l13, l17, l19]
# for list_ in lists:
# 	for val in list_:
# 		if val not in l_odd:
# 			np.append(l_odd, val)

prime_list = []
mylist = np.concatenate((l_odd, l3, l5, l7, l11, l13, l17, l19))
mylist = np.unique(mylist)
for val in mylist:
	div_list = []
	for div in range(2, int(np.sqrt(val))):
		if val % div != 0:
			if val == int(np.sqrt(val)):
				prime_list.append(val)
			continue
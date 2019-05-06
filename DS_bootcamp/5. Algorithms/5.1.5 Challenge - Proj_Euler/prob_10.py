def isprime(val):
	for n in range(2, (val // 2) + 1):
		if val % n != 0:
			if n == val // 2:
				return True
			continue
		else:
			return False
			
def nextprime(myval):
	myval += 2
	while isprime(myval) == False:
		myval += 2
	return myval

def max_list(list_, max_):
	mylist = list_
	while max(mylist) < max_:
		val_ = mylist[-1]
		if nextprime(val_) > max_:
			break
		else:
			mylist.append(nextprime(val_))
	return mylist

prime_list = [1, 3, 5, 7, 11]
verdict = max_list(prime_list, 2000000)
print(sum(verdict))
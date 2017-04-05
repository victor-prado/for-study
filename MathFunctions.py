#class MathFunctions():

def mmc(numbers):
	i = 2
	length = len(numbers)
	mmc = 1
	while (sum(numbers) != len(numbers)):
		usefull = False
		for j in range(length):
			if (numbers[j]%i == 0):
				numbers[j] = numbers[j]/i
				usefull=True

		if (usefull):
			mmc*=i
		else:
			i+=1

	return mmc

def mdc(numbers):
	i, mdc = 2, 1
	length = len(numbers)
	while (sum(numbers) != len(numbers)):
		usefull = False
		k = 0
		for j in range(length):
			if (numbers[j]%i == 0):
				numbers[j] = numbers[j]/i
				usefull = True
				k+=1

		if (not usefull):
			i+=1
		if (k == length):
			mdc*=i

	return mdc






def howold(year):
	'''
	I wanted to create a function to calculate my age based off of 
	the year I added as an argument.
	'''
	
	currentage = 26
	currentyear = 2019
	if (year > currentyear):
		add = year - currentyear
		futureage = currentage + add
		print("In the year {} I will be {}".format(year,futureage))
		print("\n")
	elif(year < currentyear):
		subtract = currentyear-year
		pastage = currentage-subtract
		print("In the year {} I was {}".format(year,pastage))
		print("\n")

#Testing fuction
howold(2020)
howold(2030)
howold(1992)
howold(1988)
howold(3001)
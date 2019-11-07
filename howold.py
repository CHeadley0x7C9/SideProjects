

def howold(year):
	'''
	I wanted to create a function to calculate my age based off of 
	the year I added as an argument. 
	'''
	try:
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
	except TypeError:
		print("ERROR: Please use a year as an argument!")
	

#Testing function
howold(2020)
howold(2030)
howold(1992)
howold(1988)
howold(3001)
howold("pink")

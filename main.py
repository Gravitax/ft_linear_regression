def	get_thetas():
	theta0, theta1, mean_error = 0., 0., 0.
	try:
		with open("theta", 'r') as f:
			value = f.readlines()
			if len(value) != 3:
				print("[[ Error: invalid theta file. Run training.py ]]")
				exit(1)
			theta0 = value[0][value[0].index('=') + 1:-1]
			theta1 = value[1][value[1].index('=') + 1:-1]
			mean_error = value[2][value[2].index('=') + 1:-1]
			try:
				theta0 = float(theta0)
				theta1 = float(theta1)
				mean_error = float(mean_error)
			except ValueError:
				print("[[ Error: invalid theta variables in theta file. Run training.py ]]")
				theta0, theta1, mean_error = 0., 0., 0.
	except Exception:
		print("[[ Error: invalid theta file. Run training.py ]]")
	return theta0, theta1, mean_error

def	get_mileage():
	while 1:
		try:
			mileage = float(input("Enter a mileage: "))
			if mileage < 0:
				print("[[ Mileage can't be negative ]]")
				continue
			break
		except ValueError:
			print("[[ Invalid mileage ]]")
	return mileage

if __name__ == "__main__":
	theta0, theta1, mean_error = get_thetas()
	mileage = get_mileage()
	result = theta0 + (theta1 * mileage)
	print("Estimated price: " + str(int(result)) + " €")
	if mean_error and result:
		precision = 100 - 100 * (mean_error / result)
		if precision < 0 or precision > 100: precision = 0
		print("Mean error: " + str(int(mean_error)) + " €")
		print("Precision: " + str(int(precision)) + " %")

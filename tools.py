from csv import reader


# Load a CSV file
def	load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			if not len(row[0]) or not len(row[1]):
				print("[[ Error: invalid csv file ]]")
				exit(1)
			try:
				# Convert string column to float
				i = 0
				for elt in row:
					row[i] = float(row[i])
					i += 1
			except ValueError:
				continue
			dataset.append(row)
	return dataset

def	save_in_file(theta0, theta1, mean_error):
	# saving theta0 and theta1 in a file
	if theta0 and theta1:
		print("theta0: " + str(theta0))
		print("theta1: " + str(theta1))
		if not mean_error: mean_error = 0.0
		print("mean_error: " + str(mean_error))
		try:
			theta = open("theta", 'w')
			theta.write("theta0={}\ntheta1={}\nmean_error={}\n".format(theta0, theta1, mean_error))
			theta.close()
		except Exception:
			print("[[ Error with theta file ]]")
	else:
		print("[[ Error during training ]]")

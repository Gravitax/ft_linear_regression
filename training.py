import matplotlib.pyplot as plt
from csv import reader

from training_precision import evaluate_algorithm


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
	return (dataset)

# Calculate the mean value of a list of numbers
# mean(x) = sum(x) / count(x)
def	mean(values):
	return (sum(values) / float(len(values)))

# Calculate the variance of a list of numbers
# variance = sum( (x - mean(x))^2 )
def	variance(values, mean):
	return (sum([(x - mean) ** 2 for x in values]))

def	renderGraph(theta0, theta1, km, price):
	ax.clear()
	ax.plot(km, price, 'o', color = "#000000")
	lineX = [0, 260000]
	lineY = [theta0 + (theta1 * 0), theta0 + (theta1 * 260000)]
	ax.plot(lineX, lineY, linestyle = "solid", color = "#ff0000", linewidth = 2.0)
	plt.pause(0.001)

# Calculate coefficients
# THETA1 = sum((x(i) - mean(x)) * (y(i) - mean(y))) / sum( (x(i) - mean(x))^2 )
# THETA1 = covariance(x, y) / variance(x)
# THETA0 = mean(y) - THETA1 * mean(x)
def	coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]

	# Calculate covariance between x and y
	# covariance = sum((x(i) - mean(x)) * (y(i) - mean(y)))
	mean_x, mean_y = mean(x), mean(y)
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
		theta1 = covar / variance(x, mean_x)
		theta0 = mean_y - theta1 * mean_x
		renderGraph(theta0, theta1, x, y)
	return ([theta0, theta1])

def	save_in_file(theta0, theta1, rmse):
	# saving theta0 and theta1 in a file
	if theta0 and theta1 and rmse:
		print("theta0: " + str(theta0))
		print("theta1: " + str(theta1))
		print("rmse: " + str(rmse))
		try:
			theta = open("theta", 'w')
			theta.write("theta0={}\ntheta1={}\nrmse={}\n".format(theta0, theta1, rmse))
			theta.close()
		except Exception:
			print("[[ Error with theta file ]]")
	else:
		print("[[ Error during training ]]")

# Simple linear regression algorithm
def	simple_linear_regression(train, test):
	predictions = list()
	theta0, theta1 = coefficients(train)
	for row in test:
		yhat = theta0 + theta1 * row[0]
		predictions.append(yhat)
	return (predictions)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

if __name__ == "__main__":
	if not ax:
		print("[[ Error ]]")
		exit(1)
	dataset = load_csv("data.csv")
	if len(dataset) < 2:
		print("[[ Error: failed to load csv file ]]")
		exit(1)
	theta0, theta1 = coefficients(dataset)

	plt.ioff()
	plt.show()

	# A training dataset of 70% of the data is used to prepare the model and predictions are made on the remaining 30%.
	split = 0.7
	rmse = evaluate_algorithm(dataset, simple_linear_regression, split)
	save_in_file(theta0, theta1, rmse)

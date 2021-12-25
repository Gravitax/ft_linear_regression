import matplotlib.pyplot as plt

from math import sqrt

from tools import load_csv, save_in_file


def	renderGraph(theta0, theta1, km, price):
	ax.clear()
	ax.plot(km, price, 'o', color = "#000000")
	lineX = [0, 260000]
	lineY = [theta0 + (theta1 * 0), theta0 + (theta1 * 260000)]
	ax.plot(lineX, lineY, color = "#ff0000")
	plt.pause(0.001)

# Calculate the mean value of a list of numbers
# mean(x) = sum(x) / count(x)
def	mean(values):
	return sum(values) / float(len(values))

# Calculate the variance of a list of numbers
# variance = sum( (x - mean(x))^2 )
def	variance(values, mean):
	return sum([(x - mean) ** 2 for x in values])

# Calculate coefficients
# THETA1 = sum((x(i) - mean(x)) * (y(i) - mean(y))) / sum( (x(i) - mean(x))^2 )
# THETA1 = covariance(x, y) / variance(x)
# THETA0 = mean(y) - THETA1 * mean(x)
def	coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	mean_x, mean_y = mean(x), mean(y)
	var = variance(x, mean_x)
	# Calculate covariance between x and y
	# covariance = sum((x(i) - mean(x)) * (y(i) - mean(y)))
	covariance = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
		theta1 = covar / var
		theta0 = mean_y - theta1 * mean_x
		renderGraph(theta0, theta1, x, y)
	return [theta0, theta1]

# Simple linear regression algorithm
def	simple_linear_regression(dataset):
	predictions = list()
	theta0, theta1 = coefficients(dataset)
	for row in dataset:
		yhat = theta0 + theta1 * row[0]
		predictions.append(yhat)
	return predictions, theta0, theta1

# Calculate root mean squared error
def	rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return (sqrt(mean_error))

# Evaluate an algorithm
def evaluate_algorithm(dataset, algorithm):
	predicted, theta0, theta1 = algorithm(dataset)
	actual = [row[1] for row in dataset]
	return (theta0, theta1, rmse_metric(actual, predicted))

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

if __name__ == "__main__":
	dataset = load_csv("data.csv")
	if len(dataset) < 2:
		print("[[ Error: failed to load csv file ]]")
		exit(1)
	theta0, theta1, mean_error = evaluate_algorithm(dataset, simple_linear_regression)
	save_in_file(theta0, theta1, mean_error)
	plt.ioff()
	plt.show()

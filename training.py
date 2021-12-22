# Standalone simple linear regression example
from math import sqrt
from csv import reader
from random import seed
from random import randrange

# Load a CSV file
def	load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row or row[0] == "km":
				continue
			dataset.append(row)
	return (dataset)

# Convert string column to float
def	str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
 
# Split a dataset into a train and test set
def	train_test_split(dataset, split):
	train = list()
	train_size = split * len(dataset)
	dataset_copy = list(dataset)
	while len(train) < train_size:
		index = randrange(len(dataset_copy))
		train.append(dataset_copy.pop(index))
	return (train, dataset_copy)

# Calculate root mean squared error
def	rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return (sqrt(mean_error))

# Evaluate an algorithm using a train/test split
def evaluate_algorithm(dataset, algorithm, split, *args):
	# train, test = train_test_split(dataset, split)
	test_set = list()
	for row in dataset:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)
	predicted = algorithm(dataset, test_set)
	print(predicted)
	actual = [row[-1] for row in dataset]
	rmse = rmse_metric(actual, predicted)
	return (rmse)

# Calculate the mean value of a list of numbers
def	mean(values):
	return (sum(values) / float(len(values)))

# Calculate the variance of a list of numbers
def	variance(values, mean):
	return (sum([(x - mean) ** 2 for x in values]))

# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return (covar)

# Calculate coefficients
def	coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	mean_x, mean_y = mean(x), mean(y)
	b1 = covariance(x, mean_x, y, mean_y) / variance(x, mean_x)
	b0 = mean_y - b1 * mean_x
	return ([b0, b1])

# Simple linear regression algorithm
def	simple_linear_regression(train, test):
	predictions = list()
	b0, b1 = coefficients(train)
	for row in test:
		yhat = b0 + b1 * row[0]
		predictions.append(yhat)
	return (predictions)

# Simple linear regression on insurance dataset
seed(1)

# load and prepare data
filename = "data_set.csv"
dataset = load_csv(filename)
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)

# dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
print(dataset)

# evaluate algorithm
split	= 0.9
rmse	= evaluate_algorithm(dataset, simple_linear_regression, split)
print("RMSE: %f" % (rmse))


import os

os.environ["THETA_ZERO"]	= "wallah"
os.environ["THETA_ONE"]		= "pq ça marche pas"

# kms		= []
# prices	= []

# for elt in dataset:
# 	if type(elt[0]) == str:
# 		continue
# 	kms.append(elt[0])
# 	prices.append(elt[1])

# print(kms)
# print(prices)

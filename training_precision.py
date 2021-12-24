from math import sqrt
from random import randrange


# Calculate root mean squared error
def	rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return (sqrt(mean_error))

# Split a dataset into a train and test set
def	train_test_split(dataset, split):
	train = list()
	train_size = split * len(dataset)
	dataset_copy = list(dataset)
	while len(train) < train_size:
		index = randrange(len(dataset_copy))
		train.append(dataset_copy.pop(index))
	return (train, dataset_copy)

# Evaluate an algorithm using a train/test split
def evaluate_algorithm(dataset, algorithm, split):
	train, test = train_test_split(dataset, split)
	test_set = list()
	for row in test:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)
	predicted, theta0, theta1 = algorithm(train, test_set)
	actual = [row[-1] for row in test]
	return (theta0, theta1, rmse_metric(actual, predicted))

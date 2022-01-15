from tools import load_csv, save_in_file


learning_rate = 0.01

def hypothesis(theta0, theta1, mileages):
    return theta0 + theta1 * mileages

def sum_theta0(theta0, theta1, mileages, prices, m):
	value = 0.
	for i in range(m):
		value += hypothesis(theta0, theta1, mileages[i]) - prices[i]
	return value

def sum_theta1(theta0, theta1, mileages, prices, m):
	value = 0.
	for i in range(m):
		value += (hypothesis(theta0, theta1, mileages[i]) - prices[i]) * mileages[i]
	return value

def gradient_descent(x, y, i):
	theta0, theta1 = 0., 0.
	m = len(x)
	for j in range(i):
		tmp_t0 = sum_theta0(theta0, theta1, x, y, m) / m
		tmp_t1 = sum_theta1(theta0, theta1, x, y, m) / m
		theta0 = theta0 - learning_rate * tmp_t0
		theta1 = theta1 - learning_rate * tmp_t1
	min, max = dataset_minmax(dataset)
	return denormalize(theta0, min, max), theta1

def	dataset_minmax(dataset):
	arr1 = [row[0] for row in dataset]
	arr2 = [row[1] for row in dataset]
	min = 999999999
	max = 0
	for i in range(len(arr1)):
		if int(arr1[i]) < min: min = arr1[i]
		if int(arr1[i]) > max: max = arr1[i]
	for i in range(len(arr2)):
		if int(arr2[i]) < min: min = arr2[i]
		if int(arr2[i]) > max: max = arr2[i]
	return min, max

def	denormalize(value, min, max):
	return value * (max - min) + min

def	normalize(value, min, max):
	return (value - min) / (max - min)

def	get_mileages(dataset):
	min, max = dataset_minmax(dataset)
	return [normalize(row[0], min, max) for row in dataset]

def	get_prices(dataset):
	min, max = dataset_minmax(dataset)
	return [normalize(row[1], min, max) for row in dataset]

if __name__ == "__main__":
	dataset = load_csv("data.csv")
	mileages = get_mileages(dataset)
	prices = get_prices(dataset)
	theta0, theta1 = gradient_descent(mileages, prices, 10000)
	save_in_file(theta0, theta1, 0.)

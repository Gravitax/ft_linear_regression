from tools import load_csv, save_in_file


learning_rate = 0.01

def	dataset_minmax(dataset):
	arr1 = [row[0] for row in dataset]
	arr2 = [row[1] for row in dataset]
	min = 999999999
	max = 0
	for i in range(len(arr1)):
		if int(arr1[i]) < min: min = arr1[i]
		elif int(arr1[i]) > max: max = arr1[i]
	for i in range(len(arr2)):
		if int(arr2[i]) < min: min = arr2[i]
		elif int(arr2[i]) > max: max = arr2[i]
	return min, max

def	denormalize(value, min, max):
	return value * (max - min) + min

def	normalize(value, min, max):
	return (value - min) / (max - min)

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

def gradient_descent(dataset, iterations):
	min, max = dataset_minmax(dataset)
	x = [normalize(row[0], min, max) for row in dataset]
	y = [normalize(row[1], min, max) for row in dataset]
	m = len(x)
	theta0, theta1 = 0., 0.
	for i in range(iterations):
		tmp_t0 = sum_theta0(theta0, theta1, x, y, m) / m
		tmp_t1 = sum_theta1(theta0, theta1, x, y, m) / m
		theta0 -= learning_rate * tmp_t0
		theta1 -= learning_rate * tmp_t1
	return denormalize(theta0, min, max), theta1

if __name__ == "__main__":
	dataset = load_csv("data.csv")
	theta0, theta1 = gradient_descent(dataset, 10000)
	save_in_file(theta0, theta1, 0.)

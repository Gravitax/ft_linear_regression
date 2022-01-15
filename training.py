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

def gradient_descent(mileages, prices, i):
	theta0, theta1 = 0., 0.
	m = len(mileages)
	for j in range(i):
		tmp_t0 = sum_theta0(theta0, theta1, mileages, prices, m) / m
		tmp_t1 = sum_theta1(theta0, theta1, mileages, prices, m) / m
		theta0 = theta0 - learning_rate * tmp_t0
		theta1 = theta1 - learning_rate * tmp_t1
	return theta0 * 1000000, theta1

if __name__ == "__main__":
	dataset = load_csv("data.csv")
	mileages = [row[0] / 1000000 for row in dataset]
	prices = [row[1] / 1000000 for row in dataset]
	theta0, theta1 = gradient_descent(mileages, prices, 100000)
	save_in_file(theta0, theta1, 0.)

from tools import load_csv, save_in_file


learning_rate = 0.0001

def estimator(t0, t1, mileages):
    return t0 + (t1 * mileages)

def sumTheta0(t0, t1, mileages, prices, length):
    val = 0
    for i in range(length):
        val += estimator(t0, t1, mileages[i]) - prices[i]
    return val

def sumTheta1(t0, t1, mileages, prices, length):
    val = 0
    for i in range(length):
        val += (estimator(t0, t1, mileages[i]) - prices[i]) * mileages[i]
    return val

def trainer(mileages, prices):
    t0, t1 = 0., 0.
    length = len(mileages)
    i = 0
    while i < 10:
        tmp0 = sumTheta0(t0, t1, mileages, prices, length) / length
        tmp1 = sumTheta1(t0, t1, mileages, prices, length) / length
        print(tmp0)
        print(tmp1)
        print("-----")
        t0 -= (learning_rate * tmp0)
        t1 -= (learning_rate * tmp1)
        print(t0)
        print(t1)
        print("==========")
        if abs(learning_rate * tmp0) < learning_rate:
            break
        i += 1
    return t0, t1

if __name__ == "__main__":
    dataset = load_csv("data.csv")
    if len(dataset) < 2:
        print("[[ Error: failed to load csv file ]]")
        exit(1)
    t0, t1 = trainer([row[0] for row in dataset], [row[1] for row in dataset])
    save_in_file(t0, t1, 0.)

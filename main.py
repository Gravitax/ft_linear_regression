if __name__ == "__main__":
    theta0, theta1 = 0., 0.
    while 1:
        try:
            mileage = float(input("Enter a mileage: "))
            if mileage < 0:
                print("[[ Mileage can't be negative ]]")
                continue
            break
        except ValueError:
            print("[[ Invalid mileage ]]")
    try:
        with open("theta", 'r') as f:
            value = f.readlines()
            theta0 = value[0][value[0].index('=') + 1:-1]
            theta1 = value[1][value[1].index('=') + 1:-1]
            try:
                theta0 = float(theta0)
                theta1 = float(theta1)
            except ValueError:
                print("[[ Error: invalid theta variables in theta file. Run training.py ]]")
                theta0, theta1 = 0., 0.
    except Exception:
        print("[[ Error: no theta file. Run training.py ]]")
    result = theta0 + (theta1 * mileage)
    print("Estimated price:")
    print(str(int(result)) + " €")

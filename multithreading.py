import concurrent.futures
import time
import numpy as np


def find_hypotenuse_with_theading() -> tuple:

    cathetus_1 = float(input("Input the first cathetus: "))
    cathetus_2 = float(input("Input the second cathetus: "))

    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=12) as executor:

        cathetus_square_1 = executor.submit(np.power, cathetus_1, 2)
        cathetus_square_2 = executor.submit(np.power, cathetus_2, 2)

        hypotenuse = executor.submit(np.power, cathetus_square_1.result() + cathetus_square_2.result(), 0.5)

        print("--- %.5f seconds ---" % (time.time() - start_time))

    return "%.3f" % hypotenuse.result(), "%.3f" % np.power(cathetus_1, 2), "%.3f" % np.power(cathetus_2, 2)


def find_hypotenuse_with_sleep() -> tuple:
    cathetus_1 = float(input("Input the first cathetus: "))
    cathetus_2 = float(input("Input the second cathetus: "))

    start_time = time.time()
    time.sleep(2)

    cathetus_square_1 = np.power(cathetus_1, 2)
    cathetus_square_2 = np.power(cathetus_2, 2)

    hypotenuse = np.power(cathetus_square_1 + cathetus_square_2, 0.5)

    print("--- %.5f seconds ---" % (time.time() - start_time))

    return "%.3f" % hypotenuse, "%.3f" % np.power(cathetus_1, 2), "%.3f" % np.power(cathetus_2, 2)


def find_hypotenuse() -> tuple:
    cathetus_1 = float(input("Input the first cathetus: "))
    cathetus_2 = float(input("Input the second cathetus: "))

    start_time = time.time()

    cathetus_square_1 = np.power(cathetus_1, 2)
    cathetus_square_2 = np.power(cathetus_2, 2)

    hypotenuse = np.power(cathetus_square_1 + cathetus_square_2, 0.5)

    print("--- %.5f seconds ---" % (time.time() - start_time))

    return "%.3f" % hypotenuse, "%.3f" % np.power(cathetus_1, 2), "%.3f" % np.power(cathetus_2, 2)


if __name__ == "__main__":
    print(find_hypotenuse_with_theading())
    print()
    print(find_hypotenuse_with_sleep())
    print()
    print(find_hypotenuse())

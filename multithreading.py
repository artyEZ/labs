import concurrent.futures
import time
import numpy as np


def find_hypotenuse() -> tuple:

    cathetus_1 = float(input("Input the first cathetus: "))
    cathetus_2 = float(input("Input the second cathetus: "))

    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:

        cathetus_square_1 = executor.submit(np.power, cathetus_1, 2)
        cathetus_square_2 = executor.submit(np.power, cathetus_2, 2)

        hypotenuse = executor.submit(np.power, cathetus_square_1.result() + cathetus_square_2.result(), 0.5)

        print("--- %s seconds ---" % (time.time() - start_time))

    return '%.3f' % hypotenuse, np.power(cathetus_1, 2), np.power(cathetus_2, 2)



    if __name__ == "__main__":



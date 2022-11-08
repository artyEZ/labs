import concurrent.futures
import time
import numpy as np
import argparse


def find_hypotenuse_with_theading() -> tuple:

    parser = argparse.ArgumentParser(description="Find hypotenuse")
    parser.add_argument("cathetus_square_1", type=float, help="Input first cathetus: ")
    parser.add_argument("cathetus_square_2", type=float, help="Input second cathetus: ")
    args = parser.parse_args()

    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=12) as executor:

        cathetus_square_1 = executor.submit(np.power, args.cathetus_square_1, 2)
        cathetus_square_2 = executor.submit(np.power, args.cathetus_square_2, 2)

        hypotenuse = executor.submit(np.power, cathetus_square_1.result() + cathetus_square_2.result(), 0.5)

        print("--- %.5f seconds ---" % (time.time() - start_time))

    return "%.3f" % hypotenuse.result(), "%.3f" % np.power(args.cathetus_square_1, 2), \
           "%.3f" % np.power(args.cathetus_square_2, 2)


def find_hypotenuse_with_sleep() -> tuple:
    parser = argparse.ArgumentParser(description="Find hypotenuse")
    parser.add_argument("cathetus_square_1", type=float, help="Input first cathetus: ")
    parser.add_argument("cathetus_square_2", type=float, help="Input second cathetus: ")
    args = parser.parse_args()

    start_time = time.time()
    time.sleep(2)

    cathetus_square_1 = np.power(args.cathetus_1, 2)
    cathetus_square_2 = np.power(args.cathetus_2, 2)

    hypotenuse = np.power(cathetus_square_1 + cathetus_square_2, 0.5)

    print("--- %.5f seconds ---" % (time.time() - start_time))

    return "%.3f" % hypotenuse, "%.3f" % np.power(args.cathetus_1, 2), "%.3f" % np.power(args.cathetus_2, 2)


def find_hypotenuse() -> tuple:
    parser = argparse.ArgumentParser(description="Find hypotenuse")
    parser.add_argument("cathetus_square_1", type=float, help="Input first cathetus: ")
    parser.add_argument("cathetus_square_2", type=float, help="Input second cathetus: ")
    args = parser.parse_args()

    start_time = time.time()

    cathetus_square_1 = np.power(args.cathetus_1, 2)
    cathetus_square_2 = np.power(args.cathetus_2, 2)

    hypotenuse = np.power(cathetus_square_1 + cathetus_square_2, 0.5)

    print("--- %.5f seconds ---" % (time.time() - start_time))

    return "%.3f" % hypotenuse, "%.3f" % np.power(args.cathetus_1, 2), "%.3f" % np.power(args.cathetus_2, 2)


if __name__ == "__main__":
    print(find_hypotenuse_with_theading())

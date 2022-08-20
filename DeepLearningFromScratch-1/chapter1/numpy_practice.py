import numpy as np


def numpy_array_tutorial() -> None:
    x: np.ndarray = np.array([1, 2, 3])
    print(x)  # [1 2 3]
    print(type(x))  # <class 'numpy.ndarray'>

    y: np.ndarray = np.array([2, 4, 6])
    print(x + y)  # [3 6 9]
    print(x * y)  # [2 8 18]

    A: np.ndarray = np.array([[1, 2], [3, 4]])
    print(A.shape)  # (2, 2)
    B: np.ndarray = np.array([[5, 6], [7, 8]])
    print(A + B)  # [[ 6  8], [10 12]]
    print(A * B)  # [[ 5 12], [21 32]]

    print(A.flatten())  # [1 2 3 4]


def main() -> None:
    numpy_array_tutorial()


if __name__ == "__main__":
    main()

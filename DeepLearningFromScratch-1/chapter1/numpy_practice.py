import numpy as np


def numpy_array_tutorial() -> None:
    x: np.ndarray = np.array([1, 2, 3])
    print(x)  # [1 2 3]
    print(type(x))  # <class 'numpy.ndarray'>


def main() -> None:
    numpy_array_tutorial()


if __name__ == "__main__":
    main()

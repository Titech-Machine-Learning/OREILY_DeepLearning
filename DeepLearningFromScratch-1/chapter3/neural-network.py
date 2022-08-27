import numpy as np

from functions import sygmoid


def main() -> None:
    def identity_function(x):  # type: ignore
        return x

    # X: 入力値 input values  2 x 1
    X: np.ndarray = np.array([1.0, 0.5])
    # W: 重み weights 2 x 3
    W: np.ndarray = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    # B: バイアス bias 3 x 1
    B: np.ndarray = np.array([0.1, 0.2, 0.3])

    # 行列の計算の際は、サイズをコメントに書いておくなどして Run Timeエラーを防ぐ工夫をした方が良い
    print(f"X = {X} , size of X = {X.shape}")
    print(f"W = {W} , size of W = {W.shape}")
    print(f"B = {B} , size of B = {B.shape}")

    # 第1層の計算
    A1: np.ndarray = np.dot(X, W) + B
    print(f"A1 = {A1} , size of A1 = {A1.shape}")

    Z1: np.ndarray = sygmoid(A1)  # 3 x 1
    print(f"Z1 = {Z1} , size of Z1 = {Z1.shape}")

    # 第2層の計算
    W2: np.ndarray = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])  # 3 x 2
    B2: np.ndarray = np.array([0.1, 0.2])  # 2 x 1

    A2: np.ndarray = np.dot(Z1, W2) + B2
    Z2: np.ndarray = sygmoid(A2)

    # 第3層の計算 (出力層へ)
    W3: np.ndarray = np.array([[0.1, 0.3], [0.2, 0.4]])  # 2 x 2
    B3: np.ndarray = np.array([0.1, 0.2])  # 2 x 1

    A3: np.ndarray = np.dot(Z2, W3) + B3
    Y: np.ndarray = identity_function(A3)

    print(f"Y = {Y} , size of Y = {Y.shape}")


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt  # type: ignore
import numpy as np


def step_function(x):  # type: ignore
    return np.array(x > 0, dtype=np.int64)


def sygmoid(x):  # type: ignore
    return 1 / (1 + np.exp(-x))


def relu(x):  # type: ignore
    return np.maximum(0, x)


def step_function_graph() -> None:
    x: np.ndarray = np.arange(-5.0, 5.0, 0.1)
    y: np.ndarray = step_function(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # y軸の範囲を指定
    plt.show()


def sygmoid_graph() -> None:
    x: np.ndarray = np.arange(-5.0, 5.0, 0.1)
    y: np.ndarray = sygmoid(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # y軸の範囲を指定
    plt.show()


def relu_graph() -> None:
    x: np.ndarray = np.arange(-5.0, 5.0, 0.1)
    y: np.ndarray = relu(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 5.1)  # y軸の範囲を指定
    plt.show()


def softmax(x):  # type: ignore
    constant = np.max(x)
    exp_x = np.exp(x - constant)  # overflow 対策
    sum_exp_x = np.sum(exp_x)
    return exp_x / sum_exp_x


def main() -> None:
    # step 関数の挙動を説明するためのコード
    x: np.ndarray = np.array([-1.0, 1.0, 2.0])
    print(x)
    y = x > 0
    print("y = ", type(y), end="")
    print(y)
    # np.ndarray(float64) ->  np.ndarray(bool)

    # ステップ関数
    step_function_graph()

    # シグモイド関数の挙動説明

    # numpy配列についても正しく計算されることを確かめる
    x = np.array([-1.0, 1.0, 2.0])
    print("sygmoid(x) = ", type(sygmoid(x)), end="")
    print(sygmoid(x))
    # np.ndarray(float64) ->  np.ndarray(float64)
    # sygmoid(x) =  <class 'numpy.ndarray'>[0.26894142 0.73105858 0.88079708]

    # シグモイド関数
    sygmoid_graph()

    # ReLU関数
    relu_graph()


if __name__ == "__main__":
    main()

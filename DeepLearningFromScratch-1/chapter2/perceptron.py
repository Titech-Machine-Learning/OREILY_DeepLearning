import numpy as np


def AND_perceptron(x1: int, x2: int) -> int:
    """
    ANDゲートのパーセプトロン
    """
    w1, w2, theta = 0.5, 0.5, 0.7
    perceptron_value: float = x1 * w1 + x2 * w2
    if perceptron_value <= theta:
        return 0
    else:
        return 1


def check_AND_perceptron(x1: int, x2: int) -> None:
    """
    ANDゲートのパーセプトロンをテストする
    """
    print(f"{x1} AND {x2} = {AND_perceptron(x1, x2)}")


print("AND_perceptron")
check_AND_perceptron(0, 0)
check_AND_perceptron(1, 0)
check_AND_perceptron(0, 1)
check_AND_perceptron(1, 1)


def bias_AND_perceptron(x1: int, x2: int) -> int:
    """
    バイアス付きANDゲートのパーセプトロン
    """
    x: np.ndarray = np.array([x1, x2])
    w: np.ndarray = np.array([0.5, 0.5])
    b: float = -0.7

    perceptron_value: float = np.sum(x * w) + b
    if perceptron_value <= 0:
        return 0
    else:
        return 1


# b: bias バイアスはニューロンの発火のしやすさを表す


def check_bias_AND_perceptron(x1: int, x2: int) -> None:
    print(f"{x1} AND {x2} = {bias_AND_perceptron(x1, x2)}")


print("\nbias_AND_perceptron")
check_bias_AND_perceptron(0, 0)
check_bias_AND_perceptron(1, 0)
check_bias_AND_perceptron(0, 1)
check_bias_AND_perceptron(1, 1)


# NAND, OR
def NAND_perceptron(x1: int, x2: int) -> int:
    """
    NANDゲートのパーセプトロン
    """
    x: np.ndarray = np.array([x1, x2])
    w: np.ndarray = np.array([-0.5, -0.5])
    b: float = 0.7

    perceptron_value: float = np.sum(x * w) + b
    if perceptron_value <= 0:
        return 0
    else:
        return 1


def OR_perceptron(x1: int, x2: int) -> int:
    """
    ORゲートのパーセプトロン
    """
    x: np.ndarray = np.array([x1, x2])
    w: np.ndarray = np.array([0.5, 0.5])
    b: float = -0.2

    perceptron_value: float = np.sum(x * w) + b
    if perceptron_value <= 0:
        return 0
    else:
        return 1


print("\nNAND_perceptron")
print(f"0 NAND 0 = {NAND_perceptron(0, 0)}")
print(f"1 NAND 0 = {NAND_perceptron(1, 0)}")
print(f"0 NAND 1 = {NAND_perceptron(0, 1)}")
print(f"1 NAND 1 = {NAND_perceptron(1, 1)}")

print("\nOR_perceptron")
print(f"0 OR 0 = {OR_perceptron(0, 0)}")
print(f"1 OR 0 = {OR_perceptron(1, 0)}")
print(f"0 OR 1 = {OR_perceptron(0, 1)}")
print(f"1 OR 1 = {OR_perceptron(1, 1)}")

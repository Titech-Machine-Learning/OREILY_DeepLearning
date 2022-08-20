import matplotlib.pyplot as plt  # type: ignore
import numpy as np

x: np.ndarray = np.arange(0, 6, 0.1)
y: np.ndarray = np.sin(x)

plt.plot(x, y)
plt.show()

y_sin: np.ndarray = np.sin(x)
y_cos: np.ndarray = np.cos(x)

plt.plot(x, y_sin, label="sin", color="blue")
plt.plot(x, y_cos, label="cos", color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()  # 凡例を表示する
plt.show()

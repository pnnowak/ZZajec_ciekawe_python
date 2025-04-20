import numpy as np
import matplotlib.pyplot as plt


# dane: y = 3x + szum
np.random.seed(0)
x = np.linspace(1, 10, 20)
y = 3 * x + np.random.normal(0, 1, size=len(x))

x_centered = x - np.mean(x)
y_centered = y - np.mean(y)

def mse_loss(a, x, y):
    y_pred = a * x
    return np.mean((y_pred - y) ** 2)

# Gradient funkcji błędu względem a
def mse_gradient(a, x, y):
    n = len(x)
    return (2/n) * np.sum(x * (a * x - y))

a = 0
lr = 0.01
tolerance = 1e-6
max_iter = 1000

for i in range(max_iter):
    grad = mse_gradient(a, x_centered, y_centered)
    a_new = a - lr * grad
    print(f"Iteracja {i}: a: {a_new}, wartosc funkcji celu: {mse_gradient(a_new, x_centered, y_centered)}")

    if abs(mse_gradient(a_new, x_centered, y_centered) - mse_gradient(a, x_centered, y_centered)) < tolerance:
        print(f"Zbieżność osiągnięta po {i+1} iteracjach.")
        break

    a = a_new

print(f"\nWynik optymalizacji numerycznej: a = {a}")

a_analytical = np.dot(x_centered, y_centered) / np.dot(x_centered, x_centered)
print(f"Wynik analityczny: a = {a_analytical}")

plt.plot(x, a * x, color='red', label="Regresja (numeryczna)")
plt.plot(x, a_analytical * x, color='green', linestyle='--', label="Regresja (analityczna)")
plt.xlabel("x ")
plt.ylabel("y")
plt.title("Regresja liniowa: własna optymalizacja vs analityczna")
plt.legend()
plt.grid(True)
plt.show()
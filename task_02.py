import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


# Визначення функції f(x)
def f(x: float) -> float:
    """Функція для обчислення x^2."""
    return x**2


# Межі інтегрування
a: float = 0
b: float = 2


def monte_carlo_integration(f, a: float, b: float, n_points: int = 10000) -> float:
    """
    Обчислення визначеного інтегралу методом Монте-Карло.

    Args:
        f: функція для інтегрування
        a: нижня межа інтегрування
        b: верхня межа інтегрування
        n_points: кількість випадкових точок

    Returns:
        Оцінка інтегралу.
    """
    x_random = np.random.uniform(a, b, n_points)
    y_random = np.random.uniform(0, f(b), n_points)

    under_curve = y_random < f(x_random)
    area = (b - a) * f(b)  # Площа прямокутника
    integral = np.sum(under_curve) / n_points * area
    return integral


# Кількість точок для методу Монте-Карло
n_points = 10000

# Обчислення інтегралу методом Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b, n_points)
print(f"Інтеграл методом Монте-Карло: {monte_carlo_result}")

# Перевірка за допомогою SciPy (функція quad)
result, error = spi.quad(f, a, b)
print(f"Аналітичний інтеграл (quad): {result}, похибка: {error}")

# Оцінка похибки Монте-Карло
monte_carlo_error = abs(monte_carlo_result - result)
print(f"Похибка методу Монте-Карло: {monte_carlo_error}")

# Візуалізація результату
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
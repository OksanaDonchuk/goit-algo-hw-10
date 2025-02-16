import pulp


def optimize_production() -> None:
    """
    Оптимізує виробництво лимонаду та фруктового соку для максимального використання ресурсів.
    Використовує лінійне програмування (PuLP).
    """

    # Створення моделі максимізації
    model = pulp.LpProblem(name="production-optimization", sense=pulp.LpMaximize)

    # Оголошення змінних (кількість одиниць лимонаду та фруктового соку)
    lemonade = pulp.LpVariable(name="lemonade", lowBound=0, cat="Integer")
    fruit_juice = pulp.LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

    # Цільова функція: максимізація загальної кількості напоїв
    model += lemonade + fruit_juice

    # Обмеження на ресурси
    model += (2 * lemonade + 1 * fruit_juice <= 100), "Water_Constraint"
    model += (1 * lemonade <= 50), "Sugar_Constraint"
    model += (1 * lemonade <= 30), "Lemon_Juice_Constraint"
    model += (2 * fruit_juice <= 40), "Fruit_Puree_Constraint"

    # Розв’язання задачі
    model.solve(pulp.PULP_CBC_CMD())

    # Виведення результатів
    print(f"Максимальна кількість лимонаду: {lemonade.varValue}")
    print(f"Максимальна кількість фруктового соку: {fruit_juice.varValue}")
    print(f"Загальна кількість напоїв: {lemonade.varValue + fruit_juice.varValue}")
    print(f"Статус: {pulp.LpStatus[model.status]}")


if __name__ == "__main__":
    optimize_production()
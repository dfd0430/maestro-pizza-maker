
from maestro_pizza_maker.pizza import Pizza
from maestro_pizza_maker.pizza_menu import PizzaMenu
import numpy as np


def taste_at_risk_pizza(pizza: Pizza, quantile: float) -> float:
    tar_value = np.quantile(pizza.taste, quantile)
    return tar_value


def taste_at_risk_menu(menu: PizzaMenu, quantile: float) -> float:
    taste_array = np.array([])

    for pizza in menu.pizzas:
        taste_array = np.append(taste_array, pizza.taste)
    tar_value = np.quantile(taste_array, quantile)

    return float(tar_value)


def conditional_taste_at_risk_pizza(pizza: Pizza, quantile: float) -> float:
    taste_values= pizza.taste
    quantile_value = np.quantile(taste_values, quantile)
    worst_taste_values = taste_values[taste_values<=quantile_value]
    return np.mean(worst_taste_values)


def conditional_taste_at_risk_menu(menu: PizzaMenu, quantile: float) -> float:
    taste_array = np.array([])
    for pizza in menu.pizzas:
        taste_array = np.append(taste_array, pizza.taste)
    quantile_value = np.quantile(taste_array, quantile)
    worst_taste_values = taste_array[taste_array <= quantile_value]
    return float(np.mean(worst_taste_values))

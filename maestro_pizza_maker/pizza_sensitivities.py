import numpy as np
from maestro_pizza_maker.pizza_menu import PizzaMenu
from sklearn.linear_model import LinearRegression


def menu_sensitivity_protein(menu: PizzaMenu) -> float:
    prices = []
    protein = []
    for pizza in menu.pizzas:
        prices.append(pizza.price)
        protein.append(pizza.protein)

    return build_model(prices, protein)


def menu_sensitivity_carbs(menu: PizzaMenu) -> float:
    prices = []
    carbs = []
    for pizza in menu.pizzas:
        prices.append(pizza.price)
        carbs.append(pizza.carbohydrates)
    return build_model(prices, carbs)


def menu_sensitivity_fat(menu: PizzaMenu) -> float:
    prices = []
    avg_fats = []
    for pizza in menu.pizzas:
        prices.append(pizza.price)
        avg_fats.append(pizza.average_fat)
    return build_model(prices, avg_fats)


def build_model(prices: [], value: []) -> float:
    prices = np.array(prices).reshape(-1, 1)
    value = np.array(value).reshape(-1, 1)
    model = LinearRegression()
    model.fit(value, prices)
    return model.coef_[0][0]

# class representing the pizza menu

from dataclasses import dataclass
from typing import List

import pandas as pd
import numpy as np
from maestro_pizza_maker.pizza import Pizza


@dataclass
class PizzaMenu:
    pizzas: List[Pizza]

    def to_dataframe(self, sort_by: str, descendent: bool) -> pd.DataFrame:
        pizza_data = []

        for pizza in self.pizzas:
            name = pizza.name
            price = pizza.price
            protein = pizza.protein
            average_fat = pizza.average_fat
            carbohydrates = pizza.carbohydrates
            calories = pizza.calories
            ingredients = [ingredient.value.name for ingredient in pizza.ingredients]
            pizza_data.append(
                {
                    "name": name,
                    "price": price,
                    "protein": protein,
                    "average_fat": average_fat,
                    "carbohydrates": carbohydrates,
                    "calories": calories,
                    "ingredients": ingredients,
                }
            )
        df = pd.DataFrame(pizza_data)
        df = df.sort_values(by=sort_by, ascending=descendent)

        return df

    @property
    def cheapest_pizza(self) -> Pizza:
        cheapest_pizza = None
        for pizza in self.pizzas:
            if cheapest_pizza is None or cheapest_pizza.price > pizza.price:
                cheapest_pizza = pizza
        return cheapest_pizza

    @property
    def most_caloric_pizza(self) -> Pizza:
        most_caloric_pizza = None
        for pizza in self.pizzas:
            if most_caloric_pizza is None or most_caloric_pizza.price > pizza.calories:
                most_caloric_pizza = pizza
        return most_caloric_pizza

    def get_most_fat_pizza(self, quantile: float = 0.5) -> Pizza:
        fat_arrays = [pizza.fat for pizza in self.pizzas]
        quantiles = [np.quantile(fat_array, quantile) for fat_array in fat_arrays]
        max_quantile = max(quantiles)
        index = quantiles.index(max_quantile)
        return self.pizzas[index]

    def add_pizza(self, pizza: Pizza) -> None:
        self.pizzas.append(pizza)

    def remove_pizza(self, pizza: Pizza) -> None:
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
        else:
            raise ValueError("Pizza is not in the menu")

    def __len__(self) -> int:
        return len(self.pizzas)

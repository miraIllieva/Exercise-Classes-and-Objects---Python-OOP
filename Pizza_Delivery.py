class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: dict) -> None:
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return self.pizza_ordered_made()
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += quantity * price_per_quantity
        else:
            self.ingredients[ingredient] = quantity
            self.price += quantity * price_per_quantity  # Update price only for new ingredients

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return self.pizza_ordered_made()
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_quantity

    def make_order(self):
        if self.ordered:
            return self.pizza_ordered_made()
        self.ordered = True
        formatted_ingredients = [f"{ing}: {quantity}" for ing, quantity in self.ingredients.items()]
        return (f"You've ordered pizza {self.name} prepared with {', '.join(formatted_ingredients)} and "
                f"the price will be {self.price}lv.")

    def pizza_ordered_made(self):
        return f"Pizza {self.name} already prepared, and we can't make any changes!"


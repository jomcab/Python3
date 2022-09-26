# Pizza Store
# Jomer Cabrera
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)

print("We sell", num_pizzas, "different kinds pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

pizza_and_prices = sorted(pizza_and_prices)
print(pizza_and_prices,"\n")

cheapest_pizza = pizza_and_prices[0]
print("The cheapest pizza is", cheapest_pizza[1])

priciest_pizza = pizza_and_prices[-1]
print("The priciest pizza is", priciest_pizza[1])

pizza_and_prices.pop()
pizza_and_prices.insert(4, [2.5, "peppers"])

three_cheapest = pizza_and_prices[0:3]
print("The 3 cheapest pizzas:", three_cheapest)
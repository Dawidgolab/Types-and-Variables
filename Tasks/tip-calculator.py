restaurantBill = float(input("Bill issued by a restaurant: "))

moreExpensiveTip = (20 * restaurantBill) / 100
cheaperTip = (15 * restaurantBill) / 100

print(f"More expensive tip : {moreExpensiveTip.__round__(2)} and cheaper tip: {cheaperTip.__round__(2)}")
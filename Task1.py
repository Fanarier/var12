prices = (1200, 800, 1500, 2000, 700, 3000, 400, 1100, 900, 500, 1300, 1800)

total_cost = sum(price for price in prices if price > 1000)

print("Общая стоимость товаров дороже 1000 рублей:", total_cost)

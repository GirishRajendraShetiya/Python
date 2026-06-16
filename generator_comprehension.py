daily_sales = [5, 10, 12, 20, 10, 14]

total_sales = [sale for sale in daily_sales if sale > 8]
print(total_sales)  # [10, 12, 20, 10, 14] - A full memory is allocated to the function at once.

# In case of a generator comprehension (denoted by round braces), the memory is allocated as and when required,
# like a stream.
# Also, it's used to deal with the in-built functions.

daily_sales = [5, 10, 12, 20, 10, 14]

total_sales = (sale for sale in daily_sales if sale > 8)
print(total_sales)  # <generator object <genexpr> at 0x7f1b7ae860c0>

daily_sales = [5, 10, 12, 20, 10, 14]

total_sales = sum(sale for sale in daily_sales if sale > 8)
print(total_sales)  # 66

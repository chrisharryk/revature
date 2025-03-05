# task 3: Analyzing Sales Data with Dictionaries

sales_data = {
    "Product A": [100, 200, 150],
    "Product B": [50, 75, 100],
    "Product C": [300, 250, 400]
}

for k, v in sales_data.items():
    sales_data[k] = sum(v)

print(sales_data)
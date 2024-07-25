
sales_data = [
    {"order_id": 1, "product_name": "Product A", "quantity": 5, "unit_price": 10.00},
    {"order_id": 2, "product_name": "Product B", "quantity": 3, "unit_price": 15.00},
    {"order_id": 3, "product_name": "Product A", "quantity": 2, "unit_price": 10.00},
    {"order_id": 4, "product_name": "Product C", "quantity": 1, "unit_price": 20.00},
    {"order_id": 5, "product_name": "Product B", "quantity": 4, "unit_price": 15.00}
]

# 1. Calculate Total Revenue and Units Sold
total_revenue = 0
total_units_sold = 0
product_sales = {}  # To track sales by product

for sale in sales_data:
    total_revenue += sale["quantity"] * sale["unit_price"]
    total_units_sold += sale["quantity"]
    
    product_name = sale["product_name"]
    if product_name in product_sales:
        product_sales[product_name]["quantity"] += sale["quantity"]
        product_sales[product_name]["revenue"] += sale["quantity"] * sale["unit_price"]
    else:
        product_sales[product_name] = {
            "quantity": sale["quantity"],
            "revenue": sale["quantity"] * sale["unit_price"]
        }

# 2. Identify Top-Selling Product
top_selling_product = max(product_sales, key=lambda x: product_sales[x]["quantity"])

# 3. Identify Product with Highest Revenue
highest_revenue_product = max(product_sales, key=lambda x: product_sales[x]["revenue"])

# 4. Calculate Average Unit Price
average_unit_price = total_revenue / total_units_sold

# Display the Results
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Total Units Sold: {total_units_sold}")
print(f"Top Selling Product: {top_selling_product} (Quantity: {product_sales[top_selling_product]['quantity']})")
print(f"Product with Highest Revenue: {highest_revenue_product} (Revenue: ${product_sales[highest_revenue_product]['revenue']:.2f})")
print(f"Average Unit Price: ${average_unit_price:.2f}")

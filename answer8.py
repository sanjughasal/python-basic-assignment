'''
Q8. File Restructuring and JSON Formating
You are given a large dataset in JSON format representing an e-commerce platform's order history, which includes orders from multiple customers. Each order has multiple items, with detailed attributes such as price, quantity, and shipping cost. Additionally, you need to extract specific information, perform calculations like the total cost, apply discounts, and sort the data based on various criteria like the total amount spent by each customer.
The goal is to:
Extract and restructure the data into a tabular format.
Perform calculations such as:
Total order value (price * quantity).
Apply a discount based on the total value of an order (e.g., 10% discount if the order exceeds $100).
Calculate shipping cost based on the number of items ordered (e.g., $5 per item).
Sort the data by the total amount spent by each customer.
Format the output so that it can be easily saved into a CSV file.

'''



import json
import csv

def calculate_order_details(order):
    order_id = order.get("order_id")
    customer_name = order.get("customer", {}).get("name")
    shipping_address = order.get("shipping_address")
    country_code = order.get("country_code", "")
    
    items = order.get("items", [])
    total_order_value = 0
    total_quantity = 0
    order_details = []

    for item in items:
        product_name = item.get("name")
        product_price = item.get("price", 0)
        quantity = item.get("quantity", 0)
        total_value = product_price * quantity
        total_order_value += total_value
        total_quantity += quantity

        order_details.append({
            "Order ID": order_id,
            "Customer Name": customer_name,
            "Product Name": product_name,
            "Product Price": product_price,
            "Quantity Purchased": quantity,
            "Total Value": total_value,
            "Shipping Address": shipping_address,
            "Country Code": country_code
        })

    discount = 0
    if total_order_value > 100:
        discount = total_order_value * 0.1

    shipping_cost = total_quantity * 5
    final_total = total_order_value - discount + shipping_cost

    for detail in order_details:
        detail["Discount"] = discount
        detail["Shipping Cost"] = shipping_cost
        detail["Final Total"] = final_total

    return order_details

def process_orders(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as file:
        orders = json.load(file)["orders"]

    all_order_details = []
    for order in orders:
        order_details = calculate_order_details(order)
        all_order_details.extend(order_details)

    all_order_details.sort(key=lambda x: x["Final Total"], reverse=True)

    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ["Order ID", "Customer Name", "Product Name", "Product Price", "Quantity Purchased", "Total Value", "Discount", "Shipping Cost", "Final Total", "Shipping Address", "Country Code"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for detail in all_order_details:
            writer.writerow(detail)

# Example usage
json_file_path = '/home/sanju/Documents/PythonAssignment/example.json'  
csv_file_path = '/home/sanju/Documents/PythonAssignment/example_output.csv'  
process_orders(json_file_path, csv_file_path)
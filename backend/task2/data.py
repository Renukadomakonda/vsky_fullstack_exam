

def get_data(orde) -> float:
    # Write your code here
    
    if not isinstance(orders, list):
        raise ValueError("The orders parameter must be a list.")
    
    total_revenue = 0.0

    for order in orders:
        if not isinstance(order, dict):
            raise ValueError("Each order must be a dictionary.")
        if 'item_name' not in order or 'quantity' not in order or 'price_per_item' not in order:
            raise ValueError("Each order must contain 'item_name', 'quantity', and 'price_per_item'.")
        if not isinstance(order['quantity'], (int, float)) or not isinstance(order['price_per_item'], (int, float)):
            raise ValueError("'quantity' and 'price_per_item' must be numbers.")
        if order['quantity'] < 0 or order['price_per_item'] < 0:
            raise ValueError("'quantity' and 'price_per_item' must be non-negative.")
        
        total_revenue += order['quantity'] * order['price_per_item']

    return total_revenue
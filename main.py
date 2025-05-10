# Mini-project: Inventory and Sales Analytics

# Initial data

def get_data():
    inventory = {
        'i001': {'name': 'Milk', 'stock': 5, 'unit': 'l'},
        'i002': {'name': 'Bread', 'stock': 2, 'unit': 'pcs'},
        'i003': {'name': 'Apples', 'stock': 0, 'unit': 'kg'},
        'i004': {'name': 'Flour', 'stock': 8, 'unit': 'kg'},
        'i005': {'name': 'Cheese', 'stock': 1, 'unit': 'kg'},
    }

    incoming = {
        'i001': 3,
        'i003': 5,
        'i006': 12,
    }

    sales = [
        'i001', 'i001', 'i002', 'i002', 'i002', 'i004', 'i004',
        'i004', 'i004', 'i004', 'i005', 'i005', 'i005'
    ]

    return inventory, incoming, sales

# Function to update stock

def update_stock(inventory, incoming):
    for id in incoming:
        if id in inventory:
            inventory[id]['stock'] += incoming[id]
        else:
            inventory[id] = {'name': 'Eggs', 'stock': incoming[id], 'unit': 'pcs'}

# Function to account for sales

def account_sales(inventory, sales):
    sales_sum = {}
    for id in sales:
        sales_sum[id] = sales_sum.get(id, 0) + 1

    for id in inventory:
        inventory[id]['sold'] = sales_sum.get(id, 0)

# Function to remove items with zero stock and sales

def remove_empty(inventory):
    for id in list(inventory.keys()):
        if inventory[id]['sold'] == 0 and inventory[id]['stock'] == 0:
            del inventory[id]

# Function to group items by unit

def group_by_unit(inventory):
    grouped_inventory = {}
    for id, info in inventory.items():
        unit = info['unit']
        item_data = {
            'name': info['name'],
            'stock': info['stock'],
            'sold': info['sold'],
            'id': id
        }
        grouped_inventory.setdefault(unit, []).append(item_data)
    return grouped_inventory

# Function to display report

def display_report(grouped_inventory):
    for unit, items in grouped_inventory.items():
        print(f"== {unit} ==")
        for item in items:
            print(f"{item['name']} — Stock: {item.get('stock', 0)} {unit}, Sold: {item.get('sold', 0)} (ID: {item.get('id')})")
        print()

# Function to find the top-selling item

def find_top_sales(inventory):
    max_id = None
    for id, info in inventory.items():
        if max_id is None or info['sold'] > inventory[max_id]['sold']:
            max_id = id
    if max_id:
        print(f"Top-selling item: {inventory[max_id]['name']} — Sold: {inventory[max_id]['sold']}")
    else:
        print("No sold items.")

# Function to find the item with the lowest stock

def find_lowest_stock(inventory):
    min_id = None
    for id, info in inventory.items():
        if min_id is None or info['stock'] < inventory[min_id]['stock']:
            min_id = id
    if min_id:
        print(f"Item with the lowest stock: {inventory[min_id]['name']} — Stock: {inventory[min_id]['stock']} {inventory[min_id]['unit']}")
    else:
        print("No items in stock.")

# Main function

def main():
    inventory, incoming, sales = get_data()

    update_stock(inventory, incoming)
    account_sales(inventory, sales)
    remove_empty(inventory)
    grouped_inventory = group_by_unit(inventory)

    display_report(grouped_inventory)
    find_top_sales(inventory)
    find_lowest_stock(inventory)

# Run the program

if __name__ == "__main__":
    main()

# Zomato Food Ordering System

restaurants = {
    "Spice Villa": {"Paneer Butter Masala": 180, "Roti": 20, "Biryani": 200},
    "Pizza Hub": {"Margherita": 250, "Cheese Burst": 300, "Garlic Bread": 150},
    "Burger World": {"Veg Burger": 120, "French Fries": 90, "Coke": 60}
}

def show_restaurants():
    print("\nAvailable Restaurants:")
    for i, name in enumerate(restaurants.keys(), 1):
        print(f"{i}. {name}")
    print()

def show_menu(restaurant):
    print(f"\nMenu - {restaurant}:")
    for item, price in restaurants[restaurant].items():
        print(f"{item} - ₹{price}")
    print()

def take_order(restaurant):
    order = []
    total = 0
    while True:
        item = input("Enter item to order (or 'done' to finish): ").title()
        if item.lower() == "done":
            break
        if item in restaurants[restaurant]:
            qty = int(input("Enter quantity: "))
            cost = restaurants[restaurant][item] * qty
            order.append((item, qty, cost))
            total += cost
        else:
            print("Item not found! Try again.")
    return order, total

def print_bill(order, total):
    print("\n----- BILL -----")
    for item, qty, cost in order:
        print(f"{item} x{qty} = ₹{cost}")
    print(f"Total Amount: ₹{total}")
    print("----------------\n")

def main():
    show_restaurants()
    choice = int(input("Select a restaurant (1-3): "))
    restaurant = list(restaurants.keys())[choice - 1]
    show_menu(restaurant)
    order, total = take_order(restaurant)
    print_bill(order, total)

if __name__ == "__main__":
    main()

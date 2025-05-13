from collections import deque

class MenuItem:
    def __init__(self, id, name, price, rating):
        self.id = id
        self.name = name
        self.price = price
        self.rating = rating

    def __str__(self):
        return f"{self.id}. {self.name} - ${self.price:.2f} | Rating: {self.rating}/5"

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.total = sum(item.price for item in items)

    def __str__(self):
        item_names = ', '.join(item.name for item in self.items)
        return f"Order #{self.order_id}: {item_names} | Total: ${self.total:.2f}"

def sort_menu(menu, key):
    n = len(menu)
    for i in range(n):
        for j in range(0, n-i-1):
            if getattr(menu[j], key) > getattr(menu[j+1], key):
                menu[j], menu[j+1] = menu[j+1], menu[j]
    return menu

def display_menu(menu):
    print("\nSort menu by:")
    print("1. Price")
    print("2. Name")
    print("3. Rating")
    choice = input("Enter choice: ")
    key = "price" if choice == "1" else "name" if choice == "2" else "rating"
    sorted_menu = sort_menu(menu[:], key)
    print("\n--- Menu ---")
    for item in sorted_menu:
        print(item)

def take_order(menu, order_queue, order_history, order_counter):
    display_menu(menu)
    item_ids = input("\nEnter item numbers separated by comma: ").split(",")
    items = []
    for i in item_ids:
        try:
            items.append(menu[int(i.strip()) - 1])
        except:
            print(f"Item {i.strip()} not found.")
    order = Order(order_counter, items)
    order_queue.append(order)
    order_history.append(order)
    print(f"\nOrder #{order.order_id} added to queue. Total: ${order.total:.2f}")

def serve_order(order_queue):
    if order_queue:
        order = order_queue.popleft()
        print(f"\nServing {order}")
    else:
        print("\nNo orders in the queue.")

def view_order_history(order_history):
    print("\n--- Order History ---")
    for order in order_history:
        print(order)

def main():
    menu = [
        MenuItem(1, "Burger", 5.0, 4.2),
        MenuItem(2, "Pizza", 8.0, 4.5),
        MenuItem(3, "Steak", 15.0, 4.8),
        MenuItem(4, "Fries", 3.0, 4.0),
        MenuItem(5, "Pasta", 7.0, 4.1)
    ]
    order_queue = deque()
    order_history = []
    order_counter = 100

    while True:
        print("\nWelcome to Pythonic Bites!")
        print("1. Display Menu")
        print("2. Take Order")
        print("3. Serve Order")
        print("4. View Order History")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            display_menu(menu)
        elif choice == "2":
            take_order(menu, order_queue, order_history, order_counter)
            order_counter += 1
        elif choice == "3":
            serve_order(order_queue)
        elif choice == "4":
            view_order_history(order_history)
        elif choice == "5":
            print("Thank you! Visit again.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

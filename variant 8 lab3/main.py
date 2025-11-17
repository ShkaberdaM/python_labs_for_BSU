class Order:
    orders_quantity=0
    def __init__(self):
        self.items={}
        Order.orders_quantity+=1
        print(Order.orders_quantity)

    def add_item(self,name,price):
        self.items[name] = price
        print(f"added {name}-{price}")
        return self

    def remove_item(self):
        i=input("Enter item to remove: ")
        if i in self.items:
            d=input(f"Do you want to remove {i}? (y/n): ")
            if d =='y':
                del self.items[i]
        else:
            print("Item not found")
        return self

    def get_total_price(self):
        result=sum(self.items.values())
        print(f"The total price is {result}")
        return result

    def show_items(self):
        if self.items:
            print("\nItems in order:")
            for name, price in self.items.items():
                print(f"  - {name}: {price} р.")
        else:
            print("Order doesn't exist")

    def manual_input(self):

        while True:
            print("1. Add item")
            print("2. Remove item")
            print("3. Show total price")
            print("4. Show items")
            print("5. Exit")

            choice = input("Choose action (1-5): ")

            if choice == "1":
                name = input("Enter item name: ")
                try:
                    price = float(input("Enter item price: "))
                    self.add_item(name, price)
                except ValueError:
                    print("Error: price must be a number!")

            elif choice == "2":
                self.remove_item()

            elif choice == "3":
                self.get_total_price()

            elif choice == "4":
                self.show_items()

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice!")

order = Order()


order.add_item("Book", 500)
order.add_item("Pen", 20)
order.show_items()
order.get_total_price()
order.manual_input()
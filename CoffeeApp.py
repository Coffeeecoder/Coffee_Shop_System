import random
import time
import sys

def animate_text(text, delay=0.05):
    """Print text with typing animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_steps(steps):
    """Show coffee preparation steps with animation."""
    for step in steps:
        animate_text(f"➡️ {step}...", delay=0.07)
        time.sleep(0.5)

class Coffee:
    def __init__(self, name, price, recipe_steps):
        self.name = name
        self.price = price
        self.recipe_steps = recipe_steps

    def __str__(self):
        return f"{self.name} - ₹{self.price}"


class Order:
    def __init__(self):
        self.cart = {}

    def add_item(self, coffee, quantity):
        if coffee.name in self.cart:
            self.cart[coffee.name]["quantity"] += quantity
        else:
            self.cart[coffee.name] = {"coffee": coffee, "quantity": quantity}
        animate_text(f"\n✅ {quantity} x {coffee.name} added to cart.")

    def remove_item(self, coffee_name):
        if coffee_name in self.cart:
            del self.cart[coffee_name]
            animate_text(f"\n❌ {coffee_name} removed from cart.")
        else:
            animate_text("\nCoffee not found in cart.")

    def is_empty(self):
        return len(self.cart) == 0

    def subtotal(self):
        return sum(item["coffee"].price * item["quantity"] for item in self.cart.values())

    def gst(self):
        return self.subtotal() * 0.05

    def grand_total(self):
        return self.subtotal() + self.gst()

    def display_cart(self):
        if self.is_empty():
            animate_text("\n🛒 Your cart is empty.")
            return

        print("\n=========== YOUR CART ===========")
        for item in self.cart.values():
            coffee = item["coffee"]
            qty = item["quantity"]
            total = coffee.price * qty
            print(f"{coffee.name:<20} x{qty:<3} ₹{total}")
        print("---------------------------------")
        print(f"Subtotal : ₹{self.subtotal():.2f}")
        print(f"GST (5%) : ₹{self.gst():.2f}")
        print(f"Total    : ₹{self.grand_total():.2f}")
        print("=================================")

    def clear_cart(self):
        self.cart.clear()


class CoffeeShop:
    def __init__(self):
        self.menu = [
            Coffee("Espresso", 120, ["Grinding beans", "Brewing shot", "Serving hot"]),
            Coffee("Americano", 150, ["Brewing espresso", "Adding hot water", "Serving"]),
            Coffee("Cappuccino", 180, ["Brewing espresso", "Steaming milk", "Adding foam"]),
            Coffee("Latte", 200, ["Brewing espresso", "Steaming milk", "Pouring milk"]),
            Coffee("Mocha", 220, ["Brewing espresso", "Mixing chocolate", "Adding milk"]),
        ]
        self.order = Order()

    def display_menu(self):
        animate_text("\n☕ BREW HAVEN MENU ☕", delay=0.04)
        print("=" * 30)
        for index, coffee in enumerate(self.menu, start=1):
            animate_text(f"{index}. {coffee.name:<15} ₹{coffee.price}", delay=0.02)
        print("=" * 30)

    def add_to_cart(self):
        self.display_menu()
        try:
            choice = int(input("\nEnter coffee number: "))
            if choice < 1 or choice > len(self.menu):
                animate_text("❌ Invalid coffee selection.")
                return
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                animate_text("❌ Quantity must be greater than 0.")
                return
            coffee = self.menu[choice - 1]
            self.order.add_item(coffee, quantity)
        except ValueError:
            animate_text("❌ Please enter valid numbers.")

    def remove_from_cart(self):
        if self.order.is_empty():
            animate_text("\nCart is empty.")
            return
        self.order.display_cart()
        name = input("\nEnter coffee name to remove: ").strip()
        self.order.remove_item(name)

    def view_cart(self):
        self.order.display_cart()

    def payment(self):
        animate_text("\nChoose Payment Method")
        print("1. Cash\n2. Card\n3. UPI")
        while True:
            choice = input("Enter choice (1-3): ")
            if choice == "1":
                animate_text("\n💵 Cash payment selected.")
                return "Cash"
            elif choice == "2":
                card = input("Enter last 4 digits of your card: ")
                animate_text(f"\n💳 Card ending with {card} accepted.")
                return "Card"
            elif choice == "3":
                upi = input("Enter your UPI ID: ")
                animate_text(f"\n📱 Payment request sent to {upi}")
                input("Press Enter after completing payment...")
                animate_text("✅ Payment Successful!")
                return "UPI"
            else:
                animate_text("Invalid choice.")

    def print_receipt(self, payment_method):
        order_id = random.randint(1000, 9999)
        animate_text("\n========== RECEIPT ==========")
        for item in self.order.cart.values():
            coffee = item["coffee"]
            qty = item["quantity"]
            animate_text(f"{coffee.name:<15} x{qty:<3} ₹{coffee.price * qty}", delay=0.02)
        print("-----------------------------")
        print(f"Subtotal : ₹{self.order.subtotal():.2f}")
        print(f"GST (5%) : ₹{self.order.gst():.2f}")
        print(f"Grand Total : ₹{self.order.grand_total():.2f}")
        print(f"Payment : {payment_method}")
        print(f"Order ID : #{order_id}")
        animate_text("❤️ Thank you for visiting Brew Haven!", delay=0.04)
        print("==============================")

        # Animated coffee preparation
        animate_text("\n☕ HOW YOUR COFFEE IS MADE ☕", delay=0.05)
        for item in self.order.cart.values():
            coffee = item["coffee"]
            animate_text(f"\n➡️ Preparing {coffee.name}...", delay=0.05)
            animate_steps(coffee.recipe_steps)

    def checkout(self):
        if self.order.is_empty():
            animate_text("\n🛒 Cart is empty.")
            return
        self.order.display_cart()
        confirm = input("\nConfirm Order? (yes/no): ").lower()
        if confirm != "yes":
            animate_text("\nOrder Cancelled.")
            return
        payment_method = self.payment()
        self.print_receipt(payment_method)
        self.order.clear_cart()

    def run(self):
        while True:
            animate_text("\n====== BREW HAVEN COFFEE SHOP ======", delay=0.03)
            print("1. View Coffee Menu")
            print("2. Add Coffee to Cart")
            print("3. Remove Coffee from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit")
            choice = input("\nEnter your choice: ")
            if choice == "1":
                self.display_menu()
            elif choice == "2":
                self.add_to_cart()
            elif choice == "3":
                self.remove_from_cart()
            elif choice == "4":
                self.view_cart()
            elif choice == "5":
                self.checkout()
            elif choice == "6":
                animate_text("\n👋 Thank you! Visit Again.", delay=0.04)
                break
            else:
                animate_text("\nInvalid Choice.")


def main():
    app = CoffeeShop()
    app.run()


if __name__ == "__main__":
    main()


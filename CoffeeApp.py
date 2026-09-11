import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

class BrewHavenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("☕ Brew Haven Coffee Shop ☕")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5e6ca")  # Cream background

        # Coffee menu
        self.menu = {
            "Espresso": 120,
            "Americano": 150,
            "Cappuccino": 180,
            "Latte": 200,
            "Mocha": 220
        }

        self.cart = {}
        self.build_ui()

    def build_ui(self):
        # Title
        tk.Label(self.root, text="☕ Brew Haven Menu ☕",
                 font=("Papyrus", 24, "bold"), bg="#f5e6ca", fg="#3e2f2f").pack(pady=15)

        # Menu frame
        self.menu_frame = tk.Frame(self.root, bg="#f5e6ca")
        self.menu_frame.pack()

        for coffee, price in self.menu.items():
            tk.Button(self.menu_frame,
                      text=f"{coffee} - ₹{price}",
                      font=("Helvetica", 14, "bold"),
                      width=25,
                      bg="#d7bfae", fg="#3e2f2f",
                      relief="raised",
                      command=lambda c=coffee: self.add_to_cart(c)).pack(pady=5)

        # Action buttons
        tk.Button(self.root, text="🛒 View Cart", font=("Helvetica", 12, "bold"),
                  bg="#a3c9a8", command=self.view_cart).pack(pady=8)

        tk.Button(self.root, text="✅ Checkout", font=("Helvetica", 12, "bold"),
                  bg="#f4a261", command=self.checkout).pack(pady=8)

        tk.Button(self.root, text="❌ Exit", font=("Helvetica", 12, "bold"),
                  bg="#e76f51", command=self.root.quit).pack(pady=8)

    def add_to_cart(self, coffee):
        self.cart[coffee] = self.cart.get(coffee, 0) + 1
        messagebox.showinfo("Added", f"✅ {coffee} added to cart!")

    def view_cart(self):
        if not self.cart:
            messagebox.showinfo("Cart", "🛒 Your cart is empty.")
            return
        cart_text = "\n".join([f"{c} x{q} ₹{self.menu[c]*q}" for c, q in self.cart.items()])
        messagebox.showinfo("Your Cart", cart_text)

    def checkout(self):
        if not self.cart:
            messagebox.showinfo("Empty", "🛒 Cart is empty.")
            return
        self.animate_brewing()

    def animate_brewing(self):
        brew_window = tk.Toplevel(self.root)
        brew_window.title("Preparing Your Coffee...")
        brew_window.geometry("500x300")
        brew_window.configure(bg="#f5e6ca")

        label = tk.Label(brew_window, text="Starting preparation...",
                         font=("Helvetica", 16, "bold"), bg="#f5e6ca")
        label.pack(pady=20)

        progress = ttk.Progressbar(brew_window, length=400, mode="determinate")
        progress.pack(pady=15)

        steps = ["Grinding beans ☕", "Brewing espresso 🍵", "Steaming milk 🥛", "Adding flavors 🍫", "Serving hot ❤️"]
        for step in steps:
            label.config(text=step)
            for i in range(0, 101, 20):
                progress["value"] = i
                brew_window.update_idletasks()
                time.sleep(0.2)
            time.sleep(0.5)

        label.config(text="✨ Brewing complete! Enjoy your coffee ✨")
        tk.Button(brew_window, text="📜 Show Receipt", font=("Helvetica", 12, "bold"),
                  bg="#f4a261", command=lambda: self.show_receipt(brew_window)).pack(pady=15)

    def show_receipt(self, window):
        window.destroy()
        total = sum(self.menu[c]*q for c, q in self.cart.items())
        gst = total * 0.05
        grand_total = total + gst
        order_id = random.randint(1000, 9999)

        receipt = "☕ Brew Haven Receipt ☕\n"
        receipt += "-----------------------------\n"
        for c, q in self.cart.items():
            receipt += f"{c} x{q} ₹{self.menu[c]*q}\n"
        receipt += "-----------------------------\n"
        receipt += f"Subtotal: ₹{total:.2f}\n"
        receipt += f"GST (5%): ₹{gst:.2f}\n"
        receipt += f"Grand Total: ₹{grand_total:.2f}\n"
        receipt += f"Payment: Cash/UPI/Card\n"
        receipt += f"Order ID: #{order_id}\n"
        receipt += "❤️ Thank you for visiting Brew Haven! ❤️"

        messagebox.showinfo("Receipt", receipt)
        self.cart.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = BrewHavenApp(root)
    root.mainloop()

from PIL import Image, ImageTk

def set_background(self):
    bg_img = Image.open("coffee_bg.jpg")  # Add a café background image
    bg_img = bg_img.resize((800, 600))
    self.bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(self.root, image=self.bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
self.menu.update({
    "Croissant": 80,
    "Brownie": 100,
    "Cheesecake": 150,
    "Sandwich": 120
})

def calculate_discount(self, total):
    if total > 500:
        return total * 0.1  # 10% discount
    return 0
    def animate_steam(self, canvas):
    for i in range(20):
        canvas.create_text(250, 150-i*5, text="~", font=("Helvetica", 20), fill="gray")
        canvas.update()
        time.sleep(0.1)





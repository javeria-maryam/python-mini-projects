store ={
    "Apple" : 2.0,
    "Banana" : 1.8,
    "Bread" : 1.5,
    "Milk" : 2.0,
    "Eggs" : 3.0
}

def display():

    print("\n Shopping Cart Menu:")
    print("1. View store items")
    print("2. Add item to cart")
    print("3. Remove item from cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit Cart")

def main():

    cart = {}

    while True:

        display()
        choice = int(input("Choose betweem 1-6: "))

        if choice == 1:
          
          print(f"\n Store Items:")
          for item, price in store.items():
              print(f"{item} : ${price}")

        elif choice == 2:

            item = input("Enter item name: ").capitalize()

            if item in store:
              qty = int(input("Enter quantity: "))
              cart[item] = cart.get(item, 0) + qty
              print(f"Added {qty} {item} in cart")
            else:
               print("Item not available!")
            
        elif choice == 3:
           
           item = input("Enter item to remove: ").capitalize()

           if item in cart:
             del cart[item]
           else:
              print("Item not present in cart")

        elif choice == 4:
           
           if cart:
              print("\n Your Cart:")
              total = 0
              for item , qty in cart.items():
                 price = store[item] * qty
                 total +=price
                 print(f"{item} X {qty} = ${price:.2f}")
              print(f"Total = {total:.2f}")
           else:
              print("Your Cart is Empty!")

        elif choice == 5:
           
           if cart:
            print("\nCheckout:")
            total = 0
            for item, qty in cart.items():
              price = store[item] * qty
              total += price
              print(f"Total amount: ${total}")
           else:
               print("Your cart is empty. Add items before checkout")
           break

        elif choice == 6:
           print("Exiting Cart, Goodbye!")
           break
        
        else:
           print("Invalid choice. Please enter a number between 1-6")


if __name__ == "__main__":
   main()
           
           

              


           


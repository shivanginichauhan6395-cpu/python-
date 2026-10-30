# Program 8: CRUD operations on product details

products = []

while True:
    print("\n1. Add Product  2. View Products  3. Update Product  4. Delete Product  5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        products.append({"id": product_id, "name": name, "price": price, "quantity": quantity})
        print("Product added successfully.")

    elif choice == "2":
        if products:
            for product in products:
                print(product)
        else:
            print("No products found.")

    elif choice == "3":
        product_id = input("Enter product ID to update: ")
        for product in products:
            if product["id"] == product_id:
                product["name"] = input("Enter new name: ")
                product["price"] = float(input("Enter new price: "))
                product["quantity"] = int(input("Enter new quantity: "))
                print("Product updated successfully.")
                break
        else:
            print("Product not found.")

    elif choice == "4":
        product_id = input("Enter product ID to delete: ")
        for product in products:
            if product["id"] == product_id:
                products.remove(product)
                print("Product deleted successfully.")
                break
        else:
            print("Product not found.")

    elif choice == "5":
        print("Program closed.")
        break
    else:
        print("Invalid choice.")

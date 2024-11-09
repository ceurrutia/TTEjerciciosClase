##Diccionario
productList = {}


##Crear un nuevo producto

def createProduct():
    id = int(input("Enter product ID: "))
    name = str(input("Enter product name: "))
    description = str(input("Enter description: "))
    price = float(input("Enter single price: "))
    stock = int(input("Enter stock: "))
    productList[id] = {
        "name": name,
        "description": description,
        "price": price,
        "stock": stock
    }
    print("Product added successfully")


##Listar todos los productos

def listProducts():
    if len(productList) == 0:
        print("Nothing in this list")
    else:
        for id, details in productList.items():
            print(f"ID: {id}")
            for key, value in details.items():
                print(f"{key.capitalize()}: {value}")
            print("\n")


##Remover por ID

def removeProduct():
    idRemover = int(input("Enter product ID to remove: "))
    if idRemover in productList:
        removed_product = productList.pop(idRemover)
        print("Product removed successfully")
        print(f"ID: {idRemover}, Name: {removed_product['name']} was removed")
    else:
        print("Product not found")


##Actualizar datos de producto

def updateProduct():
    idToUpdate = int(input("Enter the ID of the product to update description or price: "))

    if idToUpdate in productList:
        product = productList[idToUpdate]
        product['description'] = str(input("Enter new description: "))
        product['price'] = float(input("Enter new price: "))
        print("Product updated successfully!")
        print(f"ID: {idToUpdate}, Name: {product['name']} was updated")
    else:
        print("ID not found")
    
##Buscar un producto por ID

def searchProduct():
    IdToSearch = int(input("Enter the product ID: "))
    if IdToSearch in productList:
        product = productList[IdToSearch]
        print(f"The Product with ID: {IdToSearch}, Name: {product['name']}, Description: {product['description']} is in the list")
    else:
        print("Product not found")


##Comprar producto y que tenga stock
    
def byProduct():
    id = int(input("Enter the product ID: "))
    userCant = int(input("Enter qantity: "))
    
    if id in productList:
        product = productList[id]
        if userCant <= product['stock']:
            product['stock'] -= userCant
            print("You bought the product successfully")
            print("Total value:", product['price'] * userCant)
        else:
            print("Not enough stock for this product. Try another!")
    else:
        print("Product not found")
            
##Recargar stock

def updateStock():
    id = int(input("Enter product id to update stock: "))
    cantStock = int(input("Enter cantity to update: "))      
    
    if id in productList:
        productList[id]['stock'] += cantStock
        print("Stock updated successfully")
        print(f"Now you have {productList[id]['stock']} units in product ID: {id}")
    else:
        print("ID not found")

##MENU####

while True:
    try:
        print("Select option")
        print("1. Add a new product")
        print("2. List products")
        print("3. Update a description or price of the product by ID")
        print("4. Remove product by ID")
        print("5. Update stock")
        print("6. Search product by ID or name")
        print("7. Buy a product")
        print("8. Exit")

        option = int(input("Select an option: "))
        if option == 1:
            createProduct()

        elif option == 2:
                print("### Products List ###")
                listProducts()

        elif option == 3:
            updateProduct()

        elif option == 4:
            removeProduct()

        elif option == 5:
            updateStock()
            
        elif option == 6:
            searchProduct()
            
        elif option == 7:    
            byProduct()

        elif option == 8:
            print("Exit the program... Bye!")
            break
        else:
            print("Invalid option")
    except (ValueError):
        print("You must enter a number")
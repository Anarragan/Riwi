#stores products as items in a list
inventory:list = []

#adds products like a dictionary form to the inventory list
def add_product(name:str = "", price:int = 0, amount:int = 0):
        name:str = name.strip().lower()
        for product in inventory:
            if name in product:
                return print(f"El producto {name} ya existe")
            
        if price >  0 and amount > 0:
            product:dict = {
            name: (price, amount)
            }
            inventory.append(product)
            return print(f"Producto {name} añadido")
                
        else:
            return print(f"Precio y cantidad deben ser valores mayores a 0...")

#search within the inventory list for the dictionary 
#that has the key “name” passed as a parameter
def search_product(name:str = ""):
    name:str = name.strip().lower()
 
    for product in inventory:
        if name in product:
            price, amount = product[name]
            return print(f"Nombre: {name} \nPrecio: {price} \nCantidad: {amount}")
        
    return print(f"El producto {name} no se encuentra...")
    
        
#updates the price of a product by deleting the previous tuple 
#but retaining the value of its quantity
def update_price(name:str = "", new_price:int = 0):
    name = name.strip().lower()
    if new_price > 0:
        for product in inventory:
            if name in product:
                _, amount = product[name]
                new_tup = (new_price, amount)
                product[name] = new_tup
                return print(f"El precio de {name} se ha actualizado a {new_price}")   
            
        return print(f"El producto {name} no se encuentra")    
    
    else:
        return print("El nuevo precio debe ser mayor a 0")    
              
#deletes the product indicated by its key “name” and displays a message 
#in case of success
def delete_product(name:str = ""):
    name = name.strip().lower()
    for product in inventory:
        if name in product:
            inventory.remove(product)
            return print(f"El producto {name} ha sido eliminado")
    
    return print(f"El producto {name} no se encuentra")

#calculates the total value of the inventory by implementing a lambda function
calculate_total_price =  lambda:sum(price * amount 
for product in inventory
    for price, amount in product.values())

#displays a menu 
def show_menu():
        print("----------INVENTARIO DE PRODUCTOS----------\n" \
        "Seleccione la opcion que desee realizar...\n" \
        "1. Añadir productos\n" \
        "2. Consultar productos\n" \
        "3. Actualizar precios\n" \
        "4. Eliminar productos\n" \
        "5. Calcular el valor total del inventario\n" \
        "6. Salir\n")

#prints a welcome message and calls the function show_menu() and called 
#other functions as appropriate. Uses the tryexcept, the try executes the selected
#option and if there is not a valid option displays a message with the clarification
def main():
    print("**************BIENVENIDO AL SISTEMA DE GESTION DE INVENTARIO*************")
    while True:
        show_menu()
        try:
            option = int(input("Ingrese el número de la opcion: "))
            if option == 1:
                name:str = str(input("Ingrese el nombre del producto: "))
                price:int = int(input("Ingrese el precio: "))
                amount:int = int(input("Ingrese la cantidad: "))
                add_product(name, price, amount)
                
            elif option == 2:
                name:str = str(input("Nombre del producto que quiere buscar: "))
                search_product(name)

            elif option == 3:
                name:str = str(input("Nombre del producto que quiere actualizar: "))
                new_price:int = int(input("Nuevo precio: "))
                update_price(name, new_price)

            elif option == 4:
                name:str = str(input("Nombre del producto que quiere eliminar: "))
                delete_product(name)

            elif option == 5:
                total_price:int = calculate_total_price()
                print(f"El valor total del inventario es {total_price}")

            elif option == 6:
                print("Saliendo del programa...")
                break

            else:
                print("Oops! esa no es una opcion valida. Intentalo de nuevo")
            
        except ValueError:
            print("Debes ingresar el numero de la accion que quieres realizar o los datos que correspondan")

#causes the file to be executed directly in the code and not in case of importing as a module
if __name__ == "__main__":
    main()

#but it could also be replaced by calling only the function main() for this case
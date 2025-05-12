producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos adquiridos: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))


def costo_total(precio, cantidad, descuento):
    total = precio * cantidad
    total_descuento = total * (descuento / 100)
    total_final = total - total_descuento
    return total_final
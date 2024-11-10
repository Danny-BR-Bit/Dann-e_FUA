Inventario = {}

Inventario["Manzana"] = {
                        "Precio":1.800,
                        "Cantidad": 20}

Inventario["Pera"] = {
                       "Precio":1.400,
                        "Cantidad": 15,}

Inventario["Banano"] = {
                        "Precio":600,
                        "Cantidad": 24,}

Acc = int(input("Bienvenido!, que accion desea realizar? \n  1.Registro de productos \n  2.Consulta de inventario \n  3.Actualizacion de cantidad \n  4:Eliminacion de un producto \n"))
while True:
  if Acc == 1:
    Nm = input("Ingrese el nombre del producto a añadir: ").capitalize()
    Pr = float(input("Ingrese el valor del producto: "))
    Ct = int(input("Ingrese la cantidad del producto: "))
    Inventario[Nm] = {"Precio":Pr, "Cantidad":Ct}
    print("Inventario, actualizado")
    print(Inventario)
    menu = input("Desea realizar otra accion? (S/N): ")
    if menu == "N":
      break
    else:
      Acc = int(input("Bienvenido!, que accion desea realizar? \n  1.Registro de productos \n  2.Consulta de inventario \n  3.Actualizacion de cantidad \n  4:Eliminacion de un producto \n"))
  elif Acc == 2:
    print(Inventario)
    menu = input("Desea realizar otra accion? (S/N): ").upper()
    if menu == "N":
      break
    else:
      Acc = int(input("Bienvenido!, que accion desea realizar? \n  1.Registro de productos \n  2.Consulta de inventario \n  3.Actualizacion de cantidad \n  4:Eliminacion de un producto \n"))
  elif Acc == 3:
    Nm = str(input("ingrese el nombre del producto: ")).capitalize()
    Ct = int(input("Ingrese cantidad nueva: "))
    Inventario[Nm]["Cantidad"] = Ct
    print(Inventario)
    menu = input("Desea realizar otra accion? (S/N): ").upper()
    if menu == "N":
      break
    else:
      Acc = int(input("Bienvenido!, que accion desea realizar? \n  1.Registro de productos \n  2.Consulta de inventario \n  3.Actualizacion de cantidad \n  4:Eliminacion de un producto \n"))
  else:
    Nm = str(input("Ingrese el nombre del producto: ")).capitalize()

    if Nm in Inventario:
      del Inventario[Nm]
      print("Producto eliminado correctamente")
      print(Inventario)
      menu = input("Desea realizar otra accion? (S/N): ").upper()
      if menu == "N":
        break
      else:
        Acc = int(input("Bienvenido!, que accion desea realizar? \n  1.Registro de productos \n  2.Consulta de inventario \n  3.Actualizacion de cantidad \n  4:Eliminacion de un producto \n"))
    else:
      print(f"{Nm} no se encuentra en stock")
      menu = input("Desea realizar otra accion? (S/N): ").upper()
      if menu == "N":
        break
      else:
        Acc = int(input("Bienvenido!, que accion desea realizar? \n  1.Registro de productos \n  2.Consulta de inventario \n  3.Actualizacion de cantidad \n  4:Eliminacion de un producto \n"))
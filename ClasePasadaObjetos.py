class Catalogo:
    productos = []

    # Definir los metodos...
    def codigoExiste(self,codigo):
        for i in self.productos:
            if codigo == i["codigo"]:
                return True    
        return False

    def agregar(self,codigo,descripcion,cantidad,precio,imagen,proveedor):
        if self.codigoExiste(codigo):
            print("No se pudo agregar.")
            return False
        productoAgregar = {
            "codigo":codigo,
            "descripcion":descripcion,
            "cantidad": cantidad,
            "precio": precio,
            "imagen":imagen,
            "proveedor":proveedor
        }
        self.productos.append(productoAgregar)
        print("Se pudo agregar!")
        return True

    def eliminar(self,codigo):
        if self.codigoExiste(codigo):
            for i in self.productos:
                if codigo == i["codigo"]:
                    self.productos.remove(i)
                    return True
        return False

    def modificar(self,codigo,descripcion,cantidad,precio,imagen,proveedor):
        if self.codigoExiste(codigo):
            for i in self.productos:
                if i["codigo"] == codigo:
                    i["descripcion"] = descripcion
                    i["cantidad"] = cantidad
                    i["precio"] = precio
                    i["imagen"] = imagen
                    i["proveedor"] = proveedor
                    return True
        return False

    def mostrarTodos(self):
        for i in self.productos:
            print(f"Código: {i['codigo']}")
            print(f"Descripción: {i['descripcion']}")
            print(f"Cantidad: {i['cantidad']}")
            print(f"Precio: {i['precio']}")
            print(f"Imagen: {i['imagen']}")
            print(f"Proveedor: {i['proveedor']}")
            print("-" * 50)

    def mostrarUno(self,codigo):
        if self.codigoExiste(codigo):
            for i in self.productos:
                if codigo == i['codigo']:
                    print(f"Código: {i['codigo']}")
                    print(f"Descripción: {i['descripcion']}")
                    print(f"Cantidad: {i['cantidad']}")
                    print(f"Precio: {i['precio']}")
                    print(f"Imagen: {i['imagen']}")
                    print(f"Proveedor: {i['proveedor']}")
                    print("-" * 50)

catalogo1 = Catalogo()

catalogo1.agregar(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
catalogo1.agregar(3, 'Monitor LCD 22 pulgadas', 15, 52500, 'monitor22.jpg', 103)
catalogo1.agregar(4, 'Monitor LCD 27 pulgadas', 25, 78500, 'monitor27.jpg', 104)
catalogo1.agregar(5, 'Pad mouse', 5, 500, 'padmouse.jpg', 105)

catalogo1.mostrarTodos()

catalogo1.modificar(2, 'Mouse USB 3 botones', 5, 4000, 'mouse.jpg', 102)
print("Vamos a ver el cambio de precio...")
catalogo1.mostrarUno(2)
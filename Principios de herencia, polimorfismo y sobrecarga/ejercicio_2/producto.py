from interfaz import InterfazProducto


class Producto(InterfazProducto):
    
    def __init__(self):
        self.__lista_Productos = []
        self._descuento = None
        
        
    def agregar_producto(self, producto):
        
        if any(agregar['producto'] == producto['producto'] for agregar in self.__lista_Productos):
            print(f"\nError: '{producto['producto']}' ya existe")
            return False 
        
        
        self.__lista_Productos.append(producto)
        print(f"\nRegistro exitoso: {producto['producto']}")
        return True
    

    # Método para modificar el precio con validación (setter)
    def set_precio(self, producto, nuevo_precio):
        
        productos = next((producto_lista for producto_lista in self.__lista_Productos if producto_lista['producto'] == producto), None)
        if not productos:
            print(f"""
                  El producto {producto} no esta en la base de datos.
            """)
            return False
        
        precion_original = productos['precio']
        if nuevo_precio >= 0:
            productos['precio'] = nuevo_precio
            print(f"""\n
                --- Resumen ---
                Producto : {producto}
                Precio original: {precion_original:,}
                Precio final: {nuevo_precio:,}
            """)
        return True
        
                
                
    # Método para aplicar descuento
    def aplicar_descuento(self, objeto):
        
        if 'producto' not in objeto or 'descuento' not in objeto:
            raise KeyError("El objeto debe contener 'producto' y 'descuento'")
        
        productos = next((producto_lista for producto_lista in self.__lista_Productos if producto_lista['producto'] == objeto['producto']), None)
        if not productos:
            print(f"""
                  El producto {objeto['producto']} no esta en la base de datos.
            """)
            return False
        
        self._descuento = objeto['descuento']
        
        precio_original = productos['precio']
        nuevo_precio = precio_original * (1 - objeto['descuento'] / 100)
        productos['precio'] = nuevo_precio
        print(f"""
              Descuento aplicado: {productos['producto']} - 
              Precio original: ${precio_original:,} - 
              Nuevo precio: ${nuevo_precio:,} ({objeto['descuento']}% de descuento)
        """)
        return True
    
    
    # Método para obtener el precio (getter)
    def get_precio(self):
        return self.__lista_Productos[-1]['precio']
    
    
    def mostrar_productos(self):
        return self.__lista_Productos

class Pintura():
    def __init__(self, cota, nombre, precio, anio, status:bool, eliminate:False):
        self.cota = cota 
        self.nombre = nombre
        self.precio = precio
        self.anio = anio
        self.status = status
        self.eliminate=eliminate

    def mostrar(self):
         
        if self.status == True:
            Status = "En Exhibicion"
        else:
            Status = "En Mantenimiento"
            
        if self.eliminate == True:
            eli = "Si"
        else:
            eli = "No"

        if eli == 'Si':
            Status = "Escondido"
        
        print(f'''
        Pintura

    Nombre:    {self.nombre}
    Cota:      {self.cota}
    Precio:    {self.precio}
    Ano:       {self.anio}
    Status:    {Status}
    Eliminado: {eli}
              ''')
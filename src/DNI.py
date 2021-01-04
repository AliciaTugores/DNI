from src.tabla_asignación import tabla_asignacion

class DNI:

    length_numbers = 8
    length_dni = 9

    def __init__(self, numbers):
        self.numbers = str(numbers)

    def validarDNI(self):
        if len(self.numbers) != DNI.length_numbers:
            return False
    
    def obtenerLetra(self):
        resto = int(self.numbers) % tabla_asignacion.longitud_tabla
        letra = tabla_asignacion.tabla[resto]
        return letra

    def letra_correcta(self):
        letra = self.obtenerLetra()
        if letra in tabla_asignacion.letras_no_permitidas:
            return False
        else:
            return letra
    
    def DniConLetra(self):
        return self.numbers + self.obtenerLetra()

    def longitud_dni(self):
        if len(self.DniConLetra()) == DNI.length_dni:
            return 'lo has lograo campeón'
        else:
            return 'prueba de nuevo'
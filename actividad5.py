import csv
class PlanAhorro:
    __cod = ''
    __modelo = ''
    __version = ''
    __valor = ''
    __cuotas = ''
    __CantCuotasMin = ''

    def __init__(self, cod, mod, ver, valVeh, cuo, cantMin):
        self.__cod = int(cod)
        self.__modelo = mod
        self.__version = ver
        self.__valor = float(valVeh)
        self.__cuotas = int(cuo)
        self.__CantCuotasMin = int(cantMin)

    def __str__ (self):
        return "%s %s %s" %(self.__cod,self.__modelo,self.__version)
    
    def getValor(self):
        return (self.__valor)
    
    def getCuotas(self):
        return(self.__cuotas)
    
    def getCod(self):
        return(self.__cod)
    
    def getCantCuotasMIn(self):
        return(self.__CantCuotasMin)
    
    def getModelo(self):
        return(self.__modelo)
    
    def valorcuota(self):
        return ((self.__valor/self.__cuotas) + self.__valor * 0.10)
 
    def modificaCant(self,cant):
        self.__CantCuotasMin = cant

class ManejadorPlan:
    def __init__(self):
        self.__lista = []

    def agregarPlan(self,unPlan):
        self.__lista.append(unPlan)

    def testPlan(self):
        archivo = open('Planes.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            cod = int(fila[0])
            modelo = fila[1]
            version = fila[2]
            importe = float(fila[3])
            cuotas = int(fila[4])
            cant = fila [5]
            unPlan = PlanAhorro(cod,modelo,version,importe,cuotas,cant)
            self.agregarPlan(unPlan)
        archivo.close
        return
    
    def actualizaValorPlan(self):
        i = 0
        b = None
        while not b and i in range(len(self.__lista)):
            codigo = input('Ingrese codigo de plan a modificar valor del vehiculo: ')
            if(codigo == self.__lista[i].getCod()):
                print(self.__lista[i])
                importe = float(input('Ingrese nuevo valor del vehiculo: '))
                self.__lista[i].actualizaValor(importe)
                b = True
                print('Se modifico el valor del vehiculo')
        return
    
    def mostrarPlanes(self,importe):
        i = 0
        for i in range(len(self.__lista)):
            if(importe > self.__lista[i].valorcuota()):
                print(self.__lista[i])
        return
    
    def mostrarMontos(self):
        i = 0
        while (i<len(self.__lista)):
            codigo = input('Ingrese codigo de plan: ')
            if(codigo==self.__lista[i].getCod()):
                print('El monto que se debe haber pagado para licitar el vehiculo es: {}',self.__lista[i].getCantCuotasMIn() * self.__lista[i].valorcuota)
            else:
                i=i+1
        return
        
    def cambiarCuotas(self,codigo,cant):
        i = 0
        b = None
        while not b and i in range(len(self.__lista)):
            if(codigo == self.__lista[i].getCod()):
                self.__lista[i].modificaCant(cant)
                b = True
                print("Se modificaron las cuotas.")
        return
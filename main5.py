from actividad5 import ManejadorPlan

if __name__ == '__main__':
    lista = ManejadorPlan()
    lista.testPlan()
    opc = None

    while(opc != '0'):
        opc = input(''' --Menu--
        1) Actualizar valor de vehiculos.
        2) Mostrar planes con un importe 
        3) Monto Licitado
        4) Modificar cuotas
        0) Terminar con el programa
            ''')
        
        if opc == '1':
            lista.modificaPlanes()

        elif opc == '2':
            importe = float(input('Ingrese valor: '))
            lista.mostrarPlanes(importe)

        elif opc == '3':
            lista.mostrarMontos()

        elif opc == '4':
            codigo = int(input('Ingrese el codigo del vehiculo: '))
            cant = int(input('Ingrese las cuotas minimas para licitar: '))
            lista.cambiarCuotas(codigo,cant)
            
        elif opc == '0':
            print("Termino el progama")
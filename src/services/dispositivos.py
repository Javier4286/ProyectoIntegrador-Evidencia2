from src.services.clear_console import clear_console

def agregar_dispositivo(dispositivos):
    clear_console()
    dispositivo = {}

    nombre = input('\nIngrese nombre del dispositivo: ').strip().lower()
    if nombre:
        dispositivo['nombre'] = nombre
    else:
        clear_console()
        input('\n¡El nombre no puede estar vacio! Presione ENTER para continuar ')
        return

    tipo = input('\nIngrese tipo del dispositivo: ').strip().lower()
    if tipo:
        dispositivo['tipo'] = tipo
    else:
        clear_console()
        input('\n¡El tipo no puede estar vacio! Presione ENTER para continuar ')
        return

    estado_input = input('\nIngrese estado:\n\n1) - Encendido\n\n2) - Apagado\n\nOpción elegida: ')
    if estado_input.isdigit() and int(estado_input) in [1,2]:
        estado = int(estado_input)
        dispositivo['estado'] = 'Encendido' if estado == 1 else 'Apagado'
    else:
        clear_console()
        input('\n¡Entrada inválida! Presione ENTER para continuar ')
        return

    ubicacion = input('\nIngrese ubicación: ').strip().lower()

    if ubicacion:
        dispositivo['ubicacion'] = ubicacion
    else:
        clear_console()
        input('\n¡La ubicación no puede estar vacia! Presione ENTER para continuar ')
        return

    clear_console()

    esEsencial_input = input(
            f'\nUsted considera que el dispositivo: "{dispositivo["nombre"].capitalize()}" es esencial?\n\n1) - Sí\n\n2) - No\n\nOpción elegida: '
        )
    
    if esEsencial_input.isdigit() and int(esEsencial_input) in [1,2]:
        esEsencial = int(esEsencial_input)
        dispositivo['esencial'] = True if esEsencial == 1 else False
    else:
        clear_console()
        input('\n¡Entrada inválida! Presione ENTER para continuar ')
        return
    
    dispositivos.append(dispositivo)
    
    clear_console()
    input(
        f'\nDispositivo "{dispositivo["nombre"].capitalize()}" agregado con éxito!\n\nPresione ENTER para continuar '
    )


def buscar_dispositivo(dispositivos):
    clear_console()
    if len(dispositivos) == 0:
        input(
            '\nSin dispositivos disponibles\n\nPresione ENTER para continuar ')
    else:
        clear_console()
        opcion_buscar = int(
            input(
                '\nBuscar dispositivos\n\nA continuación ingrese el criterio de búsqueda:\n\n1) - Por nombre\n\n2) - Por tipo\n\n3) - Por estado\n\n4) - Por ubicación\n\n5) - Por esencialidad\n\n\n0) - Volver\n\nOpción elegida: '
            ))

        if opcion_buscar == 1:
            clear_console()
            buscar_nombre = input(
                '\nBuscar dispositivos por nombre\n\nA continuación ingrese el nombre del dispositivo a buscar:\n\n'
            ).lower()
            clear_console()

            encontrados = 0
            indice = 1

            for nombre in (dispositivos):
                if buscar_nombre == nombre['nombre'].lower():
                    if encontrados == 0:
                        print('\nDispositivos encontrados:\n')
                    print(f'\n{indice} - {nombre}\n')
                    encontrados += 1
                    indice += 1

            if encontrados == 0:
                clear_console()
                input(
                    f'\nNo se encontro "{buscar_nombre}"\n\nPresione ENTER para continuar '
                )
            else:
                input('\nPresione ENTER para continuar ')

        elif opcion_buscar == 2:
            clear_console()
            buscar_tipo = input(
                '\nBuscar dispositivos por tipo.\n\nA continuación ingrese el tipo del dispositivo a buscar:\n\n'
            ).lower()
            clear_console()

            encontrados = 0
            indice = 1

            for tipo in (dispositivos):
                if buscar_tipo == tipo['tipo'].lower():
                    if encontrados == 0:
                        print('\nDispositivos encontrados:\n')
                    print(f'\n{indice} - Nombre: {tipo['nombre']}    Tipo: {tipo['tipo']}    Estado: {tipo['estado']}    Ubicación: {tipo['ubicacion']}    Esencial: {'Sí' if tipo['esencial'] == True else 'No'}')
                    encontrados += 1
                    indice += 1

            if encontrados == 0:
                input(
                    f'\nNo se encontro "{buscar_tipo}"\n\nPresione ENTER para continuar '
                )
            else:
                input('\nPresione ENTER para continuar ')

        elif opcion_buscar == 3:
            clear_console()
            buscar_estado = input(
                '\nBuscar dispositivos por estado.\n\nA continuación ingrese el estado del dispositivo a buscar:\n\n'
            ).lower()
            clear_console()

            encontrados = 0
            indice = 1

            for estado in (dispositivos):
                if buscar_estado == estado['estado'].lower():
                    if encontrados == 0:
                        print('\nDispositivos encontrados:\n')
                    print(f'\n{indice} - Nombre: {estado['nombre']}    Tipo: {estado['tipo']}    Estado: {estado['estado']}    Ubicación: {estado['ubicacion']}    Esencial: {'Sí' if estado['esencial'] == True else 'No'}')

                    encontrados += 1
                    indice += 1

            if encontrados == 0:
                input(
                    f'\nNo se encontro "{buscar_estado}"\n\nPresione ENTER para continuar '
                )
            else:
                input('\nPresione ENTER para continuar ')

        elif opcion_buscar == 4:
            clear_console()
            buscar_ubicacion = input(
                '\nBuscar dispositivos por ubicación.\n\nA continuación ingrese el ubicación del dispositivo a buscar:\n\n'
            ).lower()
            clear_console()

            encontrados = 0
            indice = 1

            for ubicacion in (dispositivos):
                if buscar_ubicacion == ubicacion['ubicacion'].lower():
                    if encontrados == 0:
                        print('\nDispositivos encontrados:\n')
                    print(f'\n{indice} - Nombre: {ubicacion['nombre']}    Tipo: {ubicacion['tipo']}    Estado: {ubicacion['estado']}    Ubicación: {ubicacion['ubicacion']}    Esencial: {'Sí' if ubicacion['esencial'] == True else 'No'}')

                    encontrados += 1
                    indice += 1

            if encontrados == 0:
                input(
                    f'\nNo se encontro "{buscar_ubicacion}"\n\nPresione ENTER para continuar '
                )
            else:
                input('\nPresione ENTER para continuar ')

        elif opcion_buscar == 5:
            clear_console()
            buscar_esencialidad = int(
                input(
                    '\nBuscar dispositivos por esencialidad.\n\nA continuación indique si el dispositivo a buscar es esencialidad o no:\n\n1) - Sí\n\n2) - No\n\nOpción elegida: '
                ))
            clear_console()

            buscar_esencialidad = True if buscar_esencialidad == 1 else False

            encontrados = 0
            indice = 1

            for esencialidad in (dispositivos):
                if buscar_esencialidad == esencialidad['esencial']:
                    if encontrados == 0:
                        print('\nDispositivos encontrados:\n')
                    print(f'\n{indice} - Nombre: {esencialidad['nombre']}    Tipo: {esencialidad['tipo']}    Estado: {esencialidad['estado']}    Ubicación: {esencialidad['ubicacion']}    Esencial: {'Sí' if esencialidad['esencial'] == True else 'No'}')
                    encontrados += 1
                    indice += 1

            if encontrados == 0:
                input(
                    f'\nNo se encontro "{buscar_esencialidad}"\n\nPresione ENTER para continuar '
                )
            else:
                input('\nPresione ENTER para continuar ')

def ver_dispositivos(dispositivos, mostrarInput=True, noEsenciales=False, seccion_automatizacion=False):
    clear_console()

    hay_dispositivos = False

    if len(dispositivos) == 0:
        input(
            '\nSin dispositivos disponibles\n\nPresione ENTER para continuar ')
    else:

        if seccion_automatizacion == True:
            print('\nAutomatización aplicada en los siguientes dispositivos:\n')
        
        else:
            print('\nDispositivos disponibles:\n')

        if noEsenciales == False:
            for indice, dispositivo in enumerate(dispositivos, start=1):
                print(f'\n{indice} - Nombre: {dispositivo['nombre']}    Tipo: {dispositivo['tipo']}    Estado: {dispositivo['estado']}    Ubicación: {dispositivo['ubicacion']}    Esencial: {'Sí' if dispositivo['esencial'] == True else 'No'}')
                hay_dispositivos = True
        else:
            for indice, dispositivo in enumerate(dispositivos, start=1):
                if dispositivo['esencial'] == False:
                    print(f'\n{indice} - Nombre: {dispositivo['nombre']}    Tipo: {dispositivo['tipo']}    Estado: {dispositivo['estado']}    Ubicación: {dispositivo['ubicacion']}    Esencial: {'Sí' if dispositivo['esencial'] == True else 'No'}')
                    hay_dispositivos = True
        
        if not hay_dispositivos:
            input('\nSin dispositivos disponibles\n\nPresione ENTER para continuar ')

        if mostrarInput == True and hay_dispositivos:
            input('\nPresione ENTER para continuar ')
    
    return hay_dispositivos


def eliminar_dispositivo(dispositivos):
    ver_dispositivos(dispositivos, mostrarInput=False, noEsenciales=False)

    if len(dispositivos) > 0:
        opcion_eliminar = int(
            input(
                f'\n\nA continuación ingrese número de dispositivo a eliminar:\n\n0) - Volver\n\nOpción elegida: '
            ))
        if opcion_eliminar == 0:
            return
        else:
            clear_console()
            confirmar_eliminacion = int(
                input(
                    f'\n¿Está seguro que desea eliminar el dispositivo "{dispositivos[opcion_eliminar-1]['nombre'].capitalize()}"?\n\n1) - Sí\n\n2) - No\n\nOpción elegida: '
                ))
            if confirmar_eliminacion == 2:
                return
            else:
                clear_console()
                del dispositivos[opcion_eliminar - 1]
                input(
                    f'\n¡Dispositivo eliminado con éxito!\n\nPresione ENTER para continuar '
                )

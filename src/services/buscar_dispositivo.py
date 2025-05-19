from src.services.clear_console import clear_console


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
                    print(f'\n{indice} - {tipo}\n')
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
                    print(f'\n{indice} - {estado}\n')
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
                    print(f'\n{indice} - {ubicacion}\n')
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
                    print(f'\n{indice} - {esencialidad}\n')
                    encontrados += 1
                    indice += 1

            if encontrados == 0:
                input(
                    f'\nNo se encontro "{buscar_esencialidad}"\n\nPresione ENTER para continuar '
                )
            else:
                input('\nPresione ENTER para continuar ')

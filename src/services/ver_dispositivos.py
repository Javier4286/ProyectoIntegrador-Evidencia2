from src.services.clear_console import clear_console


def ver_dispositivos(dispositivos, mostrarInput=True, noEsenciales=False):
    clear_console()

    hay_dispositivos = False

    if len(dispositivos) == 0:
        input(
            '\nSin dispositivos disponibles\n\nPresione ENTER para continuar ')
    else:
        print('\nDispositivos disponibles:\n')

        if noEsenciales == False:
            for indice, dispositivo in enumerate(dispositivos, start=1):
                print(f'\n{indice} - Nombre: {dispositivo['nombre']}    Tipo: {dispositivo['tipo']}    Estado: {dispositivo['estado']}    Ubicación: {dispositivo['ubicacion']}    Esencial: {'Sí' if dispositivo['esencial'] == True else 'No'}')
                hay_dispositivos = True
        else:
            for indice, dispositivo in enumerate(dispositivos, start=1):
                if dispositivo['esencial'] == False:
                    print(f'\n{indice} - Nombre: {dispositivo['nombre']}    Tipo: {dispositivo['tipo']}    Estado: {dispositivo['estado']}    Ubicación: {dispositivo['ubicacion']}    Esencial: {dispositivo['esencial']}')
                    hay_dispositivos = True
        
        if not hay_dispositivos:
            input('\nSin dispositivos disponibles\n\nPresione ENTER para continuar ')

        if mostrarInput == True and hay_dispositivos:
            input('\nPresione ENTER para continuar ')
    
    return hay_dispositivos
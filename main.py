from src.services.agregar_dispositivo import agregar_dispositivo
from src.services.buscar_dispositivo import buscar_dispositivo
from src.services.clear_console import clear_console
from src.services.ver_dispositivos import ver_dispositivos
from src.services.eliminar_dispositivo import eliminar_dispositivo

dispositivos = []

while True:
    clear_console()
    menu = int(
        input(
            '\nBienvenidos al Sistema SmartHome Solutions\n\nA continuación, elija una opción:\n\n1) - Gestionar los dispositivos\n\n2) - Gestionar automatizaciones\n\n\n' \
            '0) - Salir\n\nOpción elegida: '
        ))
    if menu == 1:
        while True:
            clear_console()
            menu_dispositivos = int(
                input(
                    '\nGestión de dispositivos\n\n1) - Agregar nuevo dispositivo\n\n2) - Ver todos los dispositivos disponibles\n\n3) - Buscar dispositivos\n\n4) - Eliminar dispositivos\n\n\n0) - Volver\n\nOpción elegida: '
                ))

            if menu_dispositivos == 1:
                agregar_dispositivo(dispositivos)

            elif menu_dispositivos == 2:
                ver_dispositivos(dispositivos,
                                 mostrarInput=True,
                                 noEsenciales=False)

            elif menu_dispositivos == 3:
                buscar_dispositivo(dispositivos)

            elif menu_dispositivos == 4:
                eliminar_dispositivo(dispositivos)

            else:
                break

    elif menu == 2:
        clear_console()
        menu_automatizaciones = int(
            input(
                '\nA continuación seleccione una automatización:\n\n1) - Modo ahorro de energía\n\n\n0) - Volver\n\nOpción elegida: '
            ))

        if menu_automatizaciones == 0:
            continue

        clear_console()

        aviso_automatizacion = int(
            input(
                '\nEl modo "ahorro de energía" es una funcionalidad que apaga todos los dispositivos no esenciales\n\n¿Desea continuar con esta automatización?\n\n1) - Sí\n\n2) - No\n\nOpción elegida: '
            ))

        if menu_automatizaciones == 1 and aviso_automatizacion == 1:

            if not ver_dispositivos(
                    dispositivos, mostrarInput=False, noEsenciales=True):
                continue

            nombre_automatizacion = input(
                '\nIngrese nombre de dispositivo a automatizar: ')

            for dispositivo in dispositivos:
                if dispositivo['nombre'] == nombre_automatizacion:
                    dispositivo['estado'] = 'Apagado'

            ver_dispositivos(dispositivos,
                             mostrarInput=True,
                             noEsenciales=True)

        else:
            continue

    else:
        clear_console()
        print('\n¡Muchas gracias por utilizar nuestros servicios.!\n')
        break

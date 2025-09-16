from src.services.clear_console import clear_console
from src.services.dispositivos import ver_dispositivos
from src.services.mensaje_en_espera import mensaje_en_espera

automatizaciones = []


def gestionar_automatizaciones(dispositivos):
    while True:
        automatizacion = {}
        clear_console()
        menu = input(
            '\nA continuación seleccione una automatización:\n\n1) - Modo ahorro de energía\n\n\n0) - Volver\n\nOpción elegida: '
        )

        if menu.isdigit() and int(menu) in [0, 1]:
            opcion = int(menu)

            if opcion == 0:
                break

        else:
            clear_console()
            input('\n¡Opción inválida!\n\nPresione ENTER para continuar ')
            continue

        clear_console()
        aviso_automatizacion = input(
            '\nEl modo "ahorro de energía" es una funcionalidad que apaga todos los dispositivos no esenciales\n\n¿Desea continuar con esta automatización?\n\n1) - Sí\n\n2) - No\n\nOpción elegida: '
        )

        if aviso_automatizacion.isdigit() and int(aviso_automatizacion) in [1, 2]:
            continuar_automatizacion = int(aviso_automatizacion)

        else:
            clear_console()
            input('\n¡Opción inválida!\n\nPresione ENTER para continuar ')
            continue

        if opcion == 1 and continuar_automatizacion == 1:

            if not ver_dispositivos(
                    dispositivos, mostrarInput=False, noEsenciales=True):
                continue

            confirmar_automatizacion = input(
                '\n¿Confirma la activación del "Modo Ahorro de Energía"?\n\n1) - Sí\n\n2) - No\n\n\nOpción elegida: ')

            if confirmar_automatizacion.isdigit() and int(confirmar_automatizacion) in [1, 2]:
                automatizacion_implementada = int(confirmar_automatizacion)

                if automatizacion_implementada == 1:

                    for dispositivo in dispositivos:
                        if dispositivo['esencial'] == False:
                            dispositivo['estado'] = 'Apagado'

                    mensaje_en_espera(mensaje='automatización')
                    automatizacion['nombre'] = 'Modo ahorro de energía'
                    automatizacion['activa'] = 'Sí'
            else:
                clear_console()
                input('\n¡Opción inválida!\n\nPresione ENTER para continuar ')
                break

            for i in automatizaciones:
                if i['nombre'] == 'Modo ahorro de energía':
                    break
            else:
                automatizaciones.append(automatizacion)
            ver_dispositivos(dispositivos,
                             noEsenciales=True, seccion_automatizacion=True)
        else:
            break


def consultar_automatizaciones():
    global automatizaciones
    if len(automatizaciones) == 0:
        input('\nSin automatizaciones disponibles\n\nPresione ENTER para continuar ')

    else:
        print('\nAutomatizaciones activas.\n')
        for indice, automatizacion in enumerate(automatizaciones, start=1):
            print(
                f'{indice} - Nombre: {automatizacion['nombre']} - Activa: {automatizacion['activa']}')
        input('\nPresione ENTER para continuar ')

from src.services.clear_console import clear_console
from src.services.dispositivos import ver_dispositivos
from src.services.mensaje_en_espera import mensaje_en_espera


def automatizaciones(dispositivos):
    while True:
        clear_console()
        menu_automatizaciones = int(
            input(
                '\nA continuación seleccione una automatización:\n\n1) - Modo ahorro de energía\n\n\n0) - Volver\n\nOpción elegida: '
            ))

        if menu_automatizaciones == 0:
            break

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

            mensaje_en_espera(mensaje='automatización')

            ver_dispositivos(dispositivos,
                             mostrarInput=True,
                             noEsenciales=True)
        else:
            break

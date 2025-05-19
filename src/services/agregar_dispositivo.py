from src.services.clear_console import clear_console


def agregar_dispositivo(dispositivos):
    clear_console()
    dispositivo = {}
    dispositivo['nombre'] = input('\nIngrese nombre del dispositivo: ').lower()
    clear_console()
    dispositivo['tipo'] = input('\nIngrese tipo: ').lower()
    clear_console()
    dispositivo['estado'] = int(
        input(
            '\nIngrese estado:\n\n1) - Encendido\n\n2) - Apagado\n\nOpción elegida: '
        ))
    dispositivo[
        'estado'] = 'Encendido' if dispositivo['estado'] == 1 else 'Apagado'
    clear_console()
    dispositivo['ubicacion'] = input('\nIngrese ubicación: ').lower()
    clear_console()
    esEsencial = int(
        input(
            f'\nUsted considera que el dispositivo: "{dispositivo["nombre"]}" es esencial?\n\n1) - Sí\n\n2) - No\n\nOpción elegida: '
        ))
    esEsencial = True if esEsencial == 1 else False
    dispositivo['esencial'] = esEsencial
    dispositivos.append(dispositivo)
    clear_console()
    input(
        f'\nDispositivo "{dispositivo["nombre"]}" agregado con éxito!\n\nPresione ENTER para continuar '
    )

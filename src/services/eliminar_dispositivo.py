from src.services.ver_dispositivos import ver_dispositivos
from src.services.clear_console import clear_console


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
                    f'\n¿Está seguro que desea eliminar el dispositivo "{dispositivos[opcion_eliminar-1]}"?\n\n1) - Sí\n\n2) - No\n\nOpción elegida: '
                ))
            if confirmar_eliminacion == 2:
                return
            else:
                clear_console()
                del dispositivos[opcion_eliminar-1]
                input(
                    f'\n¡Dispositivo eliminado con éxito!\n\nPresione ENTER para continuar '
                )

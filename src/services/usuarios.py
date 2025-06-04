from src.services.clear_console import clear_console
from src.services.automatizaciones import automatizaciones
from src.services.mensaje_en_espera import mensaje_en_espera
from src.services.dispositivos import agregar_dispositivo, buscar_dispositivo, ver_dispositivos, eliminar_dispositivo

usuarios = [{
    'nombre': 'admin',
    'apellido': '',
    'email': 'admin@admin.com.ar',
    'rol': 'admin'
}]


def crear_usuario():
    clear_console()
    usuario = {}
    usuario['nombre'] = input(
        '\nRegistrar nuevo usuario.\n\nIngrese nombre: ').lower()
    usuario['apellido'] = input('\nIngrese apellido: ').lower()
    usuario['email'] = input('\nIngrese email: ').lower()
    usuario['rol'] = ''
    usuarios.append(usuario)
    clear_console()
    input(
        f'\n¡Usuario "{usuario["nombre"].capitalize()}" creado con éxito!\n\nPresione ENTER para continuar '
    )


def iniciar_sesion(dispositivos):
    while True:
        clear_console()
        print(
            '\nIniciar Sesión.\n\nA continuación, ingrese sus datos en los campos correspondientes o ingrese "exit" en algunos de ellos para volver.\n\n'
        )

        nombre_ingresado = input('Nombre de usuario: ').lower()
        if nombre_ingresado == 'exit':
            return

        email_ingresado = input('\nEmail: ').lower()
        if email_ingresado == 'exit':
            return

        for usuario in usuarios:
            if nombre_ingresado == usuario['nombre'].lower(
            ) and email_ingresado == usuario['email'].lower(
            ) and usuario['rol'] == 'admin':
                mensaje_en_espera(mensaje='datos')

                while True:
                    clear_console()
                    menu_admin = int(
                        input('\n1) - Consultar automatizaciones activas\n\n2) - Gestionar dispositivos\n\n3) - Modificar rol del usuario\n\n\n0) - Volver\n\nOpción elegida: '))

                    if menu_admin == 0:
                        return

                    elif menu_admin == 1:
                        pass

                    elif menu_admin == 2:
                        while True:
                            menu_usuarios = int(
                                input(
                                    '\nGestión de dispositivos\n\n1) - Agregar nuevo dispositivo\n\n2) - Ver todos los dispositivos disponibles\n\n3) - Buscar dispositivos\n\n4) - Eliminar dispositivos\n\n\n0) - Volver\n\nOpción elegida: '
                                ))

                            if menu_usuarios == 1:
                                agregar_dispositivo(dispositivos)

                            elif menu_usuarios == 2:
                                ver_dispositivos(dispositivos)

                            elif menu_usuarios == 3:
                                buscar_dispositivo(dispositivos)

                            elif menu_usuarios == 4:
                                eliminar_dispositivo(dispositivos)

                            else:
                                break

                    elif menu_admin == 3:
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
                                    del dispositivos[opcion_eliminar - 1]
                                    input(
                                        f'\n¡Dispositivo eliminado con éxito!\n\nPresione ENTER para continuar '
                                    )

            else:
                if nombre_ingresado == usuario['nombre'].lower(
                ) and email_ingresado == usuario['email'].lower():
                    mensaje_en_espera(mensaje='datos')

                    while True:
                        clear_console()
                        menu_usuario = int(
                            input(
                                '\n1) - Consultar datos personales\n\n2) - Ejecutar automatizaciones\n\n3) - Consultar dispositivos\n\n\n0) - Cerrar Sesión\n\nOpción elegida: '
                            ))

                        if menu_usuario == 0:
                            return

                        elif menu_usuario == 1:
                            clear_console()
                            input(
                                f'\nDatos Personales.\n\nNombre: {usuario["nombre"].capitalize()}\n\nApellido: {usuario["apellido"].capitalize()}\n\nEmail: {usuario["email"]}\n\nPresione ENTER para continuar '
                            )

                        elif menu_usuario == 2:
                            automatizaciones(dispositivos)

                        elif menu_usuario == 3:
                            ver_dispositivos(dispositivos)
        else:
            clear_console()
            input(
                '\n¡Usuario no encontrado!\n\nPresione ENTER para continuar ')

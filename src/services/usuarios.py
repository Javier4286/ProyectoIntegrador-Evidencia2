from src.services.clear_console import clear_console
from src.services.automatizaciones import automatizaciones, gestionar_automatizaciones, consultar_automatizaciones
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

    usuario['rol'] = 'estandar'

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
                    menu_admin = input(
                        f'\n¡Bienvenido {usuario["nombre"]}!\n\n1) - Consultar automatizaciones activas\n\n2) - Gestionar dispositivos\n\n3) - Modificar rol de usuario\n\n\n0) - Cerrar Sesión\n\nOpción elegida: '
                    )

                    if menu_admin.isdigit() and int(menu_admin) in [0, 1, 2, 3]:
                        opcion = int(menu_admin)

                        if opcion == 0:
                            return

                        elif opcion == 1:
                            clear_console()
                            consultar_automatizaciones()

                        elif opcion == 2:
                            while True:
                                clear_console()

                                menu_usuarios = input(
                                    '\nGestión de dispositivos\n\n1) - Agregar nuevo dispositivo\n\n2) - Ver todos los dispositivos disponibles\n\n3) - Buscar dispositivos\n\n4) - Eliminar dispositivos\n\n\n0) - Volver\n\nOpción elegida: '
                                )

                                if not menu_usuarios.isdigit() or int(menu_usuarios) not in range(0, 5):
                                    clear_console()
                                    input(
                                        '\n¡Entrada inválida! Presione ENTER para continuar ')
                                    continue

                                opcion = int(menu_usuarios)

                                if opcion == 1:
                                    agregar_dispositivo(dispositivos)

                                elif opcion == 2:
                                    ver_dispositivos(dispositivos)

                                elif opcion == 3:
                                    buscar_dispositivo(dispositivos)

                                elif opcion == 4:
                                    eliminar_dispositivo(dispositivos)

                                elif opcion == 0:
                                    break

                                else:
                                    clear_console()
                                    input(
                                        '\n¡Entrada inválida! Presione ENTER para continuar ')
                                    return

                        elif opcion == 3:
                            clear_console()
                            if len(usuarios) > 0:
                                print('\nModificar rol de usuario.')

                                for indice, user in enumerate(usuarios):
                                    if user['nombre'] == 'admin' and user['rol'] == 'admin':
                                        continue
                                    print(
                                        f'\n{indice} - Nombre: {user['nombre']}   Apellido: {user['apellido']}     Email: {user['email']}     Rol: {user['rol']}')

                                opcion_modificar = int(
                                    input(
                                        '\n\nA continuación ingrese número de usuario a modificar:\n\n0) - Volver\n\nOpción elegida: '
                                    ))

                                if opcion_modificar == 0:
                                    continue

                                else:
                                    clear_console()
                                    confirmar_modificacion_input = input(
                                        f'\n¿Está seguro que desea modificar el rol de usuario "{usuarios[opcion_modificar]['nombre'].capitalize()}"?\n\n1) - Sí\n\n2) - No\n\nOpción elegida: '
                                    )

                                    if confirmar_modificacion_input.isdigit() and int(confirmar_modificacion_input) in [1, 2]:
                                        confirmar_modificacion = int(
                                            confirmar_modificacion_input)

                                    else:
                                        clear_console()
                                        input(
                                            '\n¡Entrada inválida! Presione ENTER para continuar ')
                                        return

                                    if confirmar_modificacion == 2:
                                        continue

                                    else:
                                        usuarios[opcion_modificar]['rol'] = 'admin' if usuarios[
                                            opcion_modificar]['rol'] == 'estandar' else 'estandar'
                                        clear_console()
                                        input(
                                            '\n¡Rol de usuario actualizado con éxito!\n\nPresione ENTER para continuar '
                                        )
                    else:
                        clear_console()
                        input('\n¡Opción inválida!\n\nPresione ENTER para continuar ')

            else:
                if nombre_ingresado == usuario['nombre'].lower(
                ) and email_ingresado == usuario['email'].lower():
                    mensaje_en_espera(mensaje='datos')

                    while True:
                        clear_console()
                        menu_usuario_input = input(
                            f'\n¡Bienvenido {usuario["nombre"].capitalize()}!\n\n1) - Consultar datos personales\n\n2) - Ejecutar automatizaciones\n\n3) - Consultar dispositivos\n\n\n0) - Cerrar Sesión\n\nOpción elegida: '
                        )

                        if menu_usuario_input.isdigit() and int(menu_usuario_input) in [0, 1, 2, 3]:
                            menu_usuario = int(menu_usuario_input)

                        else:
                            clear_console()
                            input(
                                '\n¡Entrada inválida! Presione ENTER para continuar ')
                            return

                        if menu_usuario == 0:
                            return

                        elif menu_usuario == 1:
                            clear_console()
                            input(
                                f'\nDatos Personales.\n\nNombre: {usuario["nombre"].capitalize()}\n\nApellido: {usuario["apellido"].capitalize()}\n\nEmail: {usuario["email"]}\n\nPresione ENTER para continuar '
                            )

                        elif menu_usuario == 2:
                            clear_console()
                            gestionar_automatizaciones(dispositivos)

                        elif menu_usuario == 3:
                            ver_dispositivos(dispositivos)
        else:
            clear_console()
            input(
                '\n¡Usuario no encontrado!\n\nPresione ENTER para continuar ')

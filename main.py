from src.services.clear_console import clear_console
from src.services.usuarios import crear_usuario
from src.services.usuarios import iniciar_sesion

dispositivos = []

while True:
    clear_console()
    opcion_elegida = input(
        '\nBienvenidos al Sistema SmartHome Solutions\n\nA continuación, elija una opción:\n\n1) - Iniciar Sesión\n\n2) - Registrarse\n\n\n0) - Salir\n\nOpción elegida: '
    )

    if opcion_elegida.isdigit() and int(opcion_elegida) in [0, 1, 2]:
        opcion = int(opcion_elegida)

        if opcion == 1:
            iniciar_sesion(dispositivos)

        elif opcion == 2:
            crear_usuario()

        elif opcion == 0:
            clear_console()
            print('\n¡Muchas gracias por utilizar nuestros servicios!\n')
            break
    else:
        clear_console()
        input('\n¡Opción inválida!\n\nPresione ENTER para continuar ')


'''
Nombre de usuario: 'admin'
Email: 'admin@admin.com.ar'
'''

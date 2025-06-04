from src.services.clear_console import clear_console
from src.services.usuarios import crear_usuario
from src.services.usuarios import iniciar_sesion

dispositivos = []

while True:
    clear_console()
    menu = int(
        input(
            '\nBienvenidos al Sistema SmartHome Solutions\n\nA continuación, elija una opción:\n\n1) - Iniciar Sesión\n\n2) - Registrarse\n\n\n0) - Salir\n\nOpción elegida: '
        ))
    if menu == 1:
        iniciar_sesion(dispositivos)

    elif menu == 2:
        crear_usuario()

    else:
        clear_console()
        print('\n¡Muchas gracias por utilizar nuestros servicios!\n')
        break
'''
'Revisar los nombres de las variables para una mejor lectura. Quizás se lea mejor opcion_elegida u opcion en lugar de menu_dispositivo.'
No se encontró 'menu_dispositivo' para realizar correción solicitada.-
'''

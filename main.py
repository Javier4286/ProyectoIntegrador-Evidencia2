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

# file:///F:/ISPC/Tecnicatura%20Superior%20en%20Desarrollo%20de%20Software%20(Res%20111324)/1%C2%B0%20A%C3%91O/Programador%20-%20TSDS%20-%202025/Evidencias%20de%20Aprendizaje/Evidencia%20de%20aprendizaje%20N%C2%B0%202/ProyectoIntegrador-Evidencia3.pdf

# comentario de prueba Mariel Jimenez
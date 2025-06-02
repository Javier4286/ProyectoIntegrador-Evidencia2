from src.services.clear_console import clear_console
from src.services.automatizaciones import automatizaciones
from src.services.dispositivos import ver_dispositivos

usuarios =[]

def crear_usuario():
    clear_console()
    usuario = {}
    usuario['nombre'] = input('\nIngrese nombre de nuevo usuario: ').lower()
    clear_console()
    usuario['apellido'] = input('\nIngrese su apellido: ').lower()
    clear_console()
    usuario['email'] = input('\nIngrese su email: ').lower()
    usuario['rol'] = ''
    clear_console()
    usuarios.append(usuario)
    clear_console()
    print(usuarios)
    input(
        f'\nUsuario creado con exito!\n\nPresione ENTER para continuar '
    )

def iniciar_sesion(dispositivos):
    clear_console()
    usuario_registrado = {}
    usuario_registrado['nombre'] = input('\nIniciar sesion\n\nIngrese nombre de usuario: ').lower()
    usuario_registrado['email'] = input('\nIngrese email: ').lower()

    for usuario in usuarios:
        if usuario_registrado['nombre'] == usuario['nombre'].lower() and usuario_registrado['email'] == usuario['email'].lower():
            clear_console()
            while True:
                menu_usuario = int(input('\n1) - Consultar datos personales\n\n2) - Ejecutar automatizaciones\n\n3) - Consultar dispositivos\n\n\n0) - Volver\n\nOpcion elegida: '))

                if menu_usuario == 1:
                    clear_console()
                    print(usuario)
                    input('\n\nPresione ENTER para continuar ')
                
                elif menu_usuario == 2:
                    clear_console()
                    automatizaciones(dispositivos)
                
                elif menu_usuario == 3:
                    clear_console()
                    ver_dispositivos(dispositivos)
                
                else:
                    break
                    
        else:
            print("usuario no regristrado")
            input()
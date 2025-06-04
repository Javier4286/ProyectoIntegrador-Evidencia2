from src.services.clear_console import clear_console
import time


def mensaje_en_espera(mensaje):
    while True:
        if mensaje == 'automatización':
            string = '\nAplicando automatización...\n\nEspere por favor'

        elif mensaje == 'datos':
            string = '\nComprobando datos...\n\nEspere por favor'

        for i in range(0, 5):
            time.sleep(1)
            string += ' .'
            clear_console()
            print(string, end=' ')

        if mensaje == 'automatización':
            string = '\n¡Automatización implementada con éxito!\n\nRedirigiendo'

            for i in range(0, 4):
                time.sleep(1)
                string += ' .'
                clear_console()
                print(string, end=' ')

        elif mensaje == 'datos':
            string = '\n¡Comprobación de datos exitosa!\n\nRedirigiendo'

            for i in range(0, 4):
                time.sleep(1)
                string += ' .'
                clear_console()
                print(string, end=' ')
        break

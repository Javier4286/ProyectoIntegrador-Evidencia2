from src.services.clear_console import clear_console
import time


def mensaje_en_espera(sustantivo, adjetivo):
    while True:
        clear_console()
        time.sleep(0.25)
        string = f'\nAplicando {sustantivo}...\n\nEspere por favor'

        for i in range(0, 7):
            time.sleep(1)
            # string += '.\n' <=== a considerar...
            string += ' .'
            clear_console()
            print(string)
        clear_console()
        input(
            f'\n¡{sustantivo} {adjetivo} con éxito!\n\n\nPresione ENTER para continuar '
        )
        clear_console()
        break

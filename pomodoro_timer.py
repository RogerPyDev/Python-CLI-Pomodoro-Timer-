import time # La usaremos para la funcionalidad de temporización
import sys # La usaremos para salir del programa en caso de interrupciones

WORK_TIME = 25 # Duración de una sesión de trabajo en minutos
SHORT_BREAK = 5 # Duración del descanso corto en minutos
LONG_BREAK = 15 # Duración del descanso largo en minutos
CYCLES = 4 # Número de ciclos de trabajo antes de un descanso largo

# Usamos nombres en mayúscular para indicar que son variables constantes, cuyos valores no deberian cambiar

def countdown(minutes):
# Función que ejecuta una cuenta regresiva y muestra el tiempo restante.
    seconds = minutes * 60 # Convertimos minutos a segundos
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02}:{secs:02}"
            print(f"\r⏳ Tiempo restante: {timer}", end="")
            time.sleep(1)
            seconds -= 1
        print("\n⏰⏰ ¡Felicidades, has terminado tu sesión!")
    except KeyboardInterrupt:
        print("\n⏹⏹⏹ Temporizador detenido por el usuario")
        sys.exit()
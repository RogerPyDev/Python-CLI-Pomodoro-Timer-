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
    try: # Intentamos ejecutar el código
        while seconds > 0: # Mientras queden segundos
            mins, secs = divmod(seconds, 60) # Dividimos los segundos en minutos y segundos
            timer = f"{mins:02}:{secs:02}" # Formateamos el tiempo en formato MM:SS
            print(f"\r⏳ Tiempo restante: {timer}", end="") # Mostramos el tiempo restante
            time.sleep(1) # Esperamos 1 segundo
            seconds -= 1 # Reducimos el tiempo en 1 segundo
        print("\n⏰⏰ ¡Felicidades, has terminado tu sesión!") # Mostramos un mensaje cuando se acaba el tiempo
    except KeyboardInterrupt: 
        print("\n⏹⏹⏹ Temporizador detenido por el usuario") # Mostramos un mensaje si el usuario interrumpe el temporizador
        sys.exit() # Salimos del programa
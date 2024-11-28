# Python-CLI-Pomodoro-Timer-
**Python CLI Pomodoro Timer** es una herramienta simple y efectiva para implementar la técnica Pomodoro directamente en la terminal. Permite configurar y gestionar ciclos de trabajo y descanso, mejorando la productividad. Desarrollado en Python, es ideal para aprender y practicar aplicaciones CLI.

**Descripción del Proyecto:**

Este proyecto, **Python CLI Pomodoro Timer**, es una herramienta desarrollada en Python para implementar la técnica Pomodoro, diseñada para mejorar la productividad y la gestión del tiempo. Funciona directamente en la terminal (CLI), permitiendo a los usuarios iniciar ciclos de trabajo y descanso con un temporizador interactivo, sin necesidad de interfaces gráficas ni dependencias externas.

**Características principales:**

- **Fácil de usar**: Comandos simples e intuitivos para iniciar, pausar y reiniciar el temporizador.
- **Personalizable**: Configura la duración de las sesiones de trabajo, descansos cortos y largos.
- **Notificaciones visuales**: Indicadores claros en la consola para transiciones entre ciclos.
- **100% Python**: Implementación pura en Python para aprendizaje y uso práctico.

Este proyecto es ideal para quienes desean una herramienta minimalista para aumentar su concentración y productividad, además de ser una excelente práctica para desarrolladores interesados en construir aplicaciones CLI en Python.

# ⏳ Pomodoro Timer CLI

Un **Pomodoro Timer** interactivo para la consola, diseñado en Python. Este programa permite gestionar sesiones de trabajo y descansos usando la técnica Pomodoro, ayudando a aumentar la productividad y la concentración.

---

## 🚀 **Características**
- Sesiones configurables de:
  - **Trabajo**: 25 minutos.
  - **Descanso corto**: 5 minutos.
  - **Descanso largo**: 15 minutos.
- Ciclo completo de **4 sesiones de trabajo**, seguido de un descanso largo.
- Interfaz amigable en la consola con actualizaciones dinámicas del temporizador.
- Manejador de interrupciones para detener el programa limpiamente.

---

## 🛠️ **Requisitos del Sistema**
- **Python 3.6 o superior**.
- Compatible con Windows, macOS y Linux.

---

## 📥 **Instalación**
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/RogerPyDev/Python-CLI-Pomodoro-Timer-

2. Navega al directorio del proyecto:
   ```bash
   cd pomodoro-timer-cli

3. (Opcional) Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para macOS/Linux
   venv\Scripts\activate     # Para Windows

5. Ejecuta el programa:
   ```bash
   python pomodoro_timer.py

---

## 🖥️ **Uso**
1. Al iniciar el programa, selecciona la opción 1 para empezar el ciclo Pomodoro.
2. Sigue las instrucciones para completar sesiones de trabajo y descansos.
3. Selecciona la opción 2 para salir del programa.

---

## 📝 **Ejemplo de Uso**
    ```bash
     Menu:
    1. Iniciar Pomodoro Timer
    2. Salir
    Selecciona una opción (1 o 2): 1

    🔄 Ciclo 1 de 4
    ⏳ Inicia tu sesión de trabajo...
    ⏳ Tiempo restante: 24:59
    ...
    ⏰ ¡Tiempo cumplido!
    🛌 Tómate un descanso corto de 5 minutos.
    ⏳ Tiempo restante: 04:59
    ...

---

## ✨ **Personalización**
Puedes ajustar los valores de las sesiones en el archivo pomodoro_timer.py modificando las siguientes variables al inicio del script:
   ```bash
       Menu:
        WORK_TIME = 25  # Duración de la sesión de trabajo (en minutos)
        SHORT_BREAK = 5  # Duración de un descanso corto (en minutos)
        LONG_BREAK = 15  # Duración de un descanso largo (en minutos)
        CYCLES = 4  # Número de ciclos antes del descanso largo

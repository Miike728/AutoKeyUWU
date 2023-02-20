import time
import random
import pyautogui
import keyboard
from datetime import datetime, timedelta

# ejecución inicial
print(f"Script iniciado")
time.sleep(3)
keyboard.press_and_release('win+7')
time.sleep(0.1)
pyautogui.write("uwu")
time.sleep(0.4)
pyautogui.press('enter')
time.sleep(0.5)
keyboard.press_and_release('win+1')

while True:
    # generar tiempo aleatorio
    minutos = random.randint(30, 60)
    segundos = random.randint(0, 59)
    tiempo = f"Tiempo generado: {minutos} minutos y {segundos} segundos"
    print(f"Comando ejecutado a las: {datetime.now().strftime('%H:%M:%S')}")
    print(tiempo + " - Siguiente ejecución: " + (datetime.now() + timedelta(minutes=minutos, seconds=segundos)).strftime('%H:%M:%S'))

    # esperar el tiempo aleatorio
    time.sleep(minutos * 60 + segundos)

    # ir a la ventana 7 y escribir el texto
    keyboard.press_and_release('win+7')
    time.sleep(0.1)
    pyautogui.write("uwu")
    time.sleep(0.4)
    pyautogui.press('enter')

    # volver a la ventana 1
    time.sleep(0.2)
    keyboard.press_and_release('win+1')

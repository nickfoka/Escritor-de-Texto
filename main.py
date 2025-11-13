import os
import time
import keyboard

a = input("insira a redacao:\n")
time.sleep(4)
keyboard.write(a, delay=0.03)
os.system("cls")
print("Texto foi escrito!")
input("Pressione qualquer tecla para fechar...")

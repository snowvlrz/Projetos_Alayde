import pyautogui
import time

print("Vamos calcular! \n")
numero1 = input("Digite o primeiro Nº: ")
operacao = input("Digite a operação (+, -, *, /): ")
numero2 = input("Digite o segundo Nº: ")
pyautogui.press('win')
pyautogui.write('calculadora')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write(numero1)
pyautogui.write(operacao)
pyautogui.write(numero2)
pyautogui.press('enter')
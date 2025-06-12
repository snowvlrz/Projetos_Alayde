import pyautogui
import time

print("Boas vindas! \n")
escolha = str(input("Qual Programa Você Quer Abrir?\n Word \n Excel \n Chrome \n Resposta: "))
if escolha == "word":
 pyautogui.press('win')
 pyautogui.write('word')
 pyautogui.press('enter')
 time.sleep(2)
 pyautogui.press('enter')

elif escolha == "excel":
 pyautogui.press('win')
 pyautogui.write('excel')
 pyautogui.press('enter')
 time.sleep(5)
 pyautogui.press('enter')

elif escolha == "chrome":
 pyautogui.press('win')
 pyautogui.write('chrome')
 pyautogui.press('enter')
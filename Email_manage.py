import pyautogui
import time

#If the PC is a potato
pyautogui.PAUSE = 0.5

#abrir o fences
pyautogui.press('winleft')
pyautogui.write('fences')
pyautogui.press('enter')

#clicar em 'start trial'
time.sleep(1)
position = pyautogui.locateCenterOnScreen(r"Assets\Start_30_Day_Trial.png")
pyautogui.click(position)

#TODO: 3- criar um email temporario

#TODO: 4- informar esse email temporario para o fences

#TODO: 5- clica em proximo

#TODO: 6- verificar a caixa de mensagens do email

#TODO: 7- clicar no link dentro do email recebido

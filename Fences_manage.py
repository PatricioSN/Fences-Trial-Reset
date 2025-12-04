import pyautogui
import time

#If the PC is a potato
pyautogui.PAUSE = 0.5

#Open fences
def open_fences():
    pyautogui.press('winleft')
    pyautogui.write('fences')
    pyautogui.press('enter')
open_fences()

#click on 'start trial'
time.sleep(1)
def start_trial():
    try:
        position = pyautogui.locateCenterOnScreen(r"Assets\Start_30_Day_Trial.png")
    #Tries two times, because the fences have a problem sometimes. If you immediately delete the cache, maybe the program doesn't open the screen of the trial test
    except pyautogui.ImageNotFoundException:
        pyautogui.hotkey('alt','f4')
        time.sleep(0.5)
        open_fences()
        position = pyautogui.locateCenterOnScreen(r"Assets\Start_30_Day_Trial.png")
    pyautogui.click(position)
start_trial()

#criar um email temporario
#(preciso adaptar a classe para copiar o email, informar ao fences, e só depois ela prosseguir)

#TODO: 4- informar esse email temporario para o fences

#TODO: 5- clica em proximo

#verificar a caixa de mensagens do email

#clicar no link dentro do email recebido

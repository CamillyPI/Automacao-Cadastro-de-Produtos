import pyautogui # biblioteca para automacao - baixada
import time # biblioteca de tempo - ja vem baixada
import pandas # biblioteca de dados - baixada

pyautogui.PAUSE = 0.5 # pausar 0,5 seguntos entre cada comando

pyautogui.press("win") # pressione

pyautogui.write("microsoft edge") # escreva

pyautogui.press("enter")

pyautogui.click(x=470, y=52) # clique
# time.sleep(5)
# print(pyautogui.position()) 
# para saber a posicao

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # criando variavel para deixar o codigo clean

pyautogui.write(link)

pyautogui.press("enter")
time.sleep(3) # tempo de espera depois de executar acao acima

pyautogui.click(x=736, y=359)

login = "exemplodelogin@gmail.com" # criando variavel para deixar o codigo clean
pyautogui.write(login)

pyautogui.press("tab")

senha = "exemplodesenha"
pyautogui.write(senha)

pyautogui.press("tab")
#dava p eu fazer com click tb
pyautogui.press("enter")
time.sleep(3)
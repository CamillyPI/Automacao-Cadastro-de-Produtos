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

lista = pandas.read_csv("C:\\Users\\Windows\\Downloads\\PYTHONPOWERUP\\produtos.csv") # importar a lista para uma variavel usando a biblioteca

for linha in lista.index: # pegando a linha (.index) da minha variavel lista

    pyautogui.click(x=727, y=242)
    
    # filtrar usando: variavel.loc[linha, coluna] obs: ele comeca a contar a linha do 0 automaticamente
    # ja que eh lista.index
    pyautogui.write(str(lista.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(lista.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(lista.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(lista.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(lista.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(lista.loc[linha, "custo"]))
    pyautogui.press("tab")

    # se a informacao da variavel obs, que eh equivalente a obs da lista pois esta como lista.loc, NAO for NAO NAN 
    # (not a number), escreva a obs escrita 
    obs = lista.loc[linha, "obs"]
    if not pandas.isna(obs): # isna = is number, entao se nao for vazio (not a number)
        pyautogui.write(obs) # escreva obs

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("pageup") # da pra fazer com pyautogui.scroll(valor) exemplo: 1000 ou -1000)
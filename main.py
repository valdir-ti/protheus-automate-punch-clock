import os
import time
import pyautogui
import pyperclip
import subprocess
from dotenv import load_dotenv

# Carrega as variaveis de ambiente
load_dotenv()
SECRET_LINK = os.environ.get('SECRET_LINK')
SECRET_PIN = os.environ.get('SECRET_PIN')
SECRET_CPF = os.environ.get('SECRET_CPF')

# Abre o Google Chrome
subprocess.run(['google-chrome'])
    
time.sleep(5)

# Foca na barra de digitação do navegador
pyautogui.hotkey('ctrl', 'l')

# Copia o link para a área de transferência
pyperclip.copy(SECRET_LINK)

# Cola o link na área de endereço
pyautogui.hotkey('ctrl', 'v')

# Pressiona Enter para abrir o link
pyautogui.press('enter')

time.sleep(5)

# Maximiza a tela
pyautogui.hotkey('F11')

time.sleep(5)

# Clica no botão de login
pyautogui.click(x=630, y=440, duration=1)

time.sleep(2)

# Clica no menu para abrir as opções
pyautogui.click(x=100, y=225, duration=1)

time.sleep(2)

# Clica para a abrir a tela de marcar o ponto
pyautogui.click(x=70, y=370, duration=1)

time.sleep(5)

# Clica no centro de tela, segura o botão clicado e arrasta para o lado
pyautogui.moveTo(1400, 530)
pyautogui.mouseDown(button='left')
pyautogui.dragTo(1300, 530, 2)

time.sleep(3)

# Tira a maximização da tela
pyautogui.hotkey('F11')

time.sleep(2)

# Fecha o navegador
pyautogui.hotkey('ctrl', 'w')

time.sleep(2)

# Fecha o VSCode
pyautogui.hotkey('alt', 'f4')

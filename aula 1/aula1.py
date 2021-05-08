#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pyautogui
import time
import pyperclip

# sempre q um comando ser executado, vai esperar 1 segundo
pyautogui.PAUSE = 1

# pyautogui.alert("O programa vai ser executado, não use o programa. Quando ele finalizar, um alerta do termino do programa será feito.")

def abrir_firefox():
    pyautogui.click(666, 754)
    pyautogui.hotkey('ctrl','alt','t')
    time.sleep(3)
    pyautogui.write('firefox &')
    pyautogui.press('enter')
    time.sleep(3)

def acessar_google_drive():
    link = 'https://drive.google.com/drive/folders/1MR9mXuWKLzf7HdxE93VDPeFpJ6EHaXfU'
    pyperclip.copy(link)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep(5)

# def baixar_planilha_v1():
#     pyautogui.click(x=372, y=310, button='right')
#     time.sleep(2)
#     pyautogui.click(x=464, y=652)
#     time.sleep(3)
#     pyautogui.click(x=792, y=221)
#     time.sleep(3)
#     pyautogui.click(x=876, y=512)

def baixar_planilha_v2():
    pyautogui.click(x=414, y=279, button='right')
    time.sleep(2)
    pyautogui.click(x=475, y=655)
    time.sleep(3)
    pyautogui.click(x=780, y=220)
    time.sleep(3)
    pyautogui.click(x=889, y=510)

abrir_firefox()
acessar_google_drive()
baixar_planilha_v2()


# In[61]:


# encotrar posição x e y do cursos na tela
# pyautogui.position()


# In[62]:


import pandas as pd

# elimina os codigos secretos (\n\s) e le da forma q ta escrito
tabela = pd.read_excel(r"/home/boibandido/Downloads/Vendas - Dez.xlsx") 
display(tabela)

faturamento = tabela["Valor Final"].sum()
qtd_produtos = tabela["Quantidade"].sum()


# In[63]:


import credenciais
# envio de email usando o site gmail com pyautogui ou a api do python
import smtplib
import unicodedata

# f diz q vai usar variaveis dentro da string
texto_email = f"""
Prezados, bom dia

O faturamento foi de R${faturamento:,.2f}
A quantidade de produtos foi de: {qtd_produtos}

Abs
Felippe
"""

texto_email = unicodedata.normalize('NFKD', texto_email).encode('ascii', 'ignore').decode('utf8')
conection = smtplib.SMTP_SSL(credenciais.smtp_server, credenciais.smtp_port_ssl)
conection.login(credenciais.email, credenciais.senha)
conection.sendmail(credenciais.email, credenciais.email, texto_email)
conection.quit()
print("Email enviado!")


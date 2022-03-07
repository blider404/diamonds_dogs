import tkinter
import webbrowser
import time
import platform
import pyautogui
from tkinter import *

print('ola\nmeu nome e jarvis')
time.sleep(2)
print('ainda estou em versao de teste')
time.sleep(2)
nome = input('Qual o seu nome?')
nome = nome.strip()

so = platform.system()
if so == 'Windows':
    print("vc esta usando windows")
elif so == 'Linux':
    print('voce esta usando linux')
else:
    print('nao detectado')

if nome == 'iago':
    print('que nome bonito voce tem ')
else:
    print('humm')
# dados
autura = float(input('qual sua aultura ' + nome + '?'))
peso = float(input('qual o seu peso?'))
idade = int(input('quantos anos vc tem?'))
# cauculo proteinas diarias
calc1 = (peso*2)
print('OK\nestes são seus dados\nNome:{}\nAutura: {}\nPeso: {}\nIdade: {}'.format(nome, autura, peso, idade))
# pergunta de correção
core = str(input('esta tudo certo {}?'.format(nome)))
if core == 'sim':
    print('ok')
    print('vc precisa ingerir {} gramas de proteinas ao dia'.format(calc1))
else:
    print('pederia refazer o formulario')

input('ok?')

print('iremos abrir uma interface grafica')
time.sleep(1)
input('ok?')


#abrir navegador
print('vamos abrir o google')
time.sleep(3)
webbrowser.open('https://www.google.com/')

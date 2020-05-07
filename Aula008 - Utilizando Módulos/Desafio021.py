# Desafio 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo em mp3.

import os; print(os.getcwd())
os.path.join(os.path.dirname(__file__), 'C:\Users\Diego\Documents\MeusProjetos\Curso-Python-3\Aula008 - Utilizando Módulos\aula008.mp3')

from pygame import mixer

mixer.init() #Utilizado para iniciar o módulo "pygame".
mixer.music.load('C:\Users\Diego\Documents\MeusProjetos\Curso-Python-3\Aula008 - Utilizando Módulos\aula008.mp3') #Carrega o arquivo.
mixer.music.play() #Executar o player.
input() #Espera a música encerra para o player

'''import playsound
playsound.playsound('aula008_desafio021.mp3')'''
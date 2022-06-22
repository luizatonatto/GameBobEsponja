import random
import time
import pygame

def dados():
    nome = input("Digite seu nome: ")
    email= input ("Digite seu e-mail: ")

    arquivo = open("dados.bob","w")
    arquivo.write (nome)
    arquivo.write ("\n")
    arquivo.write (email)
    arquivo.close()

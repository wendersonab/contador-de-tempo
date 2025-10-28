import time
import sys
import os
import winsound

menu = "           Calcular Minutos"
linha = "-"*40

def printMenu():
    print(f"{linha}\n{menu}\n{linha}")

def opcoes():
    print("1. Adicionar minutos\n2. Remover minutos\n3. Adicionar horas\n4. Remover horas\n5. Mostrar timer\n6. Iniciar timer\n7. Sair")

def voltar():
    input("Digite qualquer tecla para voltar: ")
    for i in range(4):
        voltando = "Voltando" + "."*i
        sys.stdout.write("\r"+voltando)
        time.sleep(.3)
    print()
    os.system("cls")

minutos = 0
horas = 0

def um():
    global minutos, horas
    while True:
        try:
            minutoAdicionado = int(input("Digite os minutos a serem adicionados ao contador: "))
            minutos += minutoAdicionado
            while minutos >= 60:
                horas += 1
                minutos -= 60
            if minutos < 10:
                print(f"Minutos adicionados: {horas}:0{minutos} h")
            else:
                print(f"Minutos adicionados: {horas}:{minutos} h")
            break
        except ValueError:
            print("Digite um valor inteiro.")
def dois():
    global minutos, horas
    while True:
        if minutos == 0 and horas == 0:
            print("Não há tempo cadastrado!")
            break
        else:
            try:
                minutosRemovidos = int(input("Digite o total de minutos a serem removidos: "))
                minutos += horas * 60
                horas = 0
                if minutosRemovidos > minutos:
                    print(f"Você não pode retirar {minutosRemovidos} de {minutos}.\nTente novamente.\n")
                    while minutos >= 60:
                        horas += 1
                        minutos -= 60
                elif minutosRemovidos < 0:
                    print("Você não pode remover minutos negativos.\nTente novamente.\n")
                    while minutos >= 60:
                        horas += 1
                        minutos -= 60
                else:
                    minutos -= minutosRemovidos
                    print(f"Minutos removidos: {minutosRemovidos} min")
                    while minutos >= 60:
                        horas += 1
                        minutos -= 60
                    break
            except ValueError:
                print("Digite um valor inteiro.")
def tres():
    global horas
    while True:
        try:
            horasAdicionadas = int(input("Digite a quantidade de horas a serem adicionadas: "))
            if horasAdicionadas >= 0:
                horas += horasAdicionadas
                print(f"Você adicionou {horasAdicionadas} h.")
                break
            else:
                print("Digite um valor válido.\n")
        except ValueError:
            print("Digite um número inteiro.\nTente novamente.\n")
def quatro():
    global horas
    while True:
        try:
            horasRemovidas = int(input("Digite o valor em horas a ser removido: "))
            if horasRemovidas > horas:
                print(f"Não é possível remover {horasRemovidas} h de {horas} h.\nTente novamente.\n")
            elif horasRemovidas < 0:
                print("Digite um número maior do que zero.\n")
            else:
                horas -= horasRemovidas
                print(f"Horas removidos: {horasRemovidas} h")
                break
        except ValueError:
            print("Digite um valor inteiro.\n")


def cinco():
    if minutos < 10:
        print(f"{horas}:0{minutos} h")
    else:
        print(f"{horas}:{minutos} h")
def seis():
    global horas, minutos
    segundos = 0
    if minutos > 0 and segundos == 0:
        segundos = 60
        minutos -= 1
    input("Digite qualquer tecla para iniciar o contador. ")
    while True:
        while horas > 0 or minutos > 0 or segundos >= 0:
            while horas > 0 or minutos > 0 or segundos >= 0:
                tempo = f"{horas:02d}:{minutos:02d}:{segundos:02d} h"
                sys.stdout.write("\r" + tempo)
                sys.stdout.flush()
                time.sleep(1)
                segundos -= 1
                # Ajuste de tempo
                if segundos < 0 and (minutos > 0 or horas > 0):
                    segundos = 59
                    minutos -= 1

                if minutos < 0 and horas > 0:
                    minutos = 59
                    horas -= 1

                # Sai do loop quando tudo chega a zero
                if horas == 0 and minutos == 0 and segundos < 0:
                    break
        print("\nContador esgotado...")
        winsound.PlaySound("alarme.wav", winsound.SND_FILENAME)

        break
while True:
    printMenu()
    opcoes()
    print(linha)
    try:
        opcao = int(input("Digite a opção desejada: "))
        if 0 < opcao <= 6:
            while opcao == 1:
                um()
                voltar()
                break
            while opcao == 2:
                dois()
                voltar()
                break
            while opcao == 3:
                tres()
                voltar()
                break
            while opcao == 4:
                quatro()
                voltar()
                break
            while opcao == 5:
                cinco()
                voltar()
                break
            while opcao == 6:
                seis()
                voltar()
                break
        if opcao == 7:
            for i in range(4):
                sair = "Saindo" + "."*i
                sys.stdout.write("\r"+sair)
                time.sleep(1)
            print()
            break
    except ValueError:
        print("Digite um valor inteiro.")
        time.sleep(3)
        os.system("cls")